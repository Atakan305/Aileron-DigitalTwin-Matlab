import shutil
import os
import glob

# .mat dosyasının bulunduğu klasör ve hedef klasör
mat_folder = "/home/atakan/matlab-projects/aileron/mat_files/"
output_folder = "/home/atakan/Master's Degree/aileron_dt_matlab/mat files"

# .mat dosyalarını seçin
mat_files = glob.glob(os.path.join(mat_folder, 'simulation_data_*.mat'))

# Her bir .mat dosyasını hedef klasöre kopyala
for mat_file in mat_files:
    shutil.copy(mat_file, output_folder)

print('MAT Files Copied to:', output_folder)
