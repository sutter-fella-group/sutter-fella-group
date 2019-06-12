
%% creates ticks on right/top side
%axes('ylim', [5 45],'color', 'none','XTick',[], 'YAxisLocation', 'right')
%yticks (peak_holder)
%yticklabels(peak_holder)
%set(gca, 'FontSize', 16,'FontName', FontName)
%% make lines on ref positions
if ref_line == 1
    
%B1 = [11.24 18.21 32.94 33.4]; 
%B2 = [12.1 16.81];
%B3 = [15.72];
x = 1:time_frame(end);
    
P1 = [15.22 29.25 55.4];

plot([x(1) x(end)],[y(1) y(1)], 'r--','LineWidth',5);
plot([x(1) x(end)],[y(2) y(2)], 'r--','LineWidth',5);
plot([x(1) x(end)],[y(5) y(5)], 'r--','LineWidth',5);
plot([x(1) x(end)],[y(4) y(4)], 'r--','LineWidth',5);
P2 = [17.09 24.54 50.62];

plot([x(1) x(end)],[y(1) y(1)], 'g--','LineWidth',5);
plot([x(1) x(end)],[y(2) y(2)], 'g--','LineWidth',5);
P5 = [22.95 26.75];

plot([x(1) x(end)],[y(1) y(1)], 'y--','LineWidth',5);
else
end
%% grouping phases based on time
time_tol = 10;
frame_peak_start = ones (num_peak,1);
frame_peak_end = ones(num_peak,1);
phase = cell(num_peak, 1);
col=hsv(num_peak);
for j = 1:num_peak
    counter = 0;
    for k = frame_start:100
        if peak_frame(j,k) == 1  &&      counter == 0
            frame_peak_start(j) = k*time_per_frame;
            counter = 1;
        elseif peak_frame(j,k) == 0 && counter == 1
            frame_peak_end(j) = k*time_per_frame;
            counter = 2;
            break
        else
            frame_peak_start(j) = 1;
            frame_peak_end(j) = 1;
        end
        
        if counter == 1
            frame_peak_end(j) = 100;
        end
    end
end
for j = 1:num_peak
    temp_3 = find(frame_peak_end<frame_peak_end(j)+time_tol & frame_peak_end>frame_peak_end(j)-time_tol);
    trigger = 0;
    for o = 1:j
        if isequal(peak_holder(temp_3), phase{o,1})==1
            trigger=1;
        else
        end
    end
    if trigger == 0
        phase{j,1} = peak_holder(temp_3);
    else
        phase{j,1} = 0;
    end
end
idxZeros = cellfun(@(c)(isequal(c,0)), phase);
phase(idxZeros) = [];
%% plot fwhm to intensity
idx_peak = 8;
subplot(2,1,1);
plot(time_frame,width(idx_peak,:));
axis([0 inf 0.05 inf])
%xlim([0 100])
hold on
plot(time_frame(1:10:end-1),width_fitted(idx_peak,1:10:end-1),'s');
xlabel('Time(s)','FontSize',18);
ylabel('Width at Half Maximum','FontSize',18);
%hold off
subplot(2,1,2);
temp = int32((peak_holder(idx_peak)-twotheta_start)/resolution);
hold on
axis([0 inf 100 inf])
plot(time_frame,intensity(temp,:));
plot(time_frame(1:10:end-1),intensity(temp,1:10:end-1),'s');
xlabel('Time(s)','FontSize',18);
ylabel('Intensity','FontSize',18);
%xlim([0 100])
clf
%%
idx_peak_1 = 8;
idx_peak_2 = 10;
subplot(2,1,1);
temp = int32((peak_holder(idx_peak_1)-twotheta_start)/resolution);
plot(time_frame,intensity(temp,:));
axis([0 inf 100 inf])
xlabel('Time(s)','FontSize',18);
ylabel('Intensity','FontSize',18);
subplot(2,1,2);
temp = int32((peak_holder(idx_peak_2)-twotheta_start)/resolution);
plot(time_frame,intensity(temp,:));
axis([0 inf 100 inf])
xlabel('Time(s)','FontSize',18);
ylabel('Intensity','FontSize',18);
%% save data to file template
% fname_integration_temp = strcat(fname_idx,'_integration_',num2str(peak_holder(idx_peak)),'.txt');
%fileID = fopen(fname_integration_temp,'w');
    %fprintf(fileID,'%.4f\n',int_peak(idx_peak,:));
    %fclose(fileID);
    %% correct for failure points
    %for p = 10:length(domain)-10
    %    if domain(p)<50 || domain(p) >75
    %        domain(p) = (domain(p-1)+domain(p+1))/2;
    %    end
    %end
function plot_phase_groups(phase)
figure(7)
hold on
for j = 1:length(phase)
    for l = 1:size(phase,2)
        y = phase{j,1}(l);
        x = frame_peak_start(j):frame_peak_end(j);
        ref_line = plot([x(1) x(end)],[y y],'LineWidth',6,'color',col(j,:));
        ref_line.Color(4)=0.3;
    end
end
end