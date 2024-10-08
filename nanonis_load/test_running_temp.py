import numpy as np
from matplotlib.widgets import RangeSlider
import matplotlib.pyplot as plt
import nanonis_load.didv as didv
import nanonis_load.sxm as sxm
# Grid Experiment_30nm_along_chain_00360

map_data = np.zeros((801,41))

for i in range(127,168):
    spec = didv.spectrum('/Volumes/Data/DESKTOP-28ITBTL/D/Data/2024-08-26_BlueBronze_SameAs20230915_PtIr_77K/Bias-Spectroscopy'+str(i).zfill(5)+'.dat')
    # didv.plot(spec, channel = 'LI Demod 1 X [AVG] (A)', plot_on_previous=True, legend=False) 
    map_data[:,i-127] = spec.data['LI Demod 1 X [AVG] (A)'].values
    # LI Demod 1 X [AVG] (A)

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig00 = axs[0].imshow(np.fliplr(map_data.T), aspect='auto', cmap='viridis')

# Create a slider for adjusting the colorbar limits
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.15, 0.01, 0.3, 0.03], facecolor=axcolor)
slider = RangeSlider(ax_slider, 'Colorbar Limit', np.min(np.fliplr(map_data.T)), np.max(np.fliplr(map_data.T)), valinit=[np.min(np.fliplr(map_data.T)), np.max(np.fliplr(map_data.T))])

# Update function for the slider
def update(val):
    color_min = slider.val[0]
    color_max = slider.val[1]
    fig00.set_clim(color_min, color_max)
slider.on_changed(update)


subtraction = np.fliplr(map_data.T) - np.flipud(np.fliplr(map_data.T))
fig01 = axs[1].imshow(subtraction, aspect='auto', cmap='viridis')
# Create a slider for adjusting the colorbar limits
axcolor2 = 'lightgoldenrodyellow'
ax_slider2 = plt.axes([0.55, 0.01, 0.3, 0.03], facecolor=axcolor2)
slider2 = RangeSlider(ax_slider2, 'Colorbar Limit', np.min(subtraction), np.max(subtraction), valinit=[np.min(subtraction), np.max(subtraction)])

# Update function for the slider
def update2(val):
    color_min2 = slider2.val[0]
    color_max2 = slider2.val[1]
    fig01.set_clim(color_min2, color_max2)
slider2.on_changed(update2)

plt.show()
