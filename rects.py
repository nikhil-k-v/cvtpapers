import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

# Fixed area for each rectangle
area = 1

# Ratios (width:height) for each rectangle
ratios = [(0.667, 6), (1, 4), (2, 2), (4, 1), (6, 0.667)]

# Calculate dimensions based on area and ratios
# Using the corrected formula for dimensions
dimensions = [(ratio[0] * math.sqrt(area / (ratio[0] * ratio[1])), ratio[1] * math.sqrt(area / (ratio[0] * ratio[1]))) for ratio in ratios]

# Find the largest width and height among the rectangles
max_width = max(width for width, height in dimensions)
max_height = max(height for width, height in dimensions)

# Create a new figure for overlapping rectangles
fig, ax = plt.subplots(figsize=(9, 9))

# Plot each rectangle starting from the same point (e.g., origin)
for i, (width, height) in enumerate(dimensions):
    # Create rectangle
    rect = patches.Rectangle((0, 0), width, height, edgecolor='black', facecolor='blue', alpha=0.5)
    ax.add_patch(rect)

    # Add label in the center of the rectangle
    ax.text(width / 2, height / 2, f'$R_{i+1}$', color='white', ha='center', va='center')

# Set the aspect of the plot to be equal
ax.set_aspect('equal', adjustable='box')

# Set limits to accommodate the largest rectangle and some additional space
ax.set_xlim(0, max_width + 0.1)
ax.set_ylim(0, max_height + 0.1)

# Remove axes for clarity
ax.axis('off')
plt.savefig('layered-rects.png', format='png', bbox_inches='tight')
plt.show()

# Initialize the x-coordinate for the starting point of the first rectangle
# Space to add between rectangles
space_between = 0.1

# Reset the x-coordinate for the starting point of the first rectangle
x_offset = 0

# Create a new figure for rectangles with space between them
fig, ax = plt.subplots(figsize=(11, 4.5))

# Plot each rectangle with a space in between
for i, (width, height) in enumerate(dimensions):
    # Create rectangle at the current x_offset
    rect = patches.Rectangle((x_offset, 0), width, height, edgecolor='black', facecolor='blue', alpha=0.5)
    ax.add_patch(rect)

    # Add label in the center of the rectangle
    ax.text(x_offset + width / 2, height / 2, f'$R_{i+1}$', color='white', ha='center', va='center')

    # Update the x_offset for the next rectangle, adding space
    x_offset += width + space_between

# Adjust the limits and aspect of the plot
ax.set_xlim(0, x_offset - space_between)  # Subtract the last added space
ax.set_ylim(0, max_height)
ax.set_aspect('auto')

# Remove axes for clarity
ax.axis('off')

plt.savefig('side-rects.png', format='png', bbox_inches='tight')
plt.show()
