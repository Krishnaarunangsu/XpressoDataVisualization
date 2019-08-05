import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame({
    'normal': np.random.normal(10, 3, 1000),
    'chi': np.random.chisquare(4, 1000)
})

print(df)

print(f'Head:\n{pd.cut(df["normal"], 8).head()}')
