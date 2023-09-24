
#%%
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

def find_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    
    return outliers

T_max_A = np.array([105, 123, 12.4, 
           126, 108, 134,
           120, 112, 130,
           119, 132, 130,
           133, 136, 142,
           145, 156, 170,
           200])

T_max_A = pd.DataFrame(T_max_A)

T_max_R = np.array([ 221, 227, 280,
           261, 264, 238,
           250, 236, 240,
           230, 246, 283,
           253, 273, 516,
           256, 271])

T_max_R = pd.DataFrame(T_max_R)

data_to_plot = [T_max_A.values.flatten(), T_max_R.values.flatten()]

box = plt.boxplot(data_to_plot, positions=[1, 2],labels=["A", "R"])
plt.title("Side-by-Side boxplot of sets A and R")
fig = plt.figure(figsize =(10, 7))
plt.show()

print("Outliers of A = ", find_outliers(np.array(T_max_A)))
print("Outliers of R = ", find_outliers(np.array(T_max_R)))

A_mean = np.mean(np.array(T_max_A))
A_variance = np.var(np.array(T_max_A), ddof=1)

R_mean = np.mean(np.array(T_max_R))
R_variance = np.var(np.array(T_max_R), ddof=1)

print(" X bar of A = ", f'{A_mean:.4f}')
print(" S square of A = ", f'{A_variance:.4f}')
print(" X bar of R = ",  f'{R_mean:.4f}')
print(" S square of R = ", f'{R_variance:.4f}')
