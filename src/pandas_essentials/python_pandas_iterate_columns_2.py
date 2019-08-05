# importing pandas as pd
import pandas as pd

# dictionary of lists
from pandas import DataFrame

dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}

# creating a dataframe from a dictionary
df = pd.DataFrame(dict)
print(df.info())

print('*****************************************************')
# iterating over rows using iterrows() function
for i, j in df.iterrows():
    print(f'DataFrame Values:\n{i, j}')
    print()
print('****************************************************')

# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'],
                'Age': [21, 19, 20, 18],
                'Stream': ['Math', 'Commerce', 'Arts', 'Biology'],
                'Percentage': [88, 92, 95, 70]}

#

# Convert the dictionary into DataFrame
df_1: DataFrame = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage'])

print(f'Data Frame-2:\n{df_1.info()}')
for i, j in df_1.iterrows():
    print(f'DataFrame Values:\n{i, j}')
    print()
