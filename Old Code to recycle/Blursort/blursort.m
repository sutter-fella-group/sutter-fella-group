function [t] = blursort(time_of_interest,fps,split_fname_tif_name,time_tol) 
fprintf('proceeding with image blur check\n');
%% pick out the filenames from folder
step = 1/fps;
A = zeros(2,int32((2*time_tol/step)+1));
A(2,:)=time_of_interest-time_tol:step:time_of_interest+time_tol;
if ~contains(pwd,'Separated_tif')
    cd Separated_tif
end
flag = 0;
i = time_of_interest-time_tol;
while flag == 0 && i < time_of_interest+time_tol
    pngFileName = strcat(split_fname_tif_name,'-t=', num2str(round(i,1)), '.png'); %creats a image file name
    if ~exist(pngFileName, 'file')
        flag  = 1;
    else
        imageData = imread(pngFileName);
        FM = fmeasure(imageData, 'GDER');
        A(1,int32((i-time_of_interest+time_tol)/step+1)) = FM;
        fprintf('%s \n',pngFileName);
        i = i + step;
    end
end
%% get index
t = max(A,[],2);
disp (t);
pngFileName1 = [split_fname_tif_name,'-t=', num2str(t(2)), '.png']; %move the marked files
copyfile (pngFileName1, 'Sorted');
cd ../
end