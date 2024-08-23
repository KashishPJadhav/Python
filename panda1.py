import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df['A'])
print(df[df['A'] > 1])
print("C : A+B")
df['C'] = df['A'] + df['B']
print(df['C'])
