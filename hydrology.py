import numpy as np
import matplotlib.pyplot as plt

# Monthly PET and P values
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
pet_values = [9.41, 16.74, 38.46, 70.55, 106.64, 128.50, 144.51, 133.51, 94.83, 55.22, 24.77, 11.98]
precipitation_values = [42.10, 47.93, 68.01, 93.08, 119.02, 89.25, 55.69, 44.90, 35.28, 51.34, 45.10, 40.73]

# intersections
intersections = []
for i in range(len(pet_values) - 1):
    if (pet_values[i] <= precipitation_values[i]) != (pet_values[i + 1] <= precipitation_values[i + 1]):
        intersections.append(i)


plt.figure(figsize=(12, 6))

plt.plot(months, pet_values, color='blue', linestyle='-', marker='o', label='PET')
plt.plot(months, precipitation_values, color='red', linestyle='-', marker='o', label='P')


x = np.arange(len(months))
y_pet = np.array(pet_values)
y_p = np.array(precipitation_values)


if intersections:
    idx1, idx2 = intersections[0], intersections[-1]
    plt.fill_between(x[:idx1+1], y_pet[:idx1+1], y_p[:idx1+1], color='lightblue', label='Water Surplus')
    plt.fill_between(x[idx1:idx2+1], y_pet[idx1:idx2+1], y_p[idx1:idx2+1], color='orange', label='Water Deficiency')
    plt.fill_between(x[idx2:], y_pet[idx2:], y_p[idx2:], color='lightgrey', label='Water Storage')

plt.title('Thornthwaite-Mather Water Balance')
plt.xlabel('Month')
plt.ylabel('Amount (mm)')
plt.xticks(x, months, rotation=45, ha='right')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
