function [exist_phase]= phase_match_repo(frame_end, pos_tol, num_peak,locs_peak, error_tol,time_frame)
addpath ('E:\ALS_processing_matlab');
cd E:\ALS_processing_matlab\reference
list_name = ls ('*.csv');
disp (list_name);
num_ref = size(list_name,1);
ref = struct('crys', cell(1, num_ref(1)));
for i = 1:num_ref
    fileID = fopen (strtrim(list_name(i,:)));    
    ref(i).phase = cell2mat(textscan (fileID, '%f %f %f %f %f %f %f %f %f','delimiter',',','HeaderLines',1));
end
%% sort 
exist_phase = zeros(num_ref,frame_end);
figure
%for j = 1:temp_2
%    smoothdata (int_peak(j,:),'sgolay');
%end

% for each frame 
% match peaks until two peaks within the tolerence range is matched
% then with the top 2 matched peaks, compare if the error is within
% error_tol i.e. are they off by reference by the same margin
%
for k = 1:frame_end
    for i = 1:num_ref
        temp_peak_loc = sortrows(ref(i).phase,4,'descend'); % the peak with higer integration is more likely to be spotted
        for j = 1:num_peak
            o = 1;
            pos_error = zeros(1,2);
            while (pos_error(2) == 0 && size(temp_peak_loc,1)>= o  )
                
                if  temp_peak_loc(o,2) > locs_peak(j,k)-pos_tol && temp_peak_loc(o,2) < locs_peak(j,k)+pos_tol
                    perror = temp_peak_loc(o,2) - locs_peak(j,k); 
                    
                    if pos_error(1) == 0
                        pos_error(1) = perror;
                    else
                        pos_error(2) = perror;
                    end
                else
                end
                o = o+1;
            end
            if pos_error(1)~= 0 && pos_error(2) ~= 0
                if abs(pos_error(1)-pos_error(2))<= error_tol
                    exist_phase(i,k) = 1;
                else
                end
            else
            end
        end
    end
end
hold on
exist_phase(exist_phase==0) = NaN;
for p = 1:num_ref
    plot(time_frame, p-1+ exist_phase(p,:));
    
    temp = strsplit (list_name(p,:),'.csv') ;
    y_labels{p} = temp{1};
end
axis([0 inf 0 num_ref]);
yticks(1:1:num_ref);
yticklabels (y_labels);
set(gca,'TickLength',[0 0]);
hold off
end
