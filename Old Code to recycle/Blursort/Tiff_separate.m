function [image_time_init, image_time_end, fps] = Tiff_separate(fname , frame_start,split_fname_tif_name,idx_start)   
    info = imfinfo(fname);
    num_images = numel(info);
    if isempty(find(fname=='_', 1))
        index_tif = 1;
    else
        temp = strsplit(fname,'_');
        temp = strsplit(temp{2},'.tif');
        index_tif = str2double (temp{1})+2;
    end
    temp_1 = strsplit(fname, 'fps');
    temp_2 = strsplit(temp_1{1},'-');
    fps = str2double(temp_2{end}); %frames per second
    image_time_init = ((index_tif-idx_start)*num_images + 1 - frame_start)/fps; %time in s
    image_time_end = image_time_init+ (num_images-1)/fps;
    for k = 1:1:num_images
        fprintf('converting image');
        disp(k);
        Tif_page = imread(fname, k);
        imgname = strcat(split_fname_tif_name,'-t=',num2str(image_time_init+(k-1)/fps),'.png');
        imwrite(Tif_page,imgname);
        movefile(imgname, 'Separated_tif');
    end
    fprintf('convert completed.\n');
end