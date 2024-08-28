# Create a bar chart
import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 5, 2, 4]

plt.title('Simple Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.bar(categories, values)

plt.show()
x= [1,2,3,4]
y= [5,10,15,20]
plt.bar(x, y)
plt.title('Bar Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.show()
