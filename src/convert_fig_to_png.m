% Specify the directory containing the .fig files
figDir = '/home/atakan/matlab-projects/aileron/fig files/';

% Specify the directory where you want to save the .png files
pngDir = '/home/atakan/matlab-projects/aileron/figures';

% Get a list of all .fig files in the specified directory
figFiles = dir(fullfile(figDir, '*.fig'));

% Loop through each .fig file and convert it to .png
for i = 1:length(figFiles)
    % Load the .fig file
    figFile = fullfile(figDir, figFiles(i).name);
    h = openfig(figFile, 'new', 'invisible');
    
    % Construct the file name for the .png file
    [~, figName, ~] = fileparts(figFiles(i).name);
    pngFile = fullfile(pngDir, [figName, '.png']);
    
    % Save the figure as a .png file
    saveas(h, pngFile, 'png');
    
    % Close the figure
    close(h);
end

disp('Conversion completed.'); 