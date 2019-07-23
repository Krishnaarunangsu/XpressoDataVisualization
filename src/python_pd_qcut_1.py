import pandas as pd
import numpy as np

print(np.array([1, 7, 5, 4, 6, 3]))
print()
pdf = pd.cut(np.array([1, 7, 5, 4, 6, 3]), 3)
print(pdf)
