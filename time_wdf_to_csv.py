import pandas as pd
import numpy as np
import sys
from renishawWiRE import WDFReader
from datetime import datetime

def print_loading_bar(action, iteration, total, bar_length=30):
    progress = iteration / total
    block = int(bar_length * progress)
    loading_bar = "▇" * block + "-" * (bar_length - block)
    progress_text = f"\r {action}: {loading_bar} ({progress * 100:.2f}%)"
    sys.stdout.write(progress_text)
    sys.stdout.flush()

# Get the filename from the user
filename = input('Please enter the .wdf filename from /2_datasets (without extension): ')
if filename == '':
    sys.exit()
file_path = f'2_datasets/{filename}.wdf'

# Read the .wdf file
reader = WDFReader(file_path)

times = reader.origin_list_header[0][4]
#print(times)
# Extract metadata and spectra
wavenumbers = reader.xdata                  # shape: (n_points,)
spectra = reader.spectra                    # shape: (n_spectra, n_points)

# Print conversion progress
num_spectra = spectra.shape[0]
for i in range(num_spectra):
    print_loading_bar("Converting .WDF -> .CSV", i + 1, num_spectra)

# Handle single acquisition case
if spectra.ndim == 1:
    # Reshape to 2D array with one row
    spectra = spectra.reshape(1, -1)
    times = [times]  # Wrap in list to match one spectrum


# Create DataFrame
df = pd.DataFrame(spectra, columns=wavenumbers)
df = df[df.columns[::-1]]  # reverse columns if needed
df.insert(0, '#Time', times)
df = df[~(df.iloc[:, 1:].eq(0).all(axis=1))]  # drop all-zero rows

# Save as CSV
csv_file_path = f'2_datasets/{filename}.csv'
df.to_csv(csv_file_path, index=False)

print('\n.WDF -> .CSV complete')
print('CSV file saved as:', csv_file_path)


