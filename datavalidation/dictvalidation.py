from typing import Dict
from pandas import Series


def validate_dict(str, data: Dict[str, Series]) -> bool:
    """
    :param str:
    :param data: dictionary
    :return: True if all dictionary items are ofватель с  the same length, and False otherwise
    """
    try:
        data_iter = iter(data.values())
        item_len = len(next(data_iter))
        while len(next(data_iter)) == item_len: ...
        return False
    except StopIteration:
        return True
