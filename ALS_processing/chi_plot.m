set(0,'DefaultFigureWindowStyle','docked')
fname = ls('*.dat');
fname_idx = strsplit(fname,'.d');
fname_idx = char(fname_idx(1));
fname_contour = strcat (fname_idx,'.jpg');
%% import data
fileID = fopen(fname,'r+');
delimiter =  '\t';
%data_mat= importfile_chi(fname);
A_data = textscan (fileID, '%f %f %f %f %f %f','Delimiter',delimiter,'HeaderLines',1); 
fclose (fileID);
data_mat = cell2mat (A_data);
temp = size(data_mat);
num_row = temp(1);%changes with the number of frames taken
if data_mat(1,2) == 0
    num_frame = data_mat(num_row,2)+1;
elseif data_mat(1,2) == 1
    num_frame = data_mat(num_row,2);
end
color_shift_time = 30;
time_per_frame = 2;
frame_start = 16;
frame_end = num_frame-frame_start+1;
resolution = round(data_mat(2,1) - data_mat(1,1),1);%acquires resolution
row_per_frame = rpf(data_mat);%acquires row per frame
chi_start = round(data_mat(1,1),2);
chi_end = round(data_mat(row_per_frame,1),2);
[intensity, time_frame] = intac_chi(data_mat,row_per_frame,num_row,time_per_frame,frame_start,frame_end);
ColorSet = varycolor(round(size(intensity,2)/color_shift_time));
time_output = [20 40 250 350 450 550 850 950 1050 1150];
frame_output = (time_output/2)+frame_start;
figure
hold on
for i = 1:length(frame_output)
csvwrite([fname_idx '_' num2str(time_output(i)) '.csv' ], [chi_start:round(resolution,2):chi_end;intensity(:,frame_output(i))']');
plot(intensity(:,frame_output(i)));
end
%figure
set(gca, 'ColorOrder', ColorSet);
set(gcf, 'Colormap', ColorSet);
hold on
plot_range = chi_start:resolution:chi_end;
k1 = find(plot_range<-20 & plot_range>-30); 
k2 = find(plot_range>-15 & plot_range<26.5);
filler = NaN([1 7]);
k_temp = 1:(length(k1)+length(k2)+length(filler));
plot_range_1 = plot_range(1,k_temp);
bias = 0;
t = 1: color_shift_time:size(intensity,2);
for o = 1:size(t,2)
    plot_intensity = [intensity(k1,t(o))', filler,intensity(k2,t(o))' ]  ;
    plot(plot_range_1,plot_intensity/max(plot_intensity)+0.17*o);
end
y_lim_up = 8;
start_1 = -25-bias;
start_2 = 17-bias;
xtick = [ -35 -25 -24.3 -20    -10 0 10 17 17.7];
xticklabels = {'-30', '-20','-15', '-10', '0', '10', '20', '27', '30' };
set(gca, 'YTick', linspace(1,y_lim_up,5));
set(gca,'XTick',xtick-bias)
set(gca,'XTicklabels',xticklabels)
ytick=get(gca,'YTick');
t1=text(start_1,ytick(1),'//','fontsize',24);
t3=text(start_2,ytick(1),'//','fontsize',24);
xlabel('\chi degree','FontSize',20,'FontName', 'Arial');
ylabel('Intensity','FontSize',20,'FontName', 'Arial');
xlim([-35-bias 17-bias]);
ylim([1 y_lim_up]);
hold off
%set(gca, 'XTick', [])
caxis([0 time_per_frame*size(intensity,2)]);
set(gca,'XMinorTick','off');
FontName = 'Arial';
set(gca,'TickDir','out');
set(gca, 'YTick', []); %set Ytick invisible
colorbar
%savefig(h, [fname_idx '.fig']);
%saveas(h,fname_contour,'jpg');
function rpf_val = rpf(data_mat)
rpf_val = 0;
for k = 1:100000
    if data_mat(k,2) == 1
        rpf_val = rpf_val+1;
    else
        break
    end
end
end