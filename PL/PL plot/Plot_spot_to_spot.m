selpath = uigetdir(pwd,'sppot folder');
filenames=dir(join([selpath,'\*.txt']));
spot = NaN(1,size(filenames,1));
disp('importing');

for i=1:size(filenames,1)
    temp = strsplit(filenames(i).name(1,:),'_QEP');
    temp = strsplit(temp{1},'-spot');
    spot(i) = str2double(temp{2});
end
figure
hold on
[temp,idx] = sort(spot,'ascend');
for i=1:size(filenames,1)
    fileID = fopen(join([selpath,'\',filenames(idx(i)).name(1,:)]),'r');
    data(i).data = textscan(fileID,'%f %f %[^\n]','HeaderLines',13,'Delimiter','\t');
    fclose (fileID);
    fitting = fit(data(i).data{1,2},data(i).data{1,1} ,'gauss1');
    [~, locs] = findpeaks((data(i).data{1,2}/max(data(i).data{1,2})),data(i).data{1,1},'MinPeakHeight',0.9);
    %disp(locs)
    plot(data(i).data{1,1},(data(i).data{1,2}),'DisplayName',['spot' num2str(temp(i)) '@' num2str(locs(1))]);
end
legend
title('Front');
ylabel('Intensity (A.U.)');
xlabel('wavelength (nm)');
%set(gca, 'YTick', []); %set Ytick invisible
set(gca, 'XMinorTick', 'on');
xlim([600 900])
saveas(gcf,join([selpath,'\spot_to_spot.jpg']),'jpg');