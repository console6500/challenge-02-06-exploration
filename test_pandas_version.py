import pandas as pd

def test_pandas_version():
    assert pd.__version__ in ["1.5.3"]
