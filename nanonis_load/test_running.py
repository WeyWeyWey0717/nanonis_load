import numpy as np
from matplotlib.widgets import RangeSlider
import matplotlib.pyplot as plt
import nanonis_load.didv as didv
import nanonis_load.sxm as sxm
# Grid Experiment_30nm_along_chain_00360

line_grid_num = 360
bias_num = didv.spectrum('/Volumes/Data/DESKTOP-28ITBTL/D/Data/2024-08-26_BlueBronze_SameAs20230915_PtIr_77K/Grid Experiment_30nm_along_chain_00001.dat').data.shape[0]
line_grid_amp = np.zeros((bias_num, line_grid_num))
x_value = np.zeros((line_grid_num))

for i in range(1,361):
    # spec = didv.spectrum('/Volumes/Data/DESKTOP-28ITBTL/D/Data/2024-08-26_BlueBronze_SameAs20230915_PtIr_77K/Bias-Spectroscopy'+str(i).zfill(5)+'.dat')
    spec = didv.spectrum('/Volumes/Data/DESKTOP-28ITBTL/D/Data/2024-08-26_BlueBronze_SameAs20230915_PtIr_77K/Grid Experiment_30nm_along_chain_'+str(i).zfill(5)+'.dat')
    # print(spec.header['X (m)'])
    # print(spec.data.shape) # (800,26)
    # print(type(spec.data)) # pd.DataFrame
    # plt.plot(spec.data.iloc[:, 0]) # Bias calc (V) and the labels
    # print(spec.data['Bias calc (V)'].values) # Bias calc (V) values

    x_value[i-1] = spec.header['X (m)']
    line_grid_amp[:,i-1] = spec.data['LI Demod 1 X [AVG] (A)'].values 
    # plt.plot(spec.data[:,0], spec.data[:,4],)

    # didv.plot(spec, channel = 'LI Demod 1 X [AVG] (A)', plot_on_previous=True, legend=False) 
    # LI Demod 1 X [AVG] (A)

# plt.show()

# Perform FFT along the x-axis (axis=1)
fft_line_grid_amp = np.fft.fftshift(np.fft.fft2(line_grid_amp), axes=1)
fft_magnitude = np.abs(fft_line_grid_amp)
fft_log_magnitude = -np.log(fft_magnitude)
fft_log_magnitude[:, 360//2] = 0

# line_grid_amp = np.log(np.abs(np.fft.fftshift(np.fft.fft2(line_grid_amp), axes=1)))
# line_grid_amp[:, 360//2] = 0

fig, axs = plt.subplots(1, 2, figsize=(10, 5))
fig01 = axs[0].imshow(line_grid_amp, aspect='auto', extent=[x_value[0], x_value[-1], min(spec.data['Bias calc (V)'].values), max(spec.data['Bias calc (V)'].values)], cmap='viridis')

fig01.set_label('Bias (V)')
# Create a colorbar
cbar = fig01.colorbar()
cbar.set_label('LI Demod 1 X [AVG] (A)')

# Create a slider for adjusting the colorbar limits
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.15, 0.01, 0.65, 0.03], facecolor=axcolor)
slider = RangeSlider(ax_slider, 'Colorbar Limit', np.min(line_grid_amp), np.max(line_grid_amp), valinit=[np.min(line_grid_amp), np.max(line_grid_amp)])

# Update function for the slider
def update(val):
    color_min = slider.val[0]
    color_max = slider.val[1]
    fig01.set_clim(color_min, color_max)
    # plt.draw()

slider.on_changed(update)

fig01 = axs[1].imshow(fft_log_magnitude, aspect='auto', extent=[x_value[0], x_value[-1], min(spec.data['Bias calc (V)'].values), max(spec.data['Bias calc (V)'].values)], cmap='viridis')



plt.show()

# print(spec.data.shape)
# specPlot1 = didv.plot(spec, channel = 'Current [AVG] (A)')  
# specPlot2 = didv.plot(spec, channel = 'Current [00002] (A)')  




# channels = ['Current [AVG] (A)', 'Current [00002] (A)', 'Current [00003] (A)']  # Add more channels as needed
# spec = didv.spectrum('/Volumes/Data/DESKTOP-28ITBTL/D/Data/2024-08-26_BlueBronze_SameAs20230915_PtIr_77K/Bias-Spectroscopy00532.dat')
# for i in range(1,300,):
#     didv.plot(spec, channel='Current ['+ str(i).zfill(5) +'] (A)', plot_on_previous=True, legend=False)
# plt.show()





# For Topography 

# imageData = sxm.sxm('/Volumes/Data/DESKTOP-28ITBTL/D/Data/2024-08-26_BlueBronze_SameAs20230915_PtIr_77K/2024-08-26_BlueBronze_SameAs20230915_PtIr_77K_0425.sxm')
# imagePlot = sxm.plot(imageData, channel = 'Z (m)')
# imagePlot.fft()
# plt.show()