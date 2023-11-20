import os
import glob
import scipy.io
import pandas as pd

# .mat folder
mat_folder = "/home/atakan/Master's Degree/aileron_dt_matlab/mat files"

# Choose the .mat files  
mat_files = glob.glob(os.path.join(mat_folder, 'simulation_data_*.mat'))

# Convert to CSV and save it
for mat_file in mat_files:
    # Upload the MAT file 
    mat_data = scipy.io.loadmat(mat_file)
    
    # Extract some workspace data in it
    df = pd.DataFrame(mat_data['tout'], columns=['tout'])
    
    # Save it to the CSV
    csv_file = os.path.splitext(mat_file)[0] + '.csv'
    df.to_csv(csv_file, index=False)

print('MAT Files Converted to CSV Files in:', mat_folder)
