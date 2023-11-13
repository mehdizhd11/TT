import pandas as pd

file_path = 'pandas - 3/dataset.csv'
df = pd.read_csv(file_path)

df1 = df.iloc[:len(df)//2, :]
df2 = df.iloc[len(df)//2:, :]

# df1
string_columns1 = df1.select_dtypes(include='object').astype(str)
numeric_columns1 = df1.select_dtypes(exclude='object')

concatenated_strings1 = string_columns1.apply(lambda x: ' '.join(x), axis=1)

summed_numbers1 = numeric_columns1.sum(axis=1)

new_df1 = pd.DataFrame({
    'Concatenated_Strings': concatenated_strings1,
    'Summed_Numbers': summed_numbers1.astype(str)  # Convert to string
})

print(new_df1)

# df2
string_columns2 = df2.select_dtypes(include='object').astype(str)
numeric_columns2 = df2.select_dtypes(exclude='object')

concatenated_strings2 = string_columns2.apply(lambda x: ' '.join(x), axis=1)

summed_numbers2 = numeric_columns2.sum(axis=1)

new_df2 = pd.DataFrame({
    'Concatenated_Strings': concatenated_strings2,
    'Summed_Numbers': summed_numbers2.astype(str)  # Convert to string
})

print(new_df2)

# Reset indices to ensure proper alignment
new_df1 = new_df1.reset_index(drop=True)
new_df2 = new_df2.reset_index(drop=True)

result_df = pd.DataFrame({
    'Concatenated_Strings': new_df1['Concatenated_Strings'] + new_df2['Concatenated_Strings'],
    'Summed_Numbers': new_df1['Summed_Numbers'] + new_df2['Summed_Numbers']
})

print(result_df)

# Separate odd and even rows
odd_rows = result_df[result_df.index % 2 != 0]
even_rows = result_df[result_df.index % 2 == 0]

# Create new DataFrames
df_odd = pd.DataFrame(odd_rows)
df_even = pd.DataFrame(even_rows)

print('New Rows ...')
print(df_odd)
print(df_even)

#csv file
df_even.to_csv('pandas - 3/even_row.csv' , index=True)
df_odd.to_csv('pandas - 3/odd_row.csv' , index=True)