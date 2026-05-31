#---pandas series from dictionery
import pandas as pd

data = {'a': 10, 'b': 20, 'c': 30}
series = pd.Series(data)

print(series)

#--pandas series from list
import pandas as pd

lst = [100, 200, 300, 400]
series = pd.Series(lst)

print(series)

#--
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s[0])      # First element
print(s[2])      # Third element
print(s[:3])     # First three elements

#---dataframe
import pandas as pd

data = [
    [1, 'John', 85],
    [2, 'Alice', 90],
    [3, 'Bob', 78]
]

df = pd.DataFrame(data, columns=['ID', 'Name', 'Marks'])

print(df)

#--
import pandas as pd

data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [20, 21, 22]
}

df = pd.DataFrame(data)

print(df)

#---
import pandas as pd

data = [
    ['John', 20],
    ['Alice', 21],
    ['Bob', 22]
]

df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)

#--
import pandas as pd

data = [
    ('John', 20),
    ('Alice', 21),
    ('Bob', 22)
]

df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)

#--
import pandas as pd

data = [
    {'Name': 'John', 'Age': 20},
    {'Name': 'Alice', 'Age': 21},
    {'Name': 'Bob', 'Age': 22}
]

df = pd.DataFrame(data)

print(df)

#--data iteration---
import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [20, 21, 22],
    'Marks': [85, 90, 78]
})

print(df)

#--
for index, row in df.iterrows():
    print(index, row['Name'], row['Marks'])

 #Using itertuples()
for row in df.itertuples():
    print(row.Name, row.Age)

#Using index
for i in df.index:
    print(df.loc[i, 'Name'])

# Selecting Rows in Pandas DataFrame Based on Conditions
result = df[df['Marks'] > 80]

print(result)


#Select Any Row from a DataFrame Using iloc[]

print(df.iloc[1])      # Second row


#Limited Rows Selection with Given Column

print(df.loc[0:1, ['Name', 'Marks']])


#Drop Rows from DataFrame Based on Certain Condition Applied on a Column
df_new = df[df['Marks'] >= 80]

print(df_new)


# Insert Row at Given Position in Pandas DataFrame
import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [20, 21, 22]
})

new_row = pd.DataFrame({
    'Name': ['David'],
    'Age': [23]
})

position = 1

df = pd.concat([df.iloc[:position],
                new_row,
                df.iloc[position:]]).reset_index(drop=True)

print(df)


#Create a List from Rows in Pandas DataFrame
import pandas as pd

df = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [20, 21, 22]
})

rows_list = df.values.tolist()

print(rows_list)

