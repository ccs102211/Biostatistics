# %%
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Set values
NYCU = 0.4
NTHU = 0.5
both = 0.2

# Plot Venn diagram
venn2(subsets=(NYCU, NTHU, both), set_labels=('NYCU', 'NTHU'))
plt.show()

p_neither = 1 - (NYCU + NTHU - both)
print(
    f"P(Neither) = 1 - (P(NYCU) + P(NTHU) - P(NYCU ∩ NTHU)) = {p_neither:.2f}")

# (b) Probability she gets into NTHU but not NYCU
p_only_NTHU = NTHU - both
print(f"P(NTHU ∩ not NYCU) = P(NTHU) - P(NYCU ∩ NTHU)) = {p_only_NTHU:.2f}")

# (c) Check if events are independent
independent = both == NYCU * NTHU
print("P(NYCU ∩ NTHU) == 0.2 \nP(NTHU) * P(NYCU) == 0.2 \n=>",
      f"{'Independent' if independent else 'Not independent'}")
