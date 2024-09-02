import pandas as pd

# Sample data in a DataFrame
data = {
    'Year': [2019, 2020, 2021, 2022, 2023],
    'Sales': [250, 100, 180, 400, 450]
}

df = pd.DataFrame(data)

# Create a line plot using DataFrame

df.plot(x='Year', y='Sales', kind='line')

# Add title and labels

plt.title('Sales Over Years')
plt.xlabel('Year')
plt.ylabel('Sales')

# Show plot
plt.show()
