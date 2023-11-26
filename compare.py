import matplotlib.pyplot as plt
import numpy as np

# Define the domain
x = np.linspace(0, 5, 400)  # Avoid division by zero at omega = 0

# Define the functions
tau_optimal = 1 / x
tau_motor = 2 - x

# Create the plot
plt.figure(figsize=(6, 6))

# Plotting the curves
plt.plot(x, tau_optimal, 'r', label='Optimal Torque-Speed Curve')  # Red curve for y = 1/x
plt.plot(x, tau_motor, 'b', label="Motor's Torque-Speed Curve")   # Blue curve for y = 1 - x

# Filling the area under the curves
plt.fill_between(x, tau_optimal, color='red', alpha=0.1)
plt.fill_between(x, tau_motor, color='blue', alpha=0.1)

# Mark the intersection point
plt.plot(1, 1, 'ko')  # Black dot at (1, 1)

# Add text for the intersection point
plt.text(1, 1, '$P_{\max}$', ha='left', va='bottom', fontsize=14)


# Label the intersection points with the x and y axes
plt.plot(2, 0, 'ko')  # Black dot at (1, 1)
plt.text(2, 0, '$\omega_{\max}$', ha='left', va='bottom', fontsize=14)
plt.plot(0, 2, 'ko')  # Black dot at (1, 1)
plt.text(0, tau_motor[0], '$\\tau_{\max}$', ha='left', va='bottom', fontsize=14)


# Labeling axes
plt.xlabel('$\omega$')
plt.ylabel('$\\tau$')

# Adding the legend
plt.legend()

# ax.set_xlim([0, 5])
# ax.set_ylim([0, 5])

plt.xlim(0, 2.5)
plt.ylim(0, 2.5)
# Removing gridlines, ticks, and axis markings
plt.grid(False)
plt.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

# Display the plot
plt.savefig('ts-comparisons.png', format='png', bbox_inches='tight')
plt.show()

