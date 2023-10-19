import matplotlib.pyplot as plt

# 資料
x_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p_values = [0.03, 0.01, 0.04, 0.3, 0.3, 0.1, 0.07, 0.15, 0, 0]

# 計算CDF
cdf_values = []
cumulative_p = 0
for p in p_values:
    cumulative_p += p
    cdf_values.append(cumulative_p)


# 繪圖
plt.step(x_values, cdf_values, where='post')
plt.xlabel('X')
plt.ylabel('Pr(X ≤ x)')
plt.title('Cumulative Distribution Function (CDF)')
plt.grid(True)
plt.xticks(x_values)
plt.yticks([i/10 for i in range(11)])
plt.ylim(0, 1.1)
plt.show()
