% Load saved figures
%c=hgload('A1-30m-2s-new_fwhm_13.095.fig');
%k=hgload('A1-30m-2s-new_fwhm_28.845.fig');
%p=hgload('A1-30m-2s-new_fwhm_32.935.fig');
peaks_combine = [11.265 12.105 16.765 17.995] ;
c=hgload(['B3_110C-60m-2s_chi_35_new_fwhm_' num2str(peaks_combine(1)) '.fig']);
k=hgload(['B3_110C-60m-2s_chi_35_new_fwhm_' num2str(peaks_combine(2)) '.fig']);
p=hgload(['B3_110C-60m-2s_chi_35_new_fwhm_' num2str(peaks_combine(3)) '.fig']);

s=hgload(['B3_110C-60m-2s_chi_35_new_fwhm_' num2str(peaks_combine(4)) '.fig']);
%o=hgload('A1-30m-2s-new_fwhm_22.665.fig');
% Prepare subplots
figure
h(1)=subplot(4,1,1);
xlim([0 1500]);
ylabel('Full Width Half Max','FontSize',14)
xlabel('Time(s)','FontSize',14)
h(2)=subplot(4,1,2);
xlim([0 1500]);
ylabel('Full Width Half Max','FontSize',14)
xlabel('Time(s)','FontSize',14)

h(3)=subplot(4,1,3);
xlim([0 1500]);
ylabel('Full Width Half Max','FontSize',14)
xlabel('Time(s)','FontSize',14)


h(4)=subplot(4,1,4);
xlim([0 1500]);
ylabel('Full Width Half Max','FontSize',14)
xlabel('Time(s)','FontSize',14)
% Paste figures on the subplots
copyobj(allchild(get(c,'CurrentAxes')),h(1));
copyobj(allchild(get(k,'CurrentAxes')),h(2));
copyobj(allchild(get(p,'CurrentAxes')),h(3));
copyobj(allchild(get(s,'CurrentAxes')),h(4));
% Add legends
l(1)=legend(h(1),num2str(peaks_combine(1)));
l(2)=legend(h(2),num2str(peaks_combine(2)));
l(3)=legend(h(3),num2str(peaks_combine(3)));
l(4)=legend(h(4),num2str(peaks_combine(4)));