import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Getting CSV data
data_acc = pd.read_csv('lift_acc.csv')

# Extracting acceleration and time
noisy_data = data_acc['az (m/s^2)']
time = data_acc['time']


# Function to remove noise
def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size) / window_size, mode='valid')


# Smoothing data
win_size = 500
smoothed_data_acc = moving_average(noisy_data, win_size)
smoothed_data_time = moving_average(time, win_size)

# Offset in accelerometer
offset = 0.075

# Getting maximum magnitude acceleration upwards and downwards
acc_up_exp = max(smoothed_data_acc - offset)
acc_down_exp = abs(min(smoothed_data_acc - offset))

print(f'Acceleration of Lift Upwards (Maximum Mag): {acc_up_exp} m/s^2')
print(f'Acceleration of Lift Downwards (Maximum Mag): {acc_down_exp} m/s^2')

plt.figure(figsize=(12, 6))
# plt.plot(time, noisy_data, color='orange')
plt.plot(smoothed_data_time, smoothed_data_acc - offset, color='orange')
plt.plot(np.linspace(0, 18, 1000), [acc_up_exp]*1000, color='blue')
plt.plot(np.linspace(0, 18, 1000), [-acc_down_exp]*1000, color='blue')
plt.text(0, 0.42, '+ 0.4775 m/s^2', fontsize=13)
plt.text(0, -0.44, '- 0.4778 m/s^2', fontsize=13)
# plt.title('Acceleration of Lift Vs Time (Raw)')
plt.xlabel('Time (in sec)')
plt.ylabel('Acceleration (m/s^2)')
plt.grid()
plt.show()
