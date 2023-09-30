from functools import wraps
import time
import pandas as pd
from create_output import output_dataframe

data = {'a': [1,2,3], 'b':[3,4,5]}
season = '2022-23'

def test(season):
    #@wraps(func)
    def deco(func):
        def wrapper(*args, **kwargs):
            if season != None:
                out = pd.DataFrame(func(*args, **kwargs)) 
                out['season'] = season
                return out
            else:
                return None
        return wrapper 
    return deco

#@output_dataframe(season='2021-22')
@output_dataframe(season)
def cal(data):
    return data

cal(data)