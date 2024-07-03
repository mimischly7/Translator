"""
This modul defines helper functions
"""

from pyspark.sql.types import Row

def recursive_dictify(val: Row):
    """
    Take pyspark :class:`DataFrame` and convert it into the corresponding Python object consistin of on of Python lists
    and dictionaries (where the leafs are str)
    """
    if isinstance(val, Row):
        val = val.asDict()
        for (k, v) in val.items():
            val[k] = recursive_dictify(v)
    elif isinstance(val, list):
        val = [recursive_dictify(el) for el in val]
    return val