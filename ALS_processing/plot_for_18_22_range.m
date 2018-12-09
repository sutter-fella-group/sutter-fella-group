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
n = 200; %num of contour lines
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
[intensity, time_frame] = intac(data_mat,row_per_frame,num_row,time_per_frame,frame_start,frame_end);
for i = 1:frame_end
    l = intensity(:,i)<100;
    intensity(l,i) = 100;
end %normalize values lower than background
%% Filled contour plotting
plot_range = twotheta_start:round(resolution,2):twotheta_end;
h = figure;
contourf(time_frame,plot_range ,intensity,n,'LineStyle','none');
colormap(jet(256))
caxis(color_range)
set(gca,'XMinorTick','on','YMinorTick','on')
FontName = 'Arial';
xlabel('Time (s)','FontSize',22,'FontName', FontName)
ylabel('2\theta degree (Cu K\alpha)','FontSize',22,'FontName', FontName)
yticks (15:1:21)
yticklabels(15:1:21)
xticks(linspace(0,x_limit,4));
set(gca,'TickDir','out');
ylim([18 21.5]);
xlim([0 x_limit]);
set(gca,'box','off');
set(gca, 'FontSize', 22,'FontName', FontName)
daspect([(x_limit*3/4)/6.5 1 1])
saveas(h,[fname_contour '_' num2str(x_limit) '.jpg']);
function rpf_val = rpf(data_mat)
rpf_val = 0;
for k = 1:size(data_mat,1)
    if data_mat(k,1) == 1
        rpf_val = rpf_val+1;
    else
    end
end
end