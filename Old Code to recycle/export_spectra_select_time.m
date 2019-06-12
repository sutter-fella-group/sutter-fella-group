t =[6 10 20 50 80 800 850 900 1050 1100];
for i = 1:length(t)
    l(i) = find(time_frame==t(i));
end
    csvwrite('1.csv', [NaN ,t;(twotheta_start:resolution:twotheta_end)' ,intensity(:,l)])