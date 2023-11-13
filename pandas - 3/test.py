import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'String_Column': ['A', 'B', 'C'],
    'Number_Column': [1, 2, 3]
})

df2 = pd.DataFrame({
    'String_Column': ['X', 'Y', 'Z'],
    'Number_Column': [4, 5, 6]
})

# Concatenate strings and sum numbers
result_df = pd.DataFrame({
    'Concatenated_Strings': df1['String_Column'] + df2['String_Column'],
    'Summed_Numbers': df1['Number_Column'] + df2['Number_Column']
})

# Display the result DataFrame
print(result_df)
