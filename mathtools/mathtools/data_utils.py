import numpy as np
import pandas as pd

def create_sample_data(n=100):
    """Generate sample dataset for testing."""
    np.random.seed(42)
    return pd.DataFrame({
        'x': np.random.normal(10, 2, n),
        'y': np.random.normal(20, 3, n),
        'category': np.random.choice(['A', 'B', 'C'], n)
    })

def basic_stats(data):
    """Calculate basic statistics."""
    if isinstance(data, pd.Series):
        return {
            'mean': data.mean(),
            'median': data.median(),
            'std': data.std(),
            'min': data.min(),
            'max': data.max()
        }
    return data.describe().to_dict()

def correlation_analysis(df, col1, col2):
    """Calculate correlation between two columns."""
    correlation = df[col1].corr(df[col2])
    return {
        'correlation': correlation,
        'strength': 'strong' if abs(correlation) > 0.7 else 'moderate' if abs(correlation) > 0.3 else 'weak'
    }

def group_summary(df, group_col, value_col):
    """Summarize data by groups."""
    return df.groupby(group_col)[value_col].agg(['mean', 'count', 'std']).round(2)
