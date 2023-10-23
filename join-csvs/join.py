import pandas as pd

df1 = pd.read_csv('data1.csv')
df2 = pd.read_csv('data2.csv')

result = pd.merge(df1, df2, on='name')

result.to_csv('joined_file.csv', index=False)
