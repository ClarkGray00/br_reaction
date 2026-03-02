import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.cm as cm
import matplotlib.colors as mcolors
cmap = plt.colormaps['tab20c']


filenames = ['run5_vals_714_868_680_813','run6_vals_714_868_680_813','run7_vals_714_868_680_813']
colors = [cmap(1),cmap(12),cmap(4)]
plt.figure(figsize=(15, 10))

legend_names = ['7°C','15°C','20°C']


for i in range(len(filenames)):
    filename = filenames[i]

    if filename == '' :
        sys.exit()
    file_path = '2_datasets/' + str(filename) + '.csv'

    df = pd.read_csv(file_path)

    time_s = df['Time (s)']


    val_s = df['V']
    val_min_s = df['V_min']
    val_max_s = df['V_max']


    plt.plot(time_s, val_s, label=legend_names[i],linewidth = 2.5, color = colors[i])
    plt.fill_between(time_s, val_min_s, val_max_s, alpha=0.1, color=colors[i], edgecolor='none')




plt.axvline(30, color = 'k', linestyle = '--',alpha = 0.8)
plt.xlabel('Time Elapsed (s)', fontsize = 20,labelpad=15)
plt.ylabel('Value (a.u.)', fontsize = 20,labelpad=15)
plt.legend(fontsize = 20)
plt.xlim(0,200)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.savefig('7_figures/' + 'HSV_temp' + '_plot.png', dpi=700)


