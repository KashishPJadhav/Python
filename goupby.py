import pandas as pd
df = pd.DataFrame({'A': ['foo', 'bar', 'foo'], 'B': [1, 2, 3]})
grouped = df.groupby('A').sum()
print(grouped)
df.pivot_table(values='B', index='A', aggfunc='sum')