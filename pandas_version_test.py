import unittest
import pandas as pd

class Test(unittest.TestCase):
    def test_pandas_version():
        assert pd.__version__ in ["1.5.3"]
