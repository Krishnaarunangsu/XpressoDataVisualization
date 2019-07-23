from scipy.stats import ttest_1samp

import numpy as np
import pandas as pd

# ages = np.genfromtxt("../data/ages.csv")
ages = pd.read_csv("../data/ages.csv")
print(f'Ages:\n{ages}')
print('*************************************************')
ages_mean = np.mean(ages)
print(f'Ages Mean:\n{ages_mean}')
t_set, p_val = ttest_1samp(ages, 30)
print(f'T-Set:{t_set}')
print(f'p-values:{p_val}')
if p_val < 0.05:    # alpha value is 0.05 or 5%
   print(" we are rejecting null hypothesis")
else:
  print("we are accepting null hypothesis")
