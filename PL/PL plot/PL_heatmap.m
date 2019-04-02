classdef PL_heatmap < matlab.apps.AppBase

    % Properties that correspond to app components
    properties (Access = public)
        UIFigure                        matlab.ui.Figure
        timeresolutionsLabel            matlab.ui.control.Label
        time_res_input                  matlab.ui.control.EditField
        StartButton                     matlab.ui.control.Button
        AxisUnitDropDownLabel           matlab.ui.control.Label
        AxisUnitDropDown                matlab.ui.control.DropDown
        color_maxEditFieldLabel         matlab.ui.control.Label
        color_max_input                 matlab.ui.control.EditField
        SelectSpectrumDirectoryButton   matlab.ui.control.Button
        SelectOutputDirectoryButton     matlab.ui.control.Button
        input_path                      matlab.ui.control.EditField
        output_path                     matlab.ui.control.EditField
        y_axisUpperLimitEditFieldLabel  matlab.ui.control.Label
        y_axisUpperLimitEditField       matlab.ui.control.EditField
        y_axisLowerLimitLabel           matlab.ui.control.Label
        y_axisLowerlimitEditField       matlab.ui.control.EditField
        NumberofyTicksEditFieldLabel    matlab.ui.control.Label
        NumberofyTicksEditField         matlab.ui.control.NumericEditField
        NumberofxTicksEditFieldLabel    matlab.ui.control.Label
        NumberofxTicksEditField         matlab.ui.control.NumericEditField
        x_axisUpperLimitEditFieldLabel  matlab.ui.control.Label
        x_axisUpperLimitEditField       matlab.ui.control.EditField
        time_limitEditFieldLabel        matlab.ui.control.Label
        time_limitEditField             matlab.ui.control.NumericEditField
        LoadParametersButton            matlab.ui.control.Button
        MaxIntensityEditFieldLabel      matlab.ui.control.Label
        MaxIntensityEditField           matlab.ui.control.NumericEditField
    end

    
    properties (Access = private)
        flag_plot_both_axes = 0; % Description
    end
    
    methods (Access = private)
        function [vRounded, digit_round] = round_to_res(~,input,roundTarget)
            k = 1;
            while roundTarget < 1
                input = input*10;
                roundTarget = roundTarget*10;
                k = k*10;
            end
            vRounded = round(input)/k;
            digit_round = log10(k);
        end    
    end

    methods (Access = private)

        % Button pushed function: StartButton
        function StartButtonPushed(app, event)
            cd(app.input_path.Value)
            filenames=dir('*.txt');
            answer = {app.time_res_input.Value,app.color_max_input.Value}; %({'time resolution for measurement (s)','color scheme max'},'Input',[1 35],{'1','max'});
            resolution_set = str2double(answer{1});
            %% gather initial time
            temp_name = strings(1,size(filenames,1));
            disp('importing');
            time = NaN(1,size(filenames,1));
            for i=1:size(filenames,1)
                miliseconds= str2double(filenames(i).name(1,end-6:end-4));
                seconds= str2double(filenames(i).name(1,end-9:end-8));
                minutes= str2double(filenames(i).name(1,end-12:end-11));
                hours= str2double(filenames(i).name(1,end-15:end-14));
                fileID = fopen(filenames(i).name(1,:),'r');
                data(i).data = textscan(fileID,'%f %f %[^\n]','HeaderLines',13,'Delimiter','\t');
                [time(1,i),~] = round_to_res(app,hours*60*60+minutes*60+seconds+miliseconds/1000,resolution_set); % milisecond is considered at this code
                fclose (fileID);
            end
            time = time - time(1);
            if length(time) ~= length(unique(time))
                [~, ind] = unique(time);
                duplicate_ind = setdiff(1:size(time, 2), ind);
                for i = 1:length(duplicate_ind)
                    if time(duplicate_ind(i)) == time(duplicate_ind(i)-1)
                        time(duplicate_ind(i)) = time(duplicate_ind(i)-1) + resolution_set/2;
                    elseif time(duplicate_ind(i)) == time(duplicate_ind(i)+1)
                        time(duplicate_ind(i)) = time(duplicate_ind(i)+1) - resolution_set/2;
                    end
                end
            end
            
            plot_range_ev = 1239.84193./data(i).data{1,1};
            %plot_range_ev = sort(plot_range_ev, 'ascend');
            plot_range_wavelength = data(i).data{1,1};
      
            intensity = NaN([size(filenames,1) size(data(1).data{1,2},1)]);
            for i =1:size(filenames,1)
                temp_name(i) = filenames(i).name;
                intensity(i,:)=data(i).data{1,2};
            end
            max_intensity = max(max(intensity));
            %% plot heatmap
            FontName = 'Arial';
            h = figure;
            mode = app.AxisUnitDropDown.Value;
            switch mode
                case 'eV'
                    contourf(time,plot_range_ev, intensity',100,'LineStyle','none');
                    ylabel('Photon Energy (eV)');
                case 'Wavelength'
                    contourf(time,plot_range_wavelength, intensity',100,'LineStyle','none');
                    ylabel('Wavelength (nm)');
                case 'both'
                    contourf(time,plot_range_ev, intensity',100,'LineStyle','none');
                    app.flag_plot_both_axes = 1;
            end
            colormap(hot(size(filenames,1)));
            xlabel('Time (s)');
            y_lim_lower = str2double(app.y_axisLowerlimitEditField.Value);
            y_lim_upper = str2double(app.y_axisUpperLimitEditField.Value);
            ylim([y_lim_lower,y_lim_upper]);
            yticks (linspace(y_lim_lower,y_lim_upper,app.NumberofyTicksEditField.Value));
            xlimit = str2double(app.x_axisUpperLimitEditField.Value);
            xlim ([0 xlimit]);
            xticks(linspace(0,xlimit,app.NumberofxTicksEditField.Value));
            set(gcf,'Position',[1 1 1536 703.2])
            title_temp = strsplit(temp_name(1),'_FLMS');
            title(title_temp{1},'FontSize',30,'FontName', FontName)
            a = get(gca,'XTickLabel');
            set(gca,'XTickLabel',a)
            a = get(gca,'YTickLabel');
            set(gca,'YTickLabel',a)
            set(gca,'box','off');
            set(gca,'TickDir','out','FontSize',30,'FontName', FontName);
            set(gca,'XMinorTick','on','YMinorTick','on')
            a1 = gca;
            a1.PlotBoxAspectRatio =([1, 3/4, 1]);
            colorbar
            l = colorbar;
            switch app.flag_plot_both_axes
                case 0
                case 1
                    l.Position = [0.8518 0.1638 0.0139 0.7213];
                    a2 = copyobj(a1,gcf);
                    set(a2,'Position',get(a1,'Position'),'xtick',[],'xlabel',[]);
                    a2.YAxisLocation = 'right';
                    a2.YLabel = a1.YLabel;
                    a1.YLabel.String = 'Photon Energy (eV)';
                    a2.YLabel.String = 'Wavelength (nm)';
                    set(a2,'YTickLabel', num2cell(sort(round((1239.84193./linspace(1.4,2,4))),'ascend')));
            end
            
            if isequal(answer{2},'max')
                caxis([0 max_intensity]);
            else
                caxis([0 str2double(answer(2))]);
            end
            cd (app.output_path.Value)
            saveas(gcf,[title_temp{1} '.jpg'],'jpg');
            %% printing the maximum value
            %fprintf('The maximum intensity is : %d.\n',max_intensity);
        end

        % Button pushed function: SelectOutputDirectoryButton
        function SelectOutputDirectoryButtonPushed(app, event)
            global selpath_output
            selpath_output = uigetdir(pwd,'Output');
            app.output_path.Value = selpath_output;
        end

        % Button pushed function: SelectSpectrumDirectoryButton
        function SelectSpectrumDirectoryButtonPushed(app, event)
            global selpath
            selpath = uigetdir(pwd,'Data Folder'); % set output folder
            app.input_path.Value = selpath;
        end

        % Button pushed function: LoadParametersButton
        function LoadParametersButtonPushed(app, event)
            cd(app.input_path.Value)
            filenames=dir('*.txt');
            answer = {app.time_res_input.Value,app.color_max_input.Value}; %({'time resolution for measurement (s)','color scheme max'},'Input',[1 35],{'1','max'});
            resolution_set = str2double(answer{1});
            %% gather initial time
            temp_name = strings(1,size(filenames,1));
            time = NaN(1,size(filenames,1));
            for i=1:size(filenames,1)
                miliseconds= str2double(filenames(i).name(1,end-6:end-4));
                seconds= str2double(filenames(i).name(1,end-9:end-8));
                minutes= str2double(filenames(i).name(1,end-12:end-11));
                hours= str2double(filenames(i).name(1,end-15:end-14));
                fileID = fopen(filenames(i).name(1,:),'r');
                data(i).data = textscan(fileID,'%f %f %[^\n]','HeaderLines',13,'Delimiter','\t');
                [time(1,i),~] = round_to_res(app,hours*60*60+minutes*60+seconds+miliseconds/1000,resolution_set); % milisecond is considered at this code
                fclose (fileID);
            end
            intensity = NaN([size(filenames,1) size(data(1).data{1,2},1)]);
            for i =1:size(filenames,1)
                temp_name(i) = filenames(i).name;
                intensity(i,:)=data(i).data{1,2};
            end
            max_intensity = max(max(intensity));
            app.MaxIntensityEditField.Value = max_intensity;
            app.time_limitEditField.Value = time(end)-time(1);
            app.x_axisUpperLimitEditField.Value = num2str(round(time(end)-time(1)));
        end
    end

    % App initialization and construction
    methods (Access = private)

        % Create UIFigure and components
        function createComponents(app)

            % Create UIFigure
            app.UIFigure = uifigure;
            app.UIFigure.Position = [100 100 640 480];
            app.UIFigure.Name = 'Heatmap App';

            % Create timeresolutionsLabel
            app.timeresolutionsLabel = uilabel(app.UIFigure);
            app.timeresolutionsLabel.HorizontalAlignment = 'right';
            app.timeresolutionsLabel.Position = [282 309 101 22];
            app.timeresolutionsLabel.Text = 'time resolution (s)';

            % Create time_res_input
            app.time_res_input = uieditfield(app.UIFigure, 'text');
            app.time_res_input.Position = [398 309 100 22];
            app.time_res_input.Value = '0.01';

            % Create StartButton
            app.StartButton = uibutton(app.UIFigure, 'push');
            app.StartButton.ButtonPushedFcn = createCallbackFcn(app, @StartButtonPushed, true);
            app.StartButton.Position = [532 14 100 22];
            app.StartButton.Text = 'Start';

            % Create AxisUnitDropDownLabel
            app.AxisUnitDropDownLabel = uilabel(app.UIFigure);
            app.AxisUnitDropDownLabel.HorizontalAlignment = 'right';
            app.AxisUnitDropDownLabel.Position = [53 429 53 22];
            app.AxisUnitDropDownLabel.Text = 'Axis Unit';

            % Create AxisUnitDropDown
            app.AxisUnitDropDown = uidropdown(app.UIFigure);
            app.AxisUnitDropDown.Items = {'Wavelength', 'eV', 'both'};
            app.AxisUnitDropDown.Position = [121 429 100 22];
            app.AxisUnitDropDown.Value = 'Wavelength';

            % Create color_maxEditFieldLabel
            app.color_maxEditFieldLabel = uilabel(app.UIFigure);
            app.color_maxEditFieldLabel.HorizontalAlignment = 'right';
            app.color_maxEditFieldLabel.Position = [322 347 61 22];
            app.color_maxEditFieldLabel.Text = 'color_max';

            % Create color_max_input
            app.color_max_input = uieditfield(app.UIFigure, 'text');
            app.color_max_input.Position = [398 347 100 22];
            app.color_max_input.Value = 'max';

            % Create SelectSpectrumDirectoryButton
            app.SelectSpectrumDirectoryButton = uibutton(app.UIFigure, 'push');
            app.SelectSpectrumDirectoryButton.ButtonPushedFcn = createCallbackFcn(app, @SelectSpectrumDirectoryButtonPushed, true);
            app.SelectSpectrumDirectoryButton.Position = [262 429 155 22];
            app.SelectSpectrumDirectoryButton.Text = 'Select Spectrum Directory';

            % Create SelectOutputDirectoryButton
            app.SelectOutputDirectoryButton = uibutton(app.UIFigure, 'push');
            app.SelectOutputDirectoryButton.ButtonPushedFcn = createCallbackFcn(app, @SelectOutputDirectoryButtonPushed, true);
            app.SelectOutputDirectoryButton.Position = [262 390 140 22];
            app.SelectOutputDirectoryButton.Text = 'Select Output Directory';

            % Create output_path
            app.output_path = uieditfield(app.UIFigure, 'text');
            app.output_path.Position = [434 390 184 22];

            % Create input_path
            app.input_path = uieditfield(app.UIFigure, 'text');
            app.input_path.Position = [434 429 184 22];

            % Create y_axisUpperLimitEditFieldLabel
            app.y_axisUpperLimitEditFieldLabel = uilabel(app.UIFigure);
            app.y_axisUpperLimitEditFieldLabel.HorizontalAlignment = 'right';
            app.y_axisUpperLimitEditFieldLabel.Position = [2 390 104 22];
            app.y_axisUpperLimitEditFieldLabel.Text = 'y_axis Upper Limit';

            % Create y_axisUpperLimitEditField
            app.y_axisUpperLimitEditField = uieditfield(app.UIFigure, 'text');
            app.y_axisUpperLimitEditField.Position = [121 390 100 22];
            app.y_axisUpperLimitEditField.Value = '700';

            % Create y_axisLowerLimitLabel
            app.y_axisLowerLimitLabel = uilabel(app.UIFigure);
            app.y_axisLowerLimitLabel.HorizontalAlignment = 'right';
            app.y_axisLowerLimitLabel.Position = [2 352 104 22];
            app.y_axisLowerLimitLabel.Text = 'y_axis Lower Limit';

            % Create y_axisLowerlimitEditField
            app.y_axisLowerlimitEditField = uieditfield(app.UIFigure, 'text');
            app.y_axisLowerlimitEditField.Position = [121 352 100 22];
            app.y_axisLowerlimitEditField.Value = '300';

            % Create NumberofyTicksEditFieldLabel
            app.NumberofyTicksEditFieldLabel = uilabel(app.UIFigure);
            app.NumberofyTicksEditFieldLabel.HorizontalAlignment = 'right';
            app.NumberofyTicksEditFieldLabel.Position = [4 317 102 22];
            app.NumberofyTicksEditFieldLabel.Text = 'Number of y Ticks';

            % Create NumberofyTicksEditField
            app.NumberofyTicksEditField = uieditfield(app.UIFigure, 'numeric');
            app.NumberofyTicksEditField.Position = [121 317 100 22];
            app.NumberofyTicksEditField.Value = 4;

            % Create NumberofxTicksEditFieldLabel
            app.NumberofxTicksEditFieldLabel = uilabel(app.UIFigure);
            app.NumberofxTicksEditFieldLabel.HorizontalAlignment = 'right';
            app.NumberofxTicksEditFieldLabel.Position = [4 238 102 22];
            app.NumberofxTicksEditFieldLabel.Text = 'Number of x Ticks';

            % Create NumberofxTicksEditField
            app.NumberofxTicksEditField = uieditfield(app.UIFigure, 'numeric');
            app.NumberofxTicksEditField.Position = [121 238 100 22];
            app.NumberofxTicksEditField.Value = 6;

            % Create x_axisUpperLimitEditFieldLabel
            app.x_axisUpperLimitEditFieldLabel = uilabel(app.UIFigure);
            app.x_axisUpperLimitEditFieldLabel.HorizontalAlignment = 'right';
            app.x_axisUpperLimitEditFieldLabel.Position = [2 277 104 22];
            app.x_axisUpperLimitEditFieldLabel.Text = 'x_axis Upper Limit';

            % Create x_axisUpperLimitEditField
            app.x_axisUpperLimitEditField = uieditfield(app.UIFigure, 'text');
            app.x_axisUpperLimitEditField.Position = [121 277 100 22];
            app.x_axisUpperLimitEditField.Value = '10';

            % Create time_limitEditFieldLabel
            app.time_limitEditFieldLabel = uilabel(app.UIFigure);
            app.time_limitEditFieldLabel.HorizontalAlignment = 'right';
            app.time_limitEditFieldLabel.Position = [327 150 56 22];
            app.time_limitEditFieldLabel.Text = 'time_limit';

            % Create time_limitEditField
            app.time_limitEditField = uieditfield(app.UIFigure, 'numeric');
            app.time_limitEditField.Editable = 'off';
            app.time_limitEditField.Position = [398 150 100 22];

            % Create LoadParametersButton
            app.LoadParametersButton = uibutton(app.UIFigure, 'push');
            app.LoadParametersButton.ButtonPushedFcn = createCallbackFcn(app, @LoadParametersButtonPushed, true);
            app.LoadParametersButton.Position = [510 150 108 22];
            app.LoadParametersButton.Text = 'Load Parameters';

            % Create MaxIntensityEditFieldLabel
            app.MaxIntensityEditFieldLabel = uilabel(app.UIFigure);
            app.MaxIntensityEditFieldLabel.HorizontalAlignment = 'right';
            app.MaxIntensityEditFieldLabel.Position = [307 119 76 22];
            app.MaxIntensityEditFieldLabel.Text = 'Max Intensity';

            % Create MaxIntensityEditField
            app.MaxIntensityEditField = uieditfield(app.UIFigure, 'numeric');
            app.MaxIntensityEditField.Editable = 'off';
            app.MaxIntensityEditField.Position = [398 119 100 22];
        end
    end

    methods (Access = public)

        % Construct app
        function app = app_for_heatmap_plot

            % Create and configure components
            createComponents(app)

            % Register the app with App Designer
            registerApp(app, app.UIFigure)

            if nargout == 0
                clear app
            end
        end

        % Code that executes before app deletion
        function delete(app)

            % Delete UIFigure when app is deleted
            delete(app.UIFigure)
        end
    end
end