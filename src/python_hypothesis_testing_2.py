import pandas as pd
from scipy.stats import ttest_ind

data = {'Category': ['cat2','cat1','cat2','cat1','cat2','cat1','cat2','cat1','cat1','cat1','cat2'],
        'values': [1,2,3,1,2,3,1,2,3,5,1]}
my_data = pd.DataFrame(data)
print(f'My_Data:\n{my_data}')
print('*************************************************')
my_data_unique = my_data['Category'].unique()
print(f'My Data Unique Values:{my_data_unique}')
print('*************************************************')
my_data_mean = my_data.groupby('Category').mean()
print(f'My_Data_Mean:\n{my_data_mean}')

cat1 = my_data[my_data['Category']=='cat1']
cat2 = my_data[my_data['Category']=='cat2']

t_stat, p_value = ttest_ind(cat1['values'], cat2['values'])
print('*************************************************')
print(f'T-Statistic:{t_stat}')
print('*************************************************')
print(f'p-value:{p_value}')
if p_value < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")
