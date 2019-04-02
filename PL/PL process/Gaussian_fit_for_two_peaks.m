function []=Gaussian_fit_for_two_peaks()
set(0,'DefaultFigureWindowStyle','docked')
filenames=dir('*.txt');
resolution_set = 1;
group = 'Updates';
pref =  'Conversion';
quest = {'Are there two peaks or just one'};
pbtns = {'Yes','No'};
[pval,~] = uigetpref(group,pref,'Converting',quest,pbtns);
answer = inputdlg({'the range of peak 1(ex. "1 2")','the range of peak 2(ex. "1 2")','second peak (yes/no)'},'Input',[1 35],{'460 480', '540 560' 'no'});
temp = strsplit(answer{1});
range_1_lower = str2double(temp{1});
range_1_upper = str2double(temp{2});
temp = strsplit(answer{2});
range_2_lower = str2double(temp{1});
range_2_upper = str2double(temp{2});
%% set options
options1 = fitoptions('gauss1');  % the code currently only does gauss1 for the PL code
options1.MaxIter = 10000;
%options1.DiffMaxChange = 100;
%options1.StartPoint = [3e4 (range_1_lower+range_1_upper)/2 30];
%options1.Upper = [Inf 800 100];
%options1.Lower = [100 700 -inf];
%% set options2
options2 = fitoptions('gauss1');  % the code currently only does gauss1 for the PL code
options2.MaxIter = 10000;
%options2.DiffMaxChange = 100;
%options2.StartPoint = [3e4 (range_2_lower+range_2_upper)/2 30];
%options2.Upper = [Inf 800 100];
%options2.Lower = [100 700 -inf];
%% gather initial time
temp_name = strings(1,size(filenames,1));
i = 1;
miliseconds= str2double(filenames(i).name(1,end-6:end-4));
seconds= str2double(filenames(i).name(1,end-9:end-8));
minutes= str2double(filenames(i).name(1,end-12:end-11));
hours= str2double(filenames(i).name(1,end-15:end-14));
time_start = round(hours*60*60+minutes*60+seconds+miliseconds/1000,resolution_set);
time = NaN(1,size(filenames,1));
for i=1:size(filenames,1)
    miliseconds= str2double(filenames(i).name(1,end-6:end-4));
    seconds= str2double(filenames(i).name(1,end-9:end-8));
    minutes= str2double(filenames(i).name(1,end-12:end-11));
    hours= str2double(filenames(i).name(1,end-15:end-14));
    fileID = fopen(filenames(i).name(1,:),'r');
    data(i).data = textscan(fileID,'%f %f %[^\n]','HeaderLines',13,'Delimiter','\t');
    time(1,i) = round(hours*60*60+minutes*60+seconds+miliseconds/1000-time_start); % milisecond is considered at this code
    fclose (fileID);
end
intensity = NaN([size(filenames,1) size(data(1).data{1,2},1)]);
for i =1:size(filenames,1)
    intensity(i,:)=data(i).data{1,2};
    temp_name(i) = filenames(i).name;
end
%% plot normalized for peak 1
figure
hold on
set(gca, 'ColorOrder', jet(size(filenames,1)));
set(gcf, 'Colormap', jet(size(filenames,1)));
index_range = find(data(i).data{1,1}>range_1_lower & data(i).data{1,1}<range_1_upper);
for i=1:size(filenames,1)
    plot(data(i).data{1,1},intensity(i,:)/max(intensity(i,index_range)));
end

figure
plot(time,max(intensity(:,index_range),[],2));
disp('program finished');
title('peak 1 max over time')
xlabel('time (s)')
xlim([400 600]);
%% plot normalized for peak 2
figure
hold on
set(gca, 'ColorOrder', jet(size(filenames,1)));
set(gcf, 'Colormap', jet(size(filenames,1)));
index_range = find(data(i).data{1,1}>range_2_lower & data(i).data{1,1}<range_2_upper);
for i=1:size(filenames,1)
    plot(data(i).data{1,1},intensity(i,:)/max(intensity(i,index_range)));
end
xlim([400 600]);
%% plot for peak max change
figure
plot(time,max(intensity(:,index_range),[],2));
disp('program finished');
%% plot unnormalized
figure
hold on
set(gca, 'ColorOrder', jet(size(filenames,1)));
set(gcf, 'Colormap', jet(size(filenames,1)));
for i=1:size(filenames,1)
    plot(data(i).data{1,1},intensity(i,:));
end
xlim([400 600]);
%% fit gaussian stop here before fitting
disp('fitting');
fit_range_1 = find(data(i).data{1,1}>range_1_lower & data(i).data{1,1}<range_1_upper);
fit_range_2 = find(data(i).data{1,1}>range_2_lower & data(i).data{1,1}<range_2_upper);
gof_1 = NaN(1,size(filenames,1));
gof_2 = NaN(1,size(filenames,1));
fwhm_gauss_1 = NaN(1,size(filenames,1));
fwhm_gauss_2 = NaN(1,size(filenames,1));
for i=1:size(filenames,1)
    if max(data(i).data{1,2}) > 100
        %[pks, locs, w, ~] = findpeaks(data(i).data{1,2},'MinPeakHeight',100,'MinPeakDistance',50); %finding fwhm with pkfind
        %normalized_plot = data(i).data{1,2}/max(data(i).data{1,2});
        %plot(data(i).data{1,1},normalized_plot+i);
        [f_gauss1_1, gof1] = fit(data(i).data{1,1}(fit_range_1), data(i).data{1,2}(fit_range_1),'gauss1',options1);
        [f_gauss1_2, gof2] = fit(data(i).data{1,1}(fit_range_2), data(i).data{1,2}(fit_range_2),'gauss1',options1);
        gof_1(i) = gof1.rsquare;
        gof_2(i) = gof2.rsquare;
        temp1 = coeffvalues(f_gauss1_1);
        temp2 = coeffvalues(f_gauss1_2);
        f_gauss_1_numeric = @(t) temp1(1,1)*exp(-((t-temp1(1,2))/temp1(1,3)).^2);
        f_gauss_2_numeric = @(t) temp2(1,1)*exp(-((t-temp2(1,2))/temp2(1,3)).^2);
        fwhm_gauss_1(1,i) =  fwhm(f_gauss_1_numeric(data(i).data{1,1}(fit_range_1)),data(i).data{1,1}); %finding fwhm after gaussian fit
        fwhm_gauss_2(1,i) =  fwhm(f_gauss_2_numeric(data(i).data{1,1}(fit_range_2)),data(i).data{1,1}); %finding fwhm after gaussian fit
        %integration(i) = integral(f_gauss_numeric,0,1000); %integral of fitted curve
        %integration_numerical(i) = trapz(data(i).data{1,1},data(i).data{1,2});
    end
end
disp('plotting data')
%% plot
figure;
hold on
plot(fwhm_gauss_1);
plot(fwhm_gauss_2);
title('FWHM');
figure
hold on
plot(gof_1)
plot(gof_2)
end