#%%
import numpy as np

def back_to_back_stem_leaf_with_labels(data1, data2, label1, label2):
    # Convert each data point to an integer by multiplying by 10
    data1_shifted = [int(x * 10) for x in data1]
    data2_shifted = [int(x * 10) for x in data2]

    # Sort the data
    data1_sorted = sorted(data1_shifted)
    data2_sorted = sorted(data2_shifted, reverse=True)

    # Extract stems and leaves
    stems1 = [int(x / 10) for x in data1_sorted]
    leaves1 = [x % 10 for x in data1_sorted]
    
    stems2 = [int(x / 10) for x in data2_sorted]
    leaves2 = [x % 10 for x in data2_sorted]

    # Create a dictionary to store leaves for each stem
    plot_dict = {}

    for stem, leaf in zip(stems1, leaves1):
        if stem not in plot_dict:
            plot_dict[stem] = [[], []]
        plot_dict[stem][0].append(str(leaf))

    for stem, leaf in zip(stems2, leaves2):
        if stem not in plot_dict:
            plot_dict[stem] = [[], []]
        plot_dict[stem][1].append(str(leaf))

    # Determine max lengths for alignment
    max_len_left = max([len(" ".join(plot_dict[stem][1])) for stem in plot_dict])
    max_len_right = max([len(" ".join(plot_dict[stem][0])) for stem in plot_dict])

    # Print the stem-and-leaf plot
    print(f"{label1:^{max_len_left}} | Stem | {label2:^{max_len_right}}")
    print('-' * (max_len_left + max_len_right + 9))
    for stem in sorted(plot_dict.keys()):
        leaves1_str = " ".join(plot_dict[stem][0])
        leaves2_str = " ".join(plot_dict[stem][1])
        
        # Use string formatting for alignment
        print(f"  {leaves2_str[::-1]:>{max_len_left}} | {stem}. | {leaves1_str:<{max_len_right}}")

def find_Q1_median_Q3(data, name):
    Q1 = np.percentile(data, 25)
    median = np.percentile(data, 50)
    Q3 = np.percentile(data, 75)

    print("Caribaea ", name, " Q1 = ", Q1, ", median = ", median, ", Q3 = ", Q3)

Red = np.array([41.9, 42.0, 41.9, 43.1, 41.5, 41.7, 39.8, 40.6,
39.6, 42.2, 40.7, 37.9, 39.2, 37.4, 38.2, 38.1,
38.1, 38.0, 38.8, 38.2, 38.9 ,37.8, 38.0])

Yellow = np.array([36.8, 37.0, 36.5, 36.1, 36.0, 35.5, 38.1, 37.1,
35.2, 36.8, 36.7, 35.7, 36.0, 34.6, 34.6])

back_to_back_stem_leaf_with_labels(Red, Yellow, "Caribaea Yellow", "Caribaea Red")

find_Q1_median_Q3(Red, "Red")
find_Q1_median_Q3(Yellow, "Yellow")

