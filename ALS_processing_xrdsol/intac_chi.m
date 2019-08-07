function [intensity_acquire, time_frame] = intac_chi(data_mat,row_per_frame,num_row,time_per_frame,frame_start,frame_end)
intensity_acquire = zeros (row_per_frame,frame_end);
frame_start = frame_start-1;
if data_mat(1,2) == 0
    for k = frame_start*row_per_frame+1:num_row
        index = data_mat(k,2)-frame_start+1;
        index_loop = rem(k,row_per_frame);
        if index_loop == 0
            index_loop = row_per_frame;
        end
        intensity_acquire(index_loop,index) = data_mat(k,3);
    end
    time_frame = 0 : time_per_frame : (frame_end-1)*time_per_frame;
elseif data_mat(1,2) == 1
    for k = frame_start*row_per_frame+1:num_row
        index = data_mat(k,2)-frame_start;
        index_loop = rem(k,row_per_frame);
        if index_loop == 0
            index_loop = row_per_frame;
        end
        intensity_acquire(index_loop,index) = data_mat(k,3);
    end
    time_frame = 0 : time_per_frame : (frame_end-1)*time_per_frame;
    
end
