import matplotlib.pyplot as plt

# Sample data: list of tuples (x, y)
data = [(14, 1.0), (16, 1.0), (16, 1.0), (21, 0.6), (16, 0.2), (19, 0.2), (19, 1.0), (25, 0.4), (26, 0.0), (12, 0.2), (16, 1.0), (25, 1.0), (30, 1.0), (71, 0.4), (86, 0.2), (19, 0.2), (32, 1.0), (18, 0.0), (18, 1.0), (18, 0.8), (31, 0.4), (31, 0.0), (51, 1.0), (188, 0.2), (189, 0.2), (156, 0.6), (188, 0.4), (87, 0.0), (159, 0.4), (50, 0.2), (336, 0.6), (91, 0.2), (176, 0.0), (167, 0.2), (236, 0), (93, 0)]
data2 = [(14, 1.0), (16, 1.0), (16, 1.0), (21, 1.0), (16, 0.2), (19, 0.2), (19, 1.0), (25, 0.4), (26, 1.0), (12, 0.2), (16, 1.0), (25, 0.0), (30, 0), (71, 0.0), (86, 0.0), (19, 0.2), (32, 1.0), (18, 1.0), (18, 1.0), (18, 1.0), (31, 0.0), (31, 0.6), (51, 1.0), (188, 0.2), (189, 0.2), (156, 0.0), (188, 0.4), (87, 0.0), (159, 0), (50, 0.0), (336, 0.0), (91, 0.2), (176, 0.0), (167, 0), (236, 0), (93, 0)]
# Unzip the data into two lists: x and y coordinates
x, y = zip(*data2)

# Create a scatter plot
plt.scatter(x, y, color='blue', marker='x', s=20)

# Add labels and title
plt.xlabel("Complexity of function (string length)")
plt.ylabel("Accuracy")
plt.title("Functional Accuracy without Docstrings")

# Show the plot
plt.grid()  # Optional: add grid
plt.show()
