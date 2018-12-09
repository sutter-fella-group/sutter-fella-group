function [] = sharpen (saturation,path)
addpath ('C:\Users\voidr\Desktop\Fiji.app\scripts');
javaaddpath 'C:\Program Files\MATLAB\R2018a\java\mij.jar';
list_name = ls ('*.png');
disp (list_name);
temp = size(list_name,1);
Miji;
%bkg = ['path=[' path '\' list_name(1,:) ']' ];
%MIJ.run('Open...', bkg);
%MIJ.selectWindow(list_name(1,:));
for i = 2:temp
    image_name = list_name(i,:);
    %% first subtract background
    image_loc = ['path=[' path '\' image_name ']'];
    bkg_loc = ['path=[' path '\' 'bkg.tif' ']'];
    MIJ.run('Open...', image_loc);
    MIJ.run("Gaussian Blur...", "sigma=60");
    MIJ.run("Save", bkg_loc);
    MIJ.run("Measure");
    temp_result = MIJ.getResultsTable;
    intensity_bkg = num2str(temp_result(1,2));
    MIJ.run('Open...', image_loc);
    command_temp = ['i1=' '[' image_name ']' ' i2=' '[' 'bkg.tif' ']' ' operation=[Divide: i2 = (i1/i2) x k1 + k2] k1=' intensity_bkg ' k2=0 create'];
    MIJ.run("Calculator Plus",command_temp);
    %% enhance contrast
    MIJ.selectWindow("Result");
    %MIJ.run("Normalize Local Contrast", "block_radius_x=40 block_radius_y=40 standard_deviations=3 center stretch");
    MIJ.run("Enhance Contrast...", ['saturated=' num2str(saturation)]);%saturation can be changed    
    %MIJ.run("Sharpen");
    %MIJ.run("Apply LUT");
    MIJ.run("Save", image_loc);
    MIJ.run('Close');
end
MIJ.run("Clear Results");
MIJ.closeAllWindows;
MIJ.exit;
end    