import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
data = pd.read_csv("../../evaluation_results/accuracy_by_size_results.csv", encoding="latin1")
df = pd.DataFrame(data)

# Group by "Num. Words" and calculate min, median, and max for "CHRF"
result = df.groupby("Num. Words")["CHRF"].agg(["min", "median", "max"]).reset_index()

# Print the mean
sums = df.mean(numeric_only=True)
print(sums)

# Plotting
plt.figure(figsize=(10, 6))

# Plotting Min/Max ranges as boxes
for i, row in result.iterrows():  # Use 'result' instead of 'df'
    plt.plot([row["Num. Words"], row["Num. Words"]], [row["min"], row["max"]], color="lightgray", lw=10, alpha=0.7)

# Line plot for median accuracy
plt.plot(result["Num. Words"], result["median"], marker="o", color="b", label="Median CHRF")

# Labels and Title
plt.xlabel("Number of Words")
plt.ylabel("CHRF Score")
plt.title("CHRF Score by Number of Words")
plt.legend()
plt.grid(True)

# Show plot
plt.savefig("../../evaluation_results/img/Figure_1.png", dpi=300, bbox_inches="tight")  # Save the figure
plt.show()