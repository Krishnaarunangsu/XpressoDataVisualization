from scipy.stats import spearmanr
x = [1, 2, 3]

x_corr = [2, 4, 6]
corr, p_value = spearmanr(x, x_corr)
print(f'Correlation Coeffcient:{corr}')
print(f'P-Value:{p_value}')

x_corr = [5, 6, 5]
corr_1, p_value_1 = spearmanr(x, x_corr)
print(f'Correlation Coeffcient:{corr_1}')
print(f'P-Value:{p_value_1}')

# https://stackoverflow.com/questions/31593201/how-are-iloc-ix-and-loc-different
