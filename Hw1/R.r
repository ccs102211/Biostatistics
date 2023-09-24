# Libraries
library(ggplot2)

# Function to find outliers
find_outliers <- function(data) {
  Q1 <- quantile(data, 0.25)
  Q3 <- quantile(data, 0.75)
  IQR <- Q3 - Q1
  lower_bound <- Q1 - 1.5 * IQR
  upper_bound <- Q3 + 1.5 * IQR
  
  outliers <- data[data < lower_bound | data > upper_bound]
  return(outliers)
}

T_max_A <- c(105, 123, 12.4, 126, 108, 134, 120, 112, 130, 119, 132, 130, 133, 136, 142, 145, 156, 170, 200)

T_max_R <- c(221, 227, 280, 261, 264, 238, 250, 236, 240, 230, 246, 283, 253, 273, 516, 256, 271)

data_to_plot <- list(A = T_max_A, R = T_max_R)
df <- data.frame(values = unlist(data_to_plot), group = rep(names(data_to_plot), times=sapply(data_to_plot, length)))

print(ggplot(df, aes(x = group, y = values)) + geom_boxplot() + ggtitle("Side-by-Side boxplot of sets A and R"))

cat("Outliers of A = ", find_outliers(T_max_A), "\n")
cat("Outliers of R = ", find_outliers(T_max_R), "\n")

cat("X bar of A = ", mean(T_max_A), "\n")
cat("S square of A = ", var(T_max_A), "\n")
cat("X bar of R = ", mean(T_max_R), "\n")
cat("S square of R = ", var(T_max_R), "\n")

T_max_A[T_max_A == 12.4] <- 124

data_to_plot <- list(A = T_max_A, R = T_max_R)
df <- data.frame(values = unlist(data_to_plot), group = rep(names(data_to_plot), times=sapply(data_to_plot, length)))

print(ggplot(df, aes(x = group, y = values)) + geom_boxplot() + ggtitle("Side-by-Side boxplot of sets A and R"))

cat("Outliers of A = ", find_outliers(T_max_A), "\n")
cat("X bar of A = ", mean(T_max_A), "\n")
cat("S square of A = ", var(T_max_A), "\n")
