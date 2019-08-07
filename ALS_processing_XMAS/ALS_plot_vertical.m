[fname,path] = uigetfile(pwd,'Dat File','*.dat'); % set output folder
selpath_output = uigetdir(pwd,'output folder');
cd(path)
answer = inputdlg({'starting frame','time per frame (s)','time limit on x axis'},'Input',[1 35],{'15', '2','1800'});
y_limit = str2double(answer(3));
color_range = [105 130]; %colorbar range for the contour plot
num_peak_skip = 0;  % number of peaks to skip to speed up the process. Will change to be automatic
time_per_frame = str2double(answer(2));
frame_start = str2double(answer(1));  % time zeroing
n = 400; %num of contour lines
MinPeakHeight = 107;
MinPeakDistance = 50;
position_tol = 0.5;
peak_width = 0.5;
fname_idx = strsplit(fname,'.d');
fname_idx = char(fname_idx(1));
fname_contour = strcat (fname_idx,'_contour');
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
%csvwrite([fname_idx '_13' '.csv' ], [plot_range;intensity(:,13)']'); %
%output selected frame
%% Filled contour plotting
h = figure;
contourf(plot_range,time_frame,intensity',n,'LineStyle','none');
p = jet(128);
p(1:16,:)=[linspace(1,0,16)',linspace(1,0,16)',linspace(1,1,16)'];
colormap(p)
caxis(color_range)
set(gca,'XMinorTick','on','YMinorTick','on')
FontName = 'Arial';
ylabel('Time (s)','FontSize',24,'FontName', FontName)
xlabel('2\theta degree (Cu K\alpha)','FontSize',24,'FontName', FontName)
xticks (5:5:35)
xticklabels(5:5:35)
yticks(linspace(0,y_limit,4));
yticklabels(linspace(0,y_limit,4));
set(gca,'TickDir','out');
xlim([7 35]);
ylim([0 y_limit]);
daspect([1 (y_limit)/30 1]);
set(gca, 'FontSize', 22,'FontName', FontName);
%set(gca,'box','off');
set(gcf,'Position',[1 1 1536 703.2])
%% remove extra ticks
colorbar
%% plot the zoomed graph
num_tick = 7;
for y_limit_2 = [60 120 300 600 1200 1800]
ylim([0 y_limit_2]);
yticks(linspace(0,y_limit_2,num_tick));
yticklabels(linspace(0,y_limit_2,num_tick));
daspect([1 y_limit_2/30 1]);
a = gca;
a.YAxis.MinorTickValues = y_limit_2/12:y_limit_2/6:y_limit_2*11/12;
b = copyobj(a,gcf);
b.YAxis.MinorTickValues = [];
set(b,'Position',get(a,'Position'),'box','on','xtick',[],'ytick',[],'xlabel',[],'ylabel',[]);
set(a,'box','off','color','none');
img = getframe(gcf);
imwrite(img.cdata, [fname_contour '_' num2str(y_limit_2) '.png']);
end
%%
function rpf_val = rpf(data_mat)
rpf_val = 0;
for k = 1:size(data_mat,1)
    if data_mat(k,1) == 1
        rpf_val = rpf_val+1;
    else
    end
end
end