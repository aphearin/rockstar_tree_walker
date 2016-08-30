""" Module storing functions used to store a Numpy structured array on disk
as a set of binaries with standardized filenames and subdirectory locations.
"""
import os
import numpy as np


def store_structured_array(arr, parent_dirname, columns_to_save='all'):
    """ Function stores the desired columns of a structured array on disk.

    Parameters
    ----------
    arr : array
        Numpy structured array

    parent_dirname : string
        Root directory where the data should be stored

    columns_to_save : sequence of strings, optional
        List of column names that will be saved to disk. Default argument 'all'
        will store all columns.
    """
    dt = arr.dtype
    if columns_to_save == 'all':
        columns_to_save = dt.names
    for colname in columns_to_save:
        msg = "Column name ``{0}`` does not appear in input array".format(colname)
        assert colname in dt.names, msg
        output_dirname = os.path.join(parent_dirname, colname)
        try:
            os.makedirs(output_dirname)
        except OSError:
            pass
        output_fname = os.path.join(output_dirname, _column_filename(arr, colname))
        np.save(output_fname, arr[colname])


def _column_filename(arr, colname):
    """
    """
    msg = "Column name ``{0}`` does not appear in input array".format(colname)
    assert colname in arr.dtype.names, msg

    type_string = str(arr[colname].dtype.type.__name__)
    return colname + '_data_' + type_string

