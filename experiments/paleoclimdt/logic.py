import pathlib
import logging
import sys

import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)

logger.addHandler(handler)

logger.debug(f'''
Python Version {sys.version}
Pandas Version {pd.__version__}
''')

def series_attr_string(*args, name: str, s: pd.Series) -> str:
    dashes = ''.join(['-' for i in range(0, len(s)+27)])
    return f'''
    {name} Series Created | Size: {s.size}
    {dashes}
    ExtArr Type: {type(s.array)} | Pandas Type: {type(s)}
    Extension Array: {s.array[:5]}
    Pandas Values: {s.values[:5]}
    '''

def generate_date_range(date_resolution: int = 2000, periods: int = 10, type: str = None):
    nanosecond = pd.date_range(str(date_resolution), periods=periods).astype('datetime64[ns]')
    second = pd.date_range(str(date_resolution), periods=periods).astype('datetime64[s]')
    if type.to_lower() == 'series':
        return(pd.Series(nanosecond), pd.Series(second))
    return(nanosecond, second)

def test_older_than_1700():
    logger.info('Running Comparisions')
    arglist = [(1500, 10, None), (1500, 10, 'Series')]
    for a in arglist: 
        try:
            ns, s = generate_date_range(a[0], a[1], type=a[2])
            logger.info(name="Nanosecond", s=ns)
            logger.info(name="Second", s=s)
        except:
            logger.error(f'''generate_date_range too far in the past. {a[0], a[2]}''')

test_older_than_1700()