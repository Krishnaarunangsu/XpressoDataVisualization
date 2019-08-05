# importing pandas as pd
import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[1, 5, 3, 4, 2],
                   "B":[3, 2, 4, 3, 4],
                   "C":[2, 2, 7, 3, 4],
                   "D":[4, 3, 6, 12, 7]})

df_1 = pd.read_csv('../../data/ages.csv')

# using quantile() function to
# find the quantiles over the index axis
qtl = df.quantile([.1, .25, .5, .75], axis = 0)
print(qtl)

qtl_1 = df_1.quantile([.1, .25, .5, .75], axis = 0)
print(qtl_1)
