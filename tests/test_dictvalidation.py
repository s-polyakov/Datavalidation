import pandas as pd
import pytest

from datavalidation import validate_dict


@pytest.mark.parametrize("data, result", [
    ({}, True),
    ({'n1': pd.Series(['x1', 'x2', 'x3'])}, True),
    ({'n1': pd.Series(['x1', 'x2', 'x3']), 'n2': pd.Series(['x1', 'x2', 'x3'])}, True),
    ({'n1': pd.Series(['x1', 'x2', 'x3']), 'n2': pd.Series(['x1', 'x2'])}, False)
])
def test_dictvalidation(data, result):
    assert validate_dict('', data) == result
