# Mathtools Package

Calculator with data science utilities for basic workflows.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/your-username/math-docs/blob/testing-exercise/mathtools/colab_demo.ipynb)

## Features

### Basic Calculator
- Addition and multiplication functions
- Command-line interface

### Data Science Utilities
- Sample data generation
- Basic statistical analysis
- Correlation analysis
- Group summaries
- Simple visualizations

## Installation
```bash
git clone https://github.com/your-username/math-docs.git
cd math-docs/mathtools
pip install -e .
```

## Quick Start
```python
import mathtools

# Create sample data
df = mathtools.create_sample_data(100)

# Analyze data
stats = mathtools.basic_stats(df['x'])
correlation = mathtools.correlation_analysis(df, 'x', 'y')

# Visualize
plot = mathtools.simple_plot(df, 'x', 'y')
```
