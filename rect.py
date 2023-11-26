import matplotlib.pyplot as plt

# Define the rectangle dimensions
tau = 1  # Length
omega = 2  # Width

# Create figure and axis
fig, ax = plt.subplots()

# Draw the rectangle, with the bottom left corner at (0,0), filled with color
rect = plt.Rectangle((0, 0), omega, tau, linewidth=0, edgecolor='none', facecolor='blue', alpha=0.5)
ax.add_patch(rect)

# Annotate the sides of the rectangle
# ax.annotate(r'$\tau$', xy=(omega/2, -0.1), xytext=(0, 0),
#             textcoords="offset points", ha='center', va='bottom', fontsize=22)
# ax.annotate(r'$\omega$', xy=(-0.1, tau/2), xytext=(0, 0),
#             textcoords="offset points", ha='right', va='center', fontsize=22, rotation=90)

# Add the text for power inside the rectangle
plt.text(omega/2, tau/2, r'$P_m = \tau \cdot \omega$', ha='center', va='center', color='white', fontsize=16)

# Add labels for tau and omega at the middle of each side

#add a arrow with flat ends on both sides of the rectangle
ax.annotate("", xy=(omega, -0.1), xytext=(0, -0.1), arrowprops=dict(arrowstyle='|-|', color='black'))
#add a arrow with flat ends on both sides of the rectangle
ax.annotate("", xy=(-0.1, tau), xytext=(-0.1, 0), arrowprops=dict(arrowstyle='|-|', color='black'))

ax.text(omega / 2, -0.2, r'$\omega$', ha='center', va='center', fontsize=16)
ax.text(-0.2, tau / 2, r'$\tau$', ha='center', va='center', rotation='vertical', fontsize=16)


# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Set the limits of the plot to just show the rectangle
ax.set_xlim(-.3, omega)
ax.set_ylim(-.3, tau)

# Turn off the axes and the frame
ax.axis('off')
ax.set_frame_on(False)

png_filename = 'rect.png'
plt.savefig(png_filename, format='png', bbox_inches='tight')

# Display the plot
plt.show()
