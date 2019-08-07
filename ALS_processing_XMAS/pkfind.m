function [peak_holder, locs_peak,temp_2,width_peak,pks] = pkfind(resolution,intensity,MinPeakHeight,MinPeakDistance,frame_start,frame_end,twotheta_start,position_tol)

locs_peak = zeros(100,frame_end);

peak_holder = zeros(100,1);

width_peak = zeros(100,frame_end);

pks_1 = zeros(100,frame_end);

peak_holder(1,1) = twotheta_start;%initialize by adding starting twotheta
for k = 1:frame_end
    
    int_all = intensity(:,k);
    
    [pks, locs, w, ~] = findpeaks(int_all,'MinPeakHeight',MinPeakHeight,'MinPeakDistance',MinPeakDistance);
    
    temp = size(locs);
    
    temp = temp(1);
    
    if temp ~= 0
        for j = 1:temp
            pks_1(j,k) = pks(j);
            locs_peak(j,k) = twotheta_start + locs(j)*resolution;
            width_peak(j,k) = w(j);
            
        end
    end
    
    peak_holder = peak_holder(peak_holder ~= 0);
    
    for j = 1:temp
        
        temp_2 = size (peak_holder);
        
        temp_2 = temp_2 (1);
        
        counter = 0; %%initialize counter
        
        for o = 1:temp_2
            
            if  locs_peak(j,k)<(peak_holder(o,1)-position_tol) || locs_peak(j,k)>(peak_holder(o,1)+position_tol) 
                    
                counter = counter + 1; 
                    
            end
        end
        if counter == temp_2
            
            peak_holder(temp_2+1,1) = locs_peak(j,k);
            
        else
            
        end
    end
    
end
pks = pks_1;

peak_holder = sort(peak_holder);

temp_2 = size (peak_holder);
        
temp_2 = temp_2 (1);

peak_holder = peak_holder(2:temp_2); %removes starting twotheta

temp_2 = temp_2 -1;