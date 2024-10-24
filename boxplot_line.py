import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data for numWordsRemoved statistics
data = {
    'Token Size': [1, 2, 3, 4, 5, 6, 7, 9],
    'Min': [0.07775171756744385, 0.18654640197753905, 0.045608630180358885, 0.07165209293365478, 0.1233560562133789, 0.16271741867065428, 0.12496186256408691, 0.4794036102294922],
    'Max': [0.8624942779541016, 0.5860460281372071, 0.711168212890625, 0.730604019165039, 0.8889933013916016, 0.7014173889160156, 0.6318660354614258, 0.4794036102294922],
    'Median': [0.4573080635070801, 0.3750017166137695, 0.4547300720214844, 0.27021572113037107, 0.21054916381835936, 0.3449729537963867, 0.3765540504455567, 0.4794036102294922]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plotting
plt.figure(figsize=(10, 6))

# Plotting Min/Max ranges as boxes (using seaborn boxplot)
for i, row in df.iterrows():
    plt.plot([row['Token Size'], row['Token Size']], [row['Min'], row['Max']], color='lightgray', lw=10, alpha=0.7)

# Line plot for median accuracy
plt.plot(df['Token Size'], df['Median'], marker='o', color='b', label='Median Accuracy')

# Labels and Title
plt.xlabel('Number of Tokens Removed')
plt.ylabel('Accuracy')
plt.title('Accuracy of Code Prediction by Number of Tokens Removed')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
