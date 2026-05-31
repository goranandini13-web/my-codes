#Convert a Series of Date Strings to a Time Series

import pandas as pd

# Series of date strings
dates = pd.Series(['2024-01-01', '2024-02-15', '2024-03-20'])

# Convert to datetime
timeseries = pd.to_datetime(dates)

print(timeseries)

#DataFrame Merging and Joining

#Create Two DataFrames
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['John', 'Alice', 'Bob', 'David']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4, 5],
    'Marks': [85, 90, 78, 88]
})

print("DF1")
print(df1)

print("\nDF2")
print(df2)

# Perform an Inner Merge

inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print(inner_merge)

# Perform a Left Join

left_join = pd.merge(df1, df2, on='ID', how='left')
print(left_join)

#Right Join

right_join = pd.merge(df1, df2, on='ID', how='right')
print(right_join)

#Index-Based Join Using join()

df1_index = df1.set_index('ID')
df2_index = df2.set_index('ID')

joined_df = df1_index.join(df2_index, how='inner')

print(joined_df)

#Merging with Multiple Keys

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Dept': ['IT', 'HR', 'IT'],
    'Name': ['John', 'Alice', 'Bob']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Dept': ['IT', 'HR', 'Finance'],
    'Salary': [50000, 60000, 70000]
})

result = pd.merge(df1, df2, on=['ID', 'Dept'])

print(result)

#Concatenation and Merge

#Create Three DataFrames
import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['John', 'Alice']
})

df2 = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Bob', 'David']
})

df3 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Marks': [85, 90, 78, 88]
})

# Vertically Concatenate df1 and df2

combined = pd.concat([df1, df2], axis=0)

print(combined)

#Merge the Result with df3

final_df = pd.merge(combined, df3, on='ID')

print(final_df)

