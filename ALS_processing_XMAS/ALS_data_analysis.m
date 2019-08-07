set(0,'DefaultFigureWindowStyle','docked')
[fname,path] = uigetfile(pwd,'Dat File','*.dat'); % set output folder
selpath_output = uigetdir(pwd,'output folder');
cd(path)
answer = inputdlg({'starting frame','time per frame (s)','time limit on x axis'},'Input',[1 35],{'15', '2','1800'});
x_limit = str2double(answer(3));
color_range = [105 130]; %colorbar range for the contour plot
num_peak_skip = 0;  % number of peaks to skip to speed up the process. Will change to be automatic
time_per_frame = str2double(answer(2));
frame_start = str2double(answer(1));  % time zeroing
n = 1000; %num of contour lines
MinPeakHeight = 107;
MinPeakDistance = 50;
position_tol = 0.5;
peak_width = 0.5;
fname_idx = strsplit(fname,'.d');
fname_idx = char(fname_idx(1));
fname_contour = strcat (fname_idx,'_contour');
%% fitting parameters
P0 = [];
BOUNDS = [0 -inf -inf -inf;
    inf inf inf inf];
options = optimset('MaxFunEvals',1500,'MaxIter',1000);
%% import data
fileID = fopen(fname,'r+');
delimiter =  '\t';
A_data = textscan (fileID, '%f %f %f %f %f %f','Delimiter',delimiter,'HeaderLines',1); 
fclose (fileID);
cd(selpath_output)
data_mat = cell2mat (A_data);
temp = size(data_mat);
num_row = temp(1);%changes with the number of frames taken
if data_mat(1,1) == 0
    num_frame = data_mat(num_row,1)+1;
elseif data_mat(1,1) == 1
    num_frame = data_mat(num_row,1);
end
%% set parameters - partially manual
frame_end = num_frame-frame_start+1;
row_per_frame = rpf(data_mat);%acquires row per frame
twotheta_start = data_mat(1,2);
twotheta_end = data_mat(row_per_frame,2);
resolution = data_mat(2,2) - data_mat(1,2);%acquires resolution
resolution =round(resolution,2);
[intensity, time_frame] = intac(data_mat,row_per_frame,num_row,time_per_frame,frame_start,frame_end);
for i = 1:frame_end
    l = intensity(:,i)<100;
    intensity(l,i) = 100;
end %normalize values lower than background
plot_range = twotheta_start:round(resolution,2):twotheta_end;
csvwrite([fname_idx '_13' '.csv' ], [plot_range;intensity(:,13)']');
%% acquire all possible peaks and locations
[peak_holder, locs_peak,num_peak,width_peak,~] = pkfind(resolution,intensity,MinPeakHeight,MinPeakDistance,frame_start,frame_end,twotheta_start,position_tol);
%% Filled contour plotting
h = figure;
contourf(time_frame,plot_range ,intensity,n,'LineStyle','none');
colormap(jet(256))
caxis(color_range)
set(gca,'XMinorTick','on','YMinorTick','on')
FontName = 'Arial';
xlabel('Time (s)','FontSize',22,'FontName', FontName)
ylabel('2\theta degree (Cu K\alpha)','FontSize',22,'FontName', FontName)
yticks (5:5:35)
yticklabels(5:5:35)
xticks(linspace(0,x_limit,4));
set(gca,'TickDir','out');
ylim([7 35]);
xlim([0 x_limit]);
set(gca, 'FontSize', 22,'FontName', FontName)
daspect([(x_limit*3/4)/30 1 1])
saveas(h,[fname_contour '_' num2str(x_limit) '.jpg']);
%colorbar
%saveas(h,[fname_contour '_' num2str(x_limit) '_colorbar' '.jpg']);
%% plot the zoomed graph
x_limit_2 = 120;
xlim([0 x_limit_2]);
xticks(linspace(0,x_limit_2,4));
daspect([(x_limit_2*3/4)/30 1 1])
saveas(h,[fname_contour '_120' '.jpg']);
%saveas(h,[fname_contour '_120_colorbar' '.jpg']);
%% align peak location
temp = zeros(num_peak,frame_end);
temp_width = zeros(num_peak,frame_end);
for j = 1:num_peak
    for k = 1:frame_end
        for i = 1:num_peak
            if locs_peak(j,k)>(peak_holder(i,1)-position_tol) && locs_peak(j,k)<(peak_holder(i,1)+position_tol)
                temp(i,k) = locs_peak(j,k);
                temp_width(i,k) = width_peak(j,k);
            end
        end
    end
end
locs_peak = temp;
width = temp_width*resolution;
%% smooth peak by filling in zeros with average between 2 values
for j = 1:num_peak
    for k = 1+2:frame_end-2
        if locs_peak(j,k) == 0 && locs_peak(j,k-1)~=0 && locs_peak(j,k+1)~= 0
           locs_peak(j,k) = locs_peak(j,k-1);
        end
        if locs_peak(j,k) ~= 0 && locs_peak(j,k-1) == 0 && locs_peak(j,k+1) == 0
            locs_peak(j,k) = 0;
        end
    end
end
%% match peaks and locations, yielding the time range for the appearance of the peaks
peak_frame = zeros (num_peak, frame_end);
for i = 1:num_peak
    for k = 1:frame_end
            if locs_peak(i,k)>(peak_holder(i,1)-peak_width) && locs_peak(i,k)<(peak_holder(i,1)+peak_width)  
                    peak_frame(i,k)= 1; 
            else
            end
    end
end
%% marks peak twotheta range for analysis
peak_start = zeros (num_peak,frame_end);
peak_end = zeros (num_peak,frame_end);
for k = 1:frame_end
    for j = 1:num_peak
        peak_start(j,k) = locs_peak(j,k)- peak_width;
        peak_end(j,k) = locs_peak(j,k)+ peak_width;
        if peak_end (j,k) > twotheta_end
            peak_end(j,k) = twotheta_end;
        end
        if peak_start (j,k) < twotheta_start
            peak_start(j,k) = twotheta_start;
        end
    end
end
%% peak fitting loops
width_fitted = zeros(num_peak,frame_end);
int_peak = zeros(num_peak,frame_end);
for j = 1+num_peak_skip:num_peak
    for k = 1:frame_end
        if peak_frame(j,k) == 1
            x = uint32((peak_start(j,k) - twotheta_start)/resolution+1);
            y = uint32((peak_end(j,k) - twotheta_start)/resolution+1);
            y_select_peak = intensity (x:y,k);
            peak_range = peak_start(j,k):resolution:peak_end(j,k);
            [~, P, ~, ~] = lorentzfit (peak_range', y_select_peak,P0,BOUNDS,'3c',options);
            f_integration = @(g) P(1)./((g - P(2)).^2 + P(3));
            width_fitted(j,k) = fwhm(f_integration(peak_range'),peak_range');
            int_peak(j,k) = integral(f_integration,peak_start(j,k),peak_end(j,k));
            %int_peak(j,k)= trapz(peak_range', y_select_peak-P(4));  %calculate the numerical integration to check goodness of fit
        end
    end
end
%% save plots to file
for idx_peak = 1
    domain = 0.15406*0.94/cos(peak_holder(idx_peak)*2*pi/360)./(2*pi*(width_fitted(idx_peak,:))/360);
    h2 = figure(2);
    plot (time_frame,domain);
    xlabel('Time(s)')
    ylabel('Crystal domain size (nm)')
    temp = strcat(fname_idx,'_domain_',num2str(peak_holder(idx_peak)));
    fname_domain_temp = strcat(fname_idx,'domain',num2str(peak_holder(idx_peak)),'.txt');
    fileID = fopen(fname_domain_temp,'w');
    fprintf(fileID,'%.4f\n',domain);
    fclose(fileID);
    savefig(h2,[temp '.fig']);
    h3 = figure(3);
    plot(time_frame,locs_peak(idx_peak,:));
    xlabel('Time(s)')
    ylabel('Peak Position')
    temp = strcat(fname_idx,'_position_',num2str(peak_holder(idx_peak)));
    %saveas(h3,temp,'tiffn'); %reserved for saving as .tif
    savefig(h3,[temp '.fig']);
    h4 = figure (4);
    plot (time_frame,int_peak(idx_peak,:)/max(int_peak(idx_peak,:)))
    xlabel('Time(s)')
    ylabel('Integration')
    temp = strcat(fname_idx,'_integration_',num2str(peak_holder(idx_peak)));
    savefig(h4,[temp '.fig']);
end
function rpf_val = rpf(data_mat)
rpf_val = 0;
for k = 1:size(data_mat,1)
    if data_mat(k,1) == 1
        rpf_val = rpf_val+1;
    else
    end
end
end