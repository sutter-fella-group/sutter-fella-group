selpath = uigetdir(pwd,'sppot folder');
filenames=dir(join([selpath,'\*.txt']));
figure
hold on
for i=1:size(filenames,1)
    fileID = fopen(join([selpath,'\',filenames(i).name(1,:)]),'r');
    data(i).data = textscan(fileID,'%f %f %[^\n]','HeaderLines',13,'Delimiter','\t');
    fclose (fileID);
    [~, locs] = findpeaks((data(i).data{1,2}/max(data(i).data{1,2})),data(i).data{1,1},'MinPeakHeight',0.9);
    %disp(locs)
    plot(data(i).data{1,1},(data(i).data{1,2}));
end
legend
title('Front @ 160K');
ylabel('Intensity (A.U.)');
xlabel('wavelength (nm)');
%set(gca, 'YTick', []); %set Ytick invisible
set(gca, 'XMinorTick', 'on');
xlim([600 900])
saveas(gcf,join([selpath,'\spot_to_spot.jpg']),'jpg');