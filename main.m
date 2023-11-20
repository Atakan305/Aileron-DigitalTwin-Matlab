% Load aileron model
load_system('sm_aileron_actuator.slx');

% Start the simulation
simOut = sim('sm_aileron_actuator.slx');

% Get all Workspace data
workspaceData = evalin('base', 'whos');

% Generate a unique name
timestamp = datestr(now, 'yyyymmdd_HHMMSS');
matFileName = ['simulation_data_', 'Circuit-Averaged_', timestamp, '.mat'];

% Specify the folder where you want to save the .mat files
mat_folder = '/home/atakan/matlab-projects/aileron/mat_files/';

% Save all workspace variables into .mat file
for i = 1:length(workspaceData)
    variableName = workspaceData(i).name;
    eval([variableName ' = ' workspaceData(i).name ';']);
end

% Save the .mat file in the specified folder
save(fullfile(mat_folder, matFileName), '-regexp', '^(?!(workspaceData)$).');

% Display the final result
disp(['Saved Data to: ', fullfile(mat_folder, matFileName)]); 
