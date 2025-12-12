import matplotlib.pyplot as plt
import pandas as pd
import glob

datasets = glob.glob('*.csv')
#print(datasets)
#pd.set_option('display.max_columns', 1000)
dataframe = pd.concat(map(pd.read_csv, datasets))

# Removed rows where quantity == 0
dataframe_filtered = dataframe[dataframe['quantity'] != 0]

# Saving filtered dataframe in csv
dataframe_filtered.to_csv("filtered_data.csv")

# Check if dataframe_filtered contains quantity == 0
zero_counter = 0
nonzero_counter = 0
for row in dataframe_filtered['quantity']:
   if row == 0:
       zero_counter += 1
   else:
       nonzero_counter += 1
       
print(zero_counter)
print(nonzero_counter)

# List all unique products and checking inconsistencies in naming
print(dataframe_filtered['product'].unique()) # -> there are no inconsistencies in naming

# Calculation of statistics per product
stats = (
    dataframe_filtered
    .groupby("product")["price"]
    .agg(min_price="min", max_price="max", mean_price="mean")
)

# Graphical representation of average price per product
plt.bar(stats.index, stats["mean_price"])
for i, v in enumerate(stats["mean_price"]):
    plt.text(i, v, f"{v:.2f}", ha='center', va='bottom', fontsize=9)

plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Calculation of outliners
stats["min_deviation"] = stats["min_price"] - stats["mean_price"]
stats["max_deviation"] = stats["max_price"] - stats["mean_price"]
print(stats)