# Import Libraries
import numpy as np
import pandas as pd
import seaborn as sns
# import matplotlib.pyplot as plt
# This is to supress the warning messages (if any) generated in our code
import warnings

warnings.filterwarnings('ignore')
# dataset = pd.read_csv('../input/train.csv')
dataset = pd.read_csv('../data/train2.csv')
print(f'Dataset:\n{dataset}')
print('************************************************')
print(f'Dataset Info:\n{dataset.info()}')
print('************************************************')

count_int: int = 0
count_float: int = 0
count_categorical: int = 0
type_dict = dict()
x = ''
y = ''
z = ''


def treat_int(data_set, column):
    """

    :param data_set:
    :param column:
    :return:
    """
    global count_int
    # if count_int == 0:
    # count_int = count_int+1
    count_int = count_int + 1
    # print(f'Numeric Count Int:{count_int}')
    global x
    x = dataset[column].dtype
    # print(f'Data Type in treat Int:{x}')
    # print(f'Numeric Data Set:\n{dataset[column]}')
    global type_dict
    type_dict.update({str(x): count_int})


def treat_float(data_set, column):
    """

    :param data_set:
    :param column:
    :return:
    """
    global count_float
    # if count_int == 0:
    # count_int = count_int+1
    count_float = count_float + 1
    # print(f'Float Count Int:{count_float}')
    global y
    y = dataset[column].dtype
    # print(f'Float Data Set:\n{dataset[column]}')
    global type_dict
    type_dict.update({str(y): count_float})


def treat_str(data_se, column):
    """

    :param data_se:
    :param column:
    :return:
    """
    global count_categorical
    # if count_int == 0:
    # count_int = count_int+1
    count_categorical = count_categorical + 1
    # print(f'Numeric Count Int:{count_categorical}')
    global z
    z = dataset[column].dtype
    # print(f'Categoricsl Data Set:\n{dataset[column]}')
    global type_dict
    type_dict.update({str(z): count_categorical})


# Iterate through DataSet Columns
for y in dataset.columns:
    if dataset[y].dtype == np.int64:
        treat_int(dataset[y], y)

    elif dataset[y].dtype == np.float64:
        treat_float(dataset[y], y)

    else:
        treat_str(dataset[y], y)

    # print(f'Dict:{type_dict}')

for key in type_dict:
    print('#################################################')
    print(f'Data Type:{key}')
    print('************************************************')
    print(dataset.select_dtypes(include=key).copy())
    print('************************************************')

# https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
