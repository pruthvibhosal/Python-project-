

import pandas as pd

# initialize data of lists.
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18]}

# Create DataFrame
df = pd.DataFrame(data)

print(df)

#Create an Empty DataFrame
# Importing Pandas to create DataFrame

import pandas as pd

# Creating Empty DataFrame and Storing it in variable df
df = pd.DataFrame()

print(df)

#Creating a DataFrame from Lists or Arrays

import pandas as pd

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]

# Create the pandas DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age'])

print(df)


#Create DataFrame from List of Dictionaries

import pandas as pd

# Initialize data to lists.
data = [{'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}]

# Creates DataFrame.
df = pd.DataFrame(data)

print(df)


#create a Pandas DataFrame by passing lists of dictionaries and row indexes.


import pandas as pd

# Initialize data of lists
data = [{'b': 2, 'c': 3}, {'a': 10, 'b': 20, 'c': 30}]

# Creates pandas DataFrame by passing
# Lists of dictionaries and row index.
df = pd.DataFrame(data, index=['first', 'second'])

print(df)

#Creating a DataFrame from Another DataFrame


original_df = pd.DataFrame({
    'Name': ['Tom', 'Nick', 'Krish', 'Jack'],
    'Age': [20, 21, 19, 18]
})

new_df = original_df[['Name']] 
print(new_df)



#Create DataFrame from a Dictionary of Series

import pandas as pd

# Initialize data to Dicts of series.
d = {'one': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd']),
     'two': pd.Series([10, 20, 30, 40],
                      index=['a', 'b', 'c', 'd'])}

# creates Dataframe.
df = pd.DataFrame(d)

print(df)

#Create a DataFrame by Proving the Index Label Explicitly

import pandas as pd

# initialize data of lists.
data = {'Name': ['Tom', 'Jack', 'nick', 'juli'],
        'marks': [99, 98, 95, 90]}

# Creates pandas DataFrame.
df = pd.DataFrame(data, index=['rank1',
                               'rank2',
                               'rank3',
                               'rank4'])

# print the data
print(df)

