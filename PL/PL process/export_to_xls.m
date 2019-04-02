function export_to_xls(filenames,integration,integration_numerical,fwhm_gauss,selpath,varargin)
% default time is 1 s
% varargin for time frame and filename delimiter
if nargin == 6   % if the number of inputs equals 1
    delimiter = '_FLMS'; % default options
    time = varargin{1};
elseif nargin == 5
    time = 1:size(filenames,1);
    delimiter = '_FLMS';
else
    time = varargin{1};
    delimiter = varargin{2};
end
cd(selpath)
T =table(time',integration',integration_numerical',fwhm_gauss','VariableNames',{'time','integration','integration_numerical','fwhm_gauss'});
output_name = strsplit(filenames(1),delimiter);
writetable(T,[output_name{1} '.xls']);
end