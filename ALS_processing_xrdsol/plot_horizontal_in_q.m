% 1. keep black box but with white ticks

[fname,path] = uigetfile(pwd,'Dat File','*.dat'); % set output folder
selpath_output = uigetdir(pwd,'output folder');
cd(path)
answer = inputdlg({'starting frame','time per frame (s)'},'Input',[1 35],{'15', '2'});
color_range = [100 105]; %colorbar range for the contour plot
time_per_frame = str2double(answer(2));
frame_start = str2double(answer(1));  % time zeroing
n = 500; %num of contour lines
fname_idx = strsplit(fname,'.d');
fname_idx = char(fname_idx(1));
fname_contour = strcat (fname_idx,'_contour');
%% import data
fileID = fopen(fname,'r+');
delimiter =  '\t';
A_data = textscan (fileID, '%f %f %f %f %f %f','Delimiter',delimiter,'HeaderLines',2); 
fclose (fileID);
cd(selpath_output)
data_mat = cell2mat (A_data);
temp = size(data_mat);
num_row = temp(1);%changes with the number of frames taken
if data_mat(1,2) == 0
    num_frame = data_mat(num_row,2)+1;
elseif data_mat(1,2) == 1
    num_frame = data_mat(num_row,2);
end
%% set parameters - partially manual
frame_end = num_frame-frame_start+1;
row_per_frame = rpf(data_mat);%acquires row per frame
dspace = data_mat(1:row_per_frame,3);
q = 2*pi./dspace;
[intensity, time_frame] = intac(data_mat,row_per_frame,num_row,time_per_frame,frame_start,frame_end);
%for i = 1:frame_end
%    l = intensity(:,i)<100;
%    intensity(l,i) = 100;
%end %normalize values lower than background
plot_range = q;
%csvwrite([fname_idx '_13' '.csv' ], [plot_range;intensity(:,13)']'); %
%output selected frame
%% Filled contour plotting
h = figure;
contourf(plot_range,time_frame,intensity,n,'LineStyle','none');
p = jet(128);
%p(1:16,:)=[linspace(1,0,16)',linspace(1,0,16)',linspace(1,1,16)'];
colormap(p)
caxis(color_range)
set(gca,'XMinorTick','on','YMinorTick','on')
FontName = 'Arial';
ylabel('Time (s)','FontSize',24,'FontName', FontName)
xlabel('q','FontSize',24,'FontName', FontName)
xticks (0.5:0.5:4.5)
xticklabels(0.5:0.5:4.5)
%set(gca,'TickDir','out');

xlim([0.8838 4.283]);
set(gca, 'FontSize', 22,'FontName', FontName);
set(gcf,'Position',[1 1 1536 703.2])
colorbar
a = gca;
set(a,'box','on','color','none');
a.PlotBoxAspectRatio =([3/4,1, 1]);
set(gcf,'color','white');

%% plot the zoomed graph
num_tick = 7;
for y_limit_2 = [60]% 600 1200 1800]
a.YLim=  [0 y_limit_2];
a.YTick = (linspace(0,y_limit_2,num_tick));
a.YTickLabel = (linspace(0,y_limit_2,num_tick));
a.YAxis.MinorTickValues = y_limit_2/12:y_limit_2/6:y_limit_2*11/12;
b = copyobj(a, gcf);
set(b,'Position',get(a,'Position'),'box','on','xlabel',[],'ylabel',[],'linewidth', 1.5);
set(b, 'Xcolor', [1 1 1], 'YColor', [1 1 1], 'XTickLabel', [], 'YTickLabel', [], 'XLabel', [], 'YLabel', [])
img = getframe(gcf);
imwrite(img.cdata, [fname_contour '_' num2str(y_limit_2) '.png']);
end
%%
function rpf_val = rpf(data_mat)
rpf_val = 0;
for k = 1:size(data_mat,1)
    if data_mat(k,2) == 1
        rpf_val = rpf_val+1;
    else
    end
end
end