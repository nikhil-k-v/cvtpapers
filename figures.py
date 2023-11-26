import matplotlib.pyplot as plt
import numpy as np

# Define the power level we want to represent on the torque-speed curve
power_level = 1  # Power level fixed at 1 for demonstration

# Generate an array of speed values (omega), avoiding zero to prevent division by zero errors
speeds = np.linspace(0.1, 5, 400)  # Speed (omega) varies from 0.1 to 5 to decrease x bounds

# Calculate the corresponding torque values (tau) for each speed (omega) to maintain constant power
torques = power_level / speeds  # Torque (tau) is power_level / speed (omega)

# Select a point on the curve to highlight
omega_highlight = 1.2  # Example value for omega, can be changed as needed
tau_highlight = power_level / omega_highlight  # Corresponding tau value

# Plotting the torque-speed curve
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(speeds, torques, label=r'$P_m = \tau \cdot \omega$')

# Mark the point on the curve with a dot
ax.plot(omega_highlight, tau_highlight, 'ro')  # Red dot

# Draw a rectangle from the origin to the point (omega_highlight, tau_highlight) and shade it
ax.add_patch(plt.Rectangle((0, 0), omega_highlight, tau_highlight, color='blue', alpha=0.5))

# Add text inside the shaded area
plt.text(omega_highlight / 2, tau_highlight / 2, r'$P_m$',
         horizontalalignment='center', verticalalignment='center', fontsize=14)

# Setting the axis labels and title
plt.xlabel(r'$\omega$', labelpad=10)
plt.ylabel(r'$\tau$', labelpad=10)
plt.title(r'Torque-Speed Curve', pad=20)

# Removing gridlines, ticks, and tick labels
plt.grid(False)
plt.tick_params(axis='both', which='both', length=0)
plt.xticks([])  # Remove x-axis tick marks
plt.yticks([])  # Remove y-axis tick marks

# Set the limits of the axes to decrease y bounds
ax.set_xlim([0, 4])
ax.set_ylim([0, 4])  # The y limit is set to 1.2 times the max torque

# Save the figure as EPS
png_filename = 'mechpower.png'
plt.savefig(png_filename, format='png', bbox_inches='tight')

# Show the plot
plt.show()
