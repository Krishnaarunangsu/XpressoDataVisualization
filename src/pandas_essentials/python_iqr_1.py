# Some test data
import pandas as pd
import numpy as np
from scipy.stats import iqr

np.random.seed(33454)
df = (
    # A standard distribution
    pd.DataFrame({'nb': np.random.randint(0, 100, 20)})
        # Adding some outliers
        .append(pd.DataFrame({'nb': np.random.randint(100, 200, 2)}))
        # Reseting the index
        .reset_index(drop=True)
    )

# Computing IQR
Q1 = df['nb'].quantile(0.25)
print(f'Q1:{Q1}')
Q3 = df['nb'].quantile(0.75)
print(f'Q3:{Q3}')
IQR = Q3 - Q1
print(f'IQR:{IQR}')

# Filtering Values between Q1-1.5IQR and Q3+1.5IQR
filtered = df.query('(@Q1 - 1.5 * @IQR) <= nb <= (@Q3 + 1.5 * @IQR)')
# Ploting the result to check the difference
df.join(filtered, rsuffix='_filtered').boxplot()

#  https://stackoverflow.com/questions/34782063/how-to-use-pandas-filter-with-iqr

x = np.array([[10, 7, 4], [3, 2, 1]])
iqr(x, axis=0)
iqr(x, axis=1)
iqr(x, axis=1, keepdims=True)

# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.quantile.html
# http://stamfordresearch.com/outlier-removal-in-python-using-iqr-rule/
# https://www.ritchieng.com/pandas-variability/
