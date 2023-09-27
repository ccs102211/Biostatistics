# Given data
mean_regular = 59.9
std_dev_regular = 10.2

mean_randomized = 44.8
std_dev_randomized = 12.7

# Compute CV for each test
CV_regular = (std_dev_regular / mean_regular) * 100
CV_randomized = (std_dev_randomized / mean_randomized) * 100

print("CV_regular = ", f'{CV_regular:.4f}')
print("CV_randomized = ", f'{CV_randomized:.4f}')
