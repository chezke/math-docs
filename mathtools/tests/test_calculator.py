from mathtools.calculator import add, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0

def test_add_edge_cases():
    assert add(0, 0) == 0
    assert add(-5, -3) == -8
    assert add(1.5, 2.5) == 4.0

def test_multiply_edge_cases():
    assert multiply(-2, 3) == -6
    assert multiply(2.5, 4) == 10.0

import pandas as pd
from mathtools.data_utils import create_sample_data, basic_stats

def test_sample_data_creation():
    df = create_sample_data(50)
    assert len(df) == 50
    assert list(df.columns) == ['x', 'y', 'category']

def test_basic_stats():
    data = pd.Series([1, 2, 3, 4, 5])
    stats = basic_stats(data)
    assert stats['mean'] == 3.0
    assert stats['median'] == 3.0
