# Import Libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# This is to supress the warning messages (if any) generated in our code
import warnings
warnings.filterwarnings('ignore')

# Comment this if the data visualisations doesn't work on your side
# %matplotlib inline

# We are using whitegrid style for our seaborn plots. This is like the most basic one
sns.set_style(style='whitegrid')
# dataset = pd.read_csv('../input/train.csv')
dataset = pd.read_csv('../data/train.csv')
print(dataset.info())

n_row, n_col = dataset.shape
print(n_row, n_col)

print('****************************************************')
# Let's look at first few rows of our dataset
print(f'FIRST 3 ROWS:\n{dataset.head(3)}')

print('****************************************************')
# Create a separate dataframe which has only Categorical Variables
print(f'Categorical DataFrame Subset')
ds_cat = dataset.select_dtypes(include='object').copy()
print('****************************************************')
print(f'FIRST 3 ROWS:\n{ds_cat.head(2)}')

# Basic Stats for each variable
print('****************************************************')
print('Stats for MsZoning Column/Variable')
print('****************************************************')
print(f'Unique Values of MSZoning:\n{ds_cat["MSZoning"].unique()}')
print('****************************************************')
print(f'Total No of Unique Values:\n{len(ds_cat["MSZoning"].unique())}')

# Count of distinct categories in our variable but this time we don't want to count any nan values
print('****************************************************')
print(f'Unique Values of MSZoning:\n{ds_cat["MSZoning"].nunique()}')

# Number of Missing Values in that variable (for all the rows)
print('****************************************************')
print(f'Number of Missing Values of MSZoning Column:\n{ds_cat["MSZoning"].isnull().sum()}')


# Percentage of Missing Values in that variable
print('****************************************************')
print(f'Percentage of Missing Values in MSZoning Column:\n{ds_cat["MSZoning"].isnull().sum()/ n_row}')

# Let's multiple by 100 and keep only 1 decimal places
print('****************************************************')
print(f'Missing Values of MSZoning in Percentage Terms:\n{(ds_cat["MSZoning"].isnull().sum()/ n_row).round(3)*100}')

# Count Plot by MSZoning
sns.countplot(data = ds_cat, x = 'MSZoning')


# Since we are working on a supervised ML problem we should also look at the relationshipt
# between the dependent variable and independent variable. In order to do that let's add
# our dependent variable to this dataset.
print('****************************************************')
print('Dependent Variable/Column of the DataSet')
ds_cat['SalePrice'] = dataset.loc[ds_cat.index, 'SalePrice'].copy()
print('****************************************************')
print(f'Dependent Variable:{ds_cat["SalePrice"]}')

# Basic Statistics
print('****************************************************')
print('Basic Statistics of All Columns in Categorical Data Set')
ds_cat_stats = pd.DataFrame(columns=['column', 'values', 'values_Count_incna',
                                       'values_count_nona', 'num_miss', 'pct_miss'])
tmp = pd.DataFrame()
for col in ds_cat.columns:
    tmp['column'] = col
    tmp['values'] = [ds_cat[col].unique()]
    tmp['values_count_incna'] = len(list(ds_cat[col].unique()))
    tmp['values_count_nona'] = int(ds_cat[col].nunique())
    tmp['num_miss'] = ds_cat[col].isnull().sum()
    tmp['pct_miss'] = (ds_cat[col].isnull().sum() / len(ds_cat)).round(3) * 100
    ds_cat_stats = ds_cat_stats.append(tmp)

print('****************************************************')
print(f'Categorical Data Stats:\n{ds_cat_stats}')

print('****************************************************')
print('Statistics in Ascending sort')
# Let's do an Ascending sort on the Number of Distinct Categories for each categorical Variables
ds_cat_stats.sort_values(by='values_count_incna', inplace=True, ascending=True)

# And set the index to Column Names
ds_cat_stats.set_index('column', inplace=True)
print('****************************************************')
print(ds_cat_stats)

print('****************************************************')
print(f'First 5 rows of the Categorical Data Part of the Data Set:\n{ds_cat_stats.sort_values(by="pct_miss", ascending=False).head(5)}')

plt.show()

# https://www.kaggle.com/nextbigwhat/eda-for-categorical-variables-part-2
