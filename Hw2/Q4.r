# Define the data
data <- matrix(c(1630, 5550, 1684, 8232), nrow = 2)
colnames(data) <- c("Men", "Women")
rownames(data) <- c("Frequent Drinker", "Not Frequent Drinker")

# Calculate probabilities
total_students <- 17096
probabilities <- data / total_students

print(probabilities)

# Define the data
data <- matrix(c(1630, 5550, 1684, 8232), nrow = 2)
colnames(data) <- c("Men", "Women")
rownames(data) <- c("Frequent Binge Drinker", "Not Frequent Binge Drinker")

# Calculate conditional probabilities
total_male <- data[1, 1] + data[2, 1]
total_female <- data[1, 2] + data[2, 2]

prob_frequent_male <- data[1, 1] / total_male
prob_not_frequent_male <- 1 - prob_frequent_male

prob_frequent_female <- data[1, 2] / total_female
prob_not_frequent_female <- 1 - prob_frequent_female

# Data for stacked barplot
male_data <- c(prob_frequent_male, prob_not_frequent_male)
female_data <- c(prob_frequent_female, prob_not_frequent_female)

old_mar <- par("mar")
par(mar = old_mar + c(0, 0, 8, 0))

# Plotting stacked barplot
barplot(cbind(male_data, female_data),
    beside = FALSE,
    col = c("blue", "green"),
    ylim = c(0, 1),
    main = "Conditional Probabilities of Drinking Behavior",
    names.arg = c("Men", "Women"),
)

legend(
    x = 0.2, y = 1.2,
    legend = c("Frequent Drinker", "Not Frequent Drinker"),
    fill = c("blue", "green"), bty = "n",
)

par(mar = old_mar)
