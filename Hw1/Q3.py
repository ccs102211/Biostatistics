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

#(a)
literacy_rates = pd.read_csv("C:\\Users\\chih-chien\\Desktop\\Biostatistics\\Hw1\\literacy_rates.csv")

plt.boxplot([literacy_rates['female'], literacy_rates['male']], 
                labels=['Female percent', 'Male percent'])
plt.title('Side-by-Side Boxplot of Female and Male Literacy Rates')
plt.ylabel('Percentage')
plt.show()

female_summary = {
        'Min': literacy_rates['female'].min(),
        'Q1': literacy_rates['female'].quantile(0.25),
        'Median': literacy_rates['female'].median(),
        'Q3': literacy_rates['female'].quantile(0.75),
        'Max': literacy_rates['female'].max()
    }

    # Calculate the 5-number summary for Male percent
male_summary = {
        'Min': literacy_rates['male'].min(),
        'Q1': literacy_rates['male'].quantile(0.25),
        'Median': literacy_rates['male'].median(),
        'Q3': literacy_rates['male'].quantile(0.75),
        'Max': literacy_rates['male'].max()
    }

print("Female : ", female_summary)
print("Male : ", male_summary)

#(b)
print("Outliers of Female = ", find_outliers(np.array(literacy_rates['female'])))
print("Outliers of Memale = ", find_outliers(np.array(literacy_rates['male'])))


#(c)
plt.figure(figsize=(12, 5))
    
# Female histogram
plt.subplot(1, 2, 1)
plt.hist(literacy_rates['female'], bins=20, color='pink', alpha=0.7)
plt.title('Female Literacy Rates Histogram')
plt.xlabel('Percentage')
plt.ylabel('Frequency')

# Male histogram
plt.subplot(1, 2, 2)
plt.hist(literacy_rates['male'], bins=20, color='blue', alpha=0.7)
plt.title('Male Literacy Rates Histogram')
plt.xlabel('Percentage')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
