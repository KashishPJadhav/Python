# Customizing Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot with customization
plt.plot(x, y, color='blue', linestyle='--', linewidth=4, marker='*',markersize='15', markerfacecolor='yellow')

# Add title and labels
plt.title('Customized Line Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show plot
plt.show()
