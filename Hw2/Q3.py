import pandas as pd
# Tallness Punnett Square
data_tallness = {
    ' ': ['T', 'T'],
    'T': ['TT', 'TT'],
    't': ['Tt', 'Tt']
}

df_tallness = pd.DataFrame(data_tallness)
print(df_tallness)
# Since all combinations have at least one 'T'
print("\nProbability of tall (having 'T' allele): 1.0")

# Yellowness Punnett Square
data_yellowness = {
    ' ': ['Y', 'Y'],
    'Y': ['YY', 'YY'],
    'y': ['Yy', 'Yy']
}

df_yellowness = pd.DataFrame(data_yellowness)
print(df_yellowness)
# Since all combinations have at least one 'Y'
print("\nProbability of yellow (having 'Y' allele): 1.0")

# Wrinkledness Punnett Square
data_wrinkledness = {
    ' ': ['W', 'w'],
    'W': ['WW', 'Ww'],
    'w': ['Ww', 'ww']
}

df_wrinkledness = pd.DataFrame(data_wrinkledness)
print(df_wrinkledness)
# Only one combination out of four is 'ww'
print("\nProbability of wrinkled (having 'ww' genotype): 0.25")
