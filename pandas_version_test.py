import pandas as pd

def pandas_version_test():
    assert pd.__version__ in ["1.5.3"]
