function []= phasematch(intensity,resolution,twotheta_start,twotheta_end,prec_name,time_per_frame)
%% 
addpath ('H:\ALS_processing_matlab');
cd H:\ALS_processing_matlab\reference
list_name = ls ('*.csv');
list_name = 'MAPbI3 Ref XRD Cubic.csv';
disp (list_name);
temp = size(list_name,1);
fileID = zeros (temp,1);
ref = struct('crys', cell(1, temp(1)));


numofmaxpeaks = 15;
sample_time = 10; %time between each sample

t = 1: sample_time:size(intensity,2);
ColorSet = varycolor(round(size(intensity,2)/sample_time));
figure (1)
clf
axis([5 inf 0 inf])
for i = 1:temp
    fileID(i) = fopen (list_name(i,:));    
    ref(i).phase = cell2mat(textscan (fileID(i), '%f %f %f %f %f %f %f %f %f','delimiter',',','HeaderLines',1));
    temp_peak_loc = sortrows(ref(i).phase,4,'descend');
    hold on
    set(gca, 'ColorOrder', ColorSet);
    set(gcf, 'Colormap', ColorSet);
    colorbar
    caxis([0 time_per_frame*size(intensity,2)]);
    for k = 1:size(t,2)
        plot((twotheta_start:resolution:twotheta_end),intensity(:,t(k))+3*k);
    end
    set(gca, 'YTick', []); %set Ytick invisible
    for j = 1:numofmaxpeaks
        if j < size(temp_peak_loc,1)
            x = temp_peak_loc(j,2);
            mindex = [ '[' num2str(abs(ref(i).phase(j,6))) num2str(abs(ref(i).phase(j,7))) num2str(abs(ref(i).phase(j,8))) ']'];
            if x>twotheta_start && x < twotheta_end
                y = 1:135;
                plot([x x],[y(1) y(end)], 'g--');
                text(x-2,y(end)-5-2*j,mindex,'FontSize',14);
                text(x-1,y(end)-5-2*j,num2str(x),'FontSize',14);
            else
            end
        else
        end
    end
    xticks(5:5:50);
    xticklabels(5:5:50);
    temp_name = strsplit(strtrim((list_name(i,:))),'.csv');
    saveas(gcf,[prec_name '_' num2str(time_per_frame) '_' temp_name{1} '.png'],'tiffn');
    clf
end
hold off

