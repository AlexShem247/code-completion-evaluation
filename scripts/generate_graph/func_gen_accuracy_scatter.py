import pandas as pd
import matplotlib.pyplot as plt


def plot_accuracy_from_csv(csv_path, x_column, y_column, title, save_path):
    """Generates a scatter plot from a CSV file and saves it as a PNG."""
    # Read data from CSV file
    data = pd.read_csv(csv_path)

    x = data[x_column]
    y = data[y_column]

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="blue", marker="x", s=20)

    plt.xlabel("Complexity of Function (String Length)")
    plt.ylabel("Accuracy")
    plt.title(title)

    plt.grid()
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()


plot_accuracy_from_csv(
    csv_path="../../evaluation_results/func_gen_accuracy_docstring_results.csv",
    x_column="Body Length",
    y_column="Accuracy",
    title="Functional Accuracy",
    save_path="../../evaluation_results/img/Figure_2.png"
)

plot_accuracy_from_csv(
    csv_path="../../evaluation_results/func_gen_accuracy_results.csv",
    x_column="Body Length",
    y_column="Accuracy",
    title="Functional Accuracy without Docstrings",
    save_path="../../evaluation_results/img/Figure_3.png"
)
