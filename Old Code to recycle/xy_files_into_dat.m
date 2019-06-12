filenames=dir('*.xy');
frame_start = 19;
time_per_frame = 2;
x_limit = 120;
color_range = [107 115];
num_frame = size(filenames,1);
frame_end=num_frame-frame_start+1;
data = cell(frame_end,1);
intensity = zeros(3298,frame_end);
k=1;
for i=frame_start:num_frame
    fileID = fopen(filenames(i).name(1,:),'r');
    data{1,k} = textscan(fileID,'%f %f %[^\n]','HeaderLines',1,'Delimiter','\t');
    fclose(fileID);
    A = cell2mat(data{1,k}(2));
    intensity(:,k) = A;
    k = k+1;
end
for i = 1:frame_end
    l = intensity(:,i)<100;
    intensity(l,i) = 100;
end %normalize values lower than background

twotheta_start = data{1,1}{1}(1);
twotheta_end = data{1,1}{1}(end);
time_frame = 0:time_per_frame:frame_end*time_per_frame;
resolution = data{1,1}{1}(2)-data{1,1}{1}(1);
plot_range = twotheta_start:resolution:twotheta_end;
h = figure;
contourf(time_frame,plot_range ,intensity(1:3297,:),100,'LineStyle','none');
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
set(gca,'box','off');
set(gca, 'FontSize', 22,'FontName', FontName)
daspect([(x_limit*3/4)/30 1 1])
saveas(h,[fname_contour '_' num2str(x_limit) '.jpg']);