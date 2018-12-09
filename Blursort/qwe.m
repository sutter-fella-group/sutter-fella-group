frame_start = 86; %frame of sample placed on heating plate
idx_start = 1; % default is 1
%% Make a New Folder
addpath ('F:\MATLAB\Blursort');
addpath ('C:\Users\voidr\Desktop\Fiji.app\scripts');
if ~exist('Separated_tif', 'dir')
    mkdir('Separated_tif');
end
cd Separated_tif\
if ~exist('Sorted', 'dir')
    mkdir('Sorted');
end
if ~exist('rank_output','dir')
    mkdir('rank_output');
end
cd ../
list_name = ls ('*.tif');
disp (list_name);
temp = size(list_name,1);
image_name = zeros (temp,1);
for i = 1:temp
    fname = strtrim(list_name(i,:));
    split_fname_tif_name = strsplit(fname,'.tif');
    split_fname_tif_name = split_fname_tif_name{1};
    split_fname_tif_name = strsplit(split_fname_tif_name, '_');
    split_fname_tif_name = split_fname_tif_name{1};
    [~,time_end,fps] = Tiff_separate(fname , frame_start,split_fname_tif_name,idx_start);
end
%% sorting --- need further checking
time_of_interest = [ linspace(0, 10, 6) linspace(40, 60, 6) linspace(60, 300, 6) linspace(300, 1200, 6)];
for i = 1:length(time_of_interest)
    time_tol = [ones(1,6),repmat(2,1,6),repmat(5,1,6),repmat(10,1,6)];
    [~] = blursort(time_of_interest(i),fps,split_fname_tif_name,time_tol(i)); 
end
cd Separated_tif\Sorted
%%
%subtracts the first image as background, then sharpen
sharpen (0.35,pwd); %default saturation is 0.3 
%cd ../