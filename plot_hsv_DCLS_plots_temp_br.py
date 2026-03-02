import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm

# Use a colormap
cmap = plt.colormaps['tab20c']

# Filenames and colors
filenames = ['run1_vals_542_794_266_497','run1_hues_542_794_266_497','briggs_rauscher_run1_700c_0_5e_86p_1a_0i_DCLS']
colors = [cmap(1), cmap(10), cmap(8),cmap(5)]
legend_names = ['HSV Value','HSV Hue', 'Polyiodide DCLS','Base DCLS' ]

# Create side-by-side subplots with different width ratios
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10), gridspec_kw={'width_ratios': [3, 1],'wspace': 0.1})

# Load first dataset
filename = filenames[0]
file_path = '2_datasets/' + filename + '.csv'
df = pd.read_csv(file_path)

time_s = df['Time (s)']
val_s = df['V']
val_min_s = df['V_min']
val_max_s = df['V_max']

filename = filenames[1]
file_path = '2_datasets/' + filename + '.csv'
df = pd.read_csv(file_path)

hue_s = df['V']
hue_min_s = df['V_min']
hue_max_s = df['V_max']

# Plot main data
for ax in [ax1, ax2]:  # Apply the same plots to both axes
    ax.plot(time_s, val_s / 250, label=legend_names[0], linewidth=2.5, color=colors[0])
    ax.fill_between(time_s, val_min_s / 250, val_max_s / 250, alpha=0.1, color=colors[0], edgecolor='none')
    
    ax.plot(time_s, hue_s / 250, label=legend_names[1], linewidth=2.5, color=colors[3])
    ax.fill_between(time_s, hue_min_s / 250, hue_max_s / 250, alpha=0.1, color=colors[3], edgecolor='none')

# Load second dataset
filename = filenames[2]
file_path = '2_datasets/' + filename + '.csv'
df = pd.read_csv(file_path)

time_s = df['#Time']
product = df['penta']
product_smo = df['penta_wma']

base = df['ABC']
base_smo = df['ABC_wma']

# Plot spectral data
for ax in [ax1, ax2]:
    ax.plot(time_s, product_smo - 1, alpha=1, label=legend_names[2], linewidth=2.5, color=colors[1])
    ax.plot(time_s, product - 1, alpha=0.1, color=colors[2])
    ax.plot(time_s, base_smo - 1, alpha=1, label=legend_names[3], linewidth=2.5, color=colors[2], linestyle ='--')
    ax.plot(time_s, base - 1, alpha=0.1, color=colors[3], linestyle ='--')

#
# Customize ax1 (Main plot)
ax1.axvline(30, color='k', linestyle='--', alpha=0.8)
ax1.set_xlabel('Time Elapsed (s)', fontsize=20, labelpad=15)
ax1.set_ylabel('Value (a.u.)', fontsize=20, labelpad=15)
ax1.set_xlim(0, 600)
ax1.set_yticks([])
ax1.set_xticklabels(np.arange(0, 610, 100), fontsize=15)
ax1.legend(fontsize=15, loc='upper right',facecolor='white',framealpha=1)

# Customize ax2 (Zoomed-in plot)
ax2.set_xlim(200, 240)  # Set the zoom-in range
ax2.set_yticks([])  # Remove y-ticks to keep it clean
# Set the tick positions (every 20 units between 200 and 240)
ax2.set_xticks(np.arange(200, 241, 20))

# Set the corresponding labels for the ticks (same as the tick positions)
ax2.set_xticklabels(np.arange(200, 241, 20), fontsize=15)

# Save figures
fig.savefig('7_figures/HSV_DCLS_temp_plot_BR_color_comp.png', dpi=700)

