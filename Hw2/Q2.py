p_A1 = 0.4
p_A2 = 0.3
p_A3 = 0.3
p_A1_and_B = 0.1
p_A2_and_B = 0.1
p_A3_and_B = 0.2

p_B = p_A1_and_B + p_A2_and_B + p_A3_and_B
print("P(B) = P(A1 and B) + P(A2 and B) + P(A3 and B) = 0.1 + 0.1 + 0.2 = ",
      f"{p_B:.2f}")

p_B_given_A2 = p_A2_and_B / p_A2
print("P(A2|B) = P(A2 and B) / P(A2) \n=0.1 / 0.3 \n= ", f"{p_B_given_A2:.2f}")

p_leave_given_A1 = p_A1_and_B / p_A1
p_stay_given_A1 = 1 - p_leave_given_A1
print("P(stay given A1) = 1 - P(A1|B) \n= 1 - ( P(A1 and B) / P(A1)) \n=1 - (0.1 / 0.4) \n=",
      f"{p_stay_given_A1:.2f}")
