function [intensity_acquire, time_frame] = intac(data_mat,row_per_frame,num_row,time_per_frame,frame_start,frame_end)
frame_start = frame_start-1;
if data_mat(1,1) == 0
    
    intensity_acquire = zeros (row_per_frame,frame_end);
    for k = frame_start*row_per_frame+1:num_row
        index = data_mat(k,1)-frame_start+1;
        index_loop = rem(k,row_per_frame);
        if index_loop == 0
            index_loop = row_per_frame;
        end
        intensity_acquire(index_loop,index) = data_mat(k,3);
    end
    time_frame = 0 : time_per_frame : (frame_end-1)*time_per_frame;
elseif data_mat(1,1) == 1
       
    intensity_acquire = zeros (row_per_frame,frame_end-1);
    for k = frame_start*row_per_frame+1:num_row
        index = data_mat(k,1)-frame_start;
        index_loop = rem(k,row_per_frame);
        if index_loop == 0
            index_loop = row_per_frame;
        end
        intensity_acquire(index_loop,index) = data_mat(k,3);
    end
    time_frame = 0 : time_per_frame : (frame_end-1)*time_per_frame;
    
end
