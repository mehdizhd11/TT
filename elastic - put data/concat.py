import pandas as pd

# Read the two CSV files into pandas DataFrames
df1 = pd.read_csv('elastic - put data/data1.csv')
df2 = pd.read_csv('elastic - put data/data2.csv')

# Concatenate the DataFrames
concatenated_df = pd.concat([df1, df2])

# Write the concatenated DataFrame to a new CSV file
concatenated_df.to_csv('concatenated_file.csv', index=False)