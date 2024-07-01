from pyspark.sql.types import Row

def recursive_dictify(val: Row):
    if isinstance(val, Row):
        val = val.asDict()
        for (k, v) in val.items():
            val[k] = recursive_dictify(v)
    elif isinstance(val, list):
        val = [recursive_dictify(el) for el in val]
    return val