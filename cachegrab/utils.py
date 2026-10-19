import hashlib
import pickle
from copy import deepcopy

import pandas as pd
import polars as pl


def deep_copy(obj):
    '''
    Description
    ------------
    Returns deep copy of a given object. For pandas DataFrames or Series, uses
    pandas' native copy method.

    Parameters
    ------------
    obj : object
        Object to be copied.

    Returns
    ------------
    result : object
        Deep copy of object.
    '''

    if isinstance(obj, (
        pd.DataFrame,
        pd.Series,
        )):
        return obj.copy(deep=True)

    elif isinstance(obj, (
        pl.LazyFrame,
        pl.DataFrame,
        pl.Series,
        )):
        return obj.clone()

    else:
        return deepcopy(obj)


def sha256(*args):
    '''
    Description
    --------------------
    Returns sha256 hash value for any arbitrary number of arguments.

    Parameters
    --------------------
    args : tuple
        One or more arguments to hashed.

    Returns
    --------------------
    digest : str
        sha256 hash value
    '''
    payload = pickle.dumps(args)
    digest = hashlib.sha256(payload).hexdigest()
    return digest