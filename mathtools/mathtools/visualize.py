import matplotlib.pyplot as plt

def simple_plot(data, x_col, y_col, title="Data Plot"):
    """Create a simple scatter plot."""
    plt.figure(figsize=(8, 6))
    plt.scatter(data[x_col], data[y_col], alpha=0.6)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(title)
    plt.grid(True, alpha=0.3)
    return plt

def distribution_plot(data, column, title="Distribution"):
    """Create a histogram."""
    plt.figure(figsize=(8, 6))
    plt.hist(data[column], bins=20, alpha=0.7, edgecolor='black')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    return plt
