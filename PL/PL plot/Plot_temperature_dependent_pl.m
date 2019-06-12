selpath = uigetdir(pwd,'spectrum folder');
filenames=dir(join([selpath,'\*.txt']));
temperature = NaN(1,size(filenames,1));
disp('importing');
figure
hold on
for i=1:size(filenames,1)
    temp = strsplit(filenames(i).name(1,:),'K_');
    if isnan(str2double(temp{1}))
        temp = strsplit(temp{1},'_');
        temperature(i) = str2double(temp{end});
    else
        temperature(i) = str2double(temp{1});
    end
end
[temp,idx] = sort(temperature,'ascend');
position = [];
for i=1:size(filenames,1)
    fileID = fopen(join([selpath,'\',filenames(idx(i)).name(1,:)]),'r');
    if fileID ~= -1
        data(i).data = textscan(fileID,'%f %f %[^\n]','HeaderLines',13,'Delimiter','\t');
        fclose (fileID);
        fitting = fit(data(i).data{1,2},data(i).data{1,1} ,'gauss1');
        fitting
        [~, locs] = findpeaks((data(i).data{1,2}/max(data(i).data{1,2})),data(i).data{1,1},'MinPeakHeight',0.6);
        plot(data(i).data{1,1},(data(i).data{1,2}/max(data(i).data{1,2}))+i/2,'DisplayName',[num2str(temp(i)) 'K' '@' num2str(locs(1))]);
        position = [position locs(1)];
    end
end
lgd = legend;
lgd.Location = 'eastoutside';
title('7s antisolvent drop ver. 2');
ylabel('Intensity (normalized)');
xlabel('wavelength (nm)');
set(gca, 'YTick', []); %set Ytick invisible
set(gca, 'XMinorTick', 'on');
xlim([700 1000])
saveas(gcf,join([selpath,'\Temp_dependent.jpg']),'jpg');
figure
temperature = temsperature(~isnan(temperature));
[temp,idx] = sort(temperature,'ascend');
plot(temp,position);
title('Peak Position vs. Temperature');
ylabel('Peak position (nm)');
xlabel('Temprature (K)');
saveas(gcf,join([selpath,'\Peak Position vs. Temperature.jpg']),'jpg');




