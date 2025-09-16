import matplotlib.pyplot as plt
import numpy as np

# Set up the plot
fig, ax = plt.subplots(figsize=(10, 2))

# Draw the number line
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)

# Define the solution range
x_start = -2
x_end = 2
x_values = np.linspace(-4, 4, 400) # Range for the number line

# Plot the number line
ax.plot(x_values, np.zeros_like(x_values), 'k-', linewidth=1.5)

# Plot the solid points at -2 and 2
ax.plot(x_start, 0, 'ko', markersize=10, zorder=5)
ax.plot(x_end, 0, 'ko', markersize=10, zorder=5)

# Shade the solution area
ax.fill_between(x_values, 0, where=(x_values >= x_start) & (x_values <= x_end), color='skyblue', alpha=0.5)

# Add tick marks and labels
ax.set_xticks(np.arange(-4, 5, 1))
ax.set_xticklabels(np.arange(-4, 5, 1))
ax.tick_params(axis='x', direction='out', length=6, width=1)

# Add a title
ax.set_title('Solution to 10|-5x| + 5 <= 105', fontsize=16)

# Save the figure to a file
plt.savefig('solution_graph.png')

print("Graph saved as solution_graph.png")