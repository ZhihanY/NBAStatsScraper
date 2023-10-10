import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

def output_dataframe(func):
    '''
    -- Process input data to output a dataframe for usage
    df: DataFrame
    season: string
    directory: string

    '''
    def wrapper(*args, **kwargs):
        #out['season'] = season
        return pd.DataFrame(func(*args, **kwargs)) 
    return wrapper 

def add_worksheet(url, creds, worksheets):
    '''
    -- 

    url: string
        the URL of the Google Sheet you want to work with
    worksheets: list
        input a list of worksheet names you want to add to an exisitng Google Sheet
    '''
    gc = gspread.authorize(creds)  
    gs = gc.open_by_url(url)
    for sheet in worksheets:
        gs.add_worksheet(title=sheet, rows='2000', cols='50')  
     
def stat_parse_decorator(data):
    '''
    -- Parse the JSON format data returned from stat.nba.com
    
    data: JSON source returned from stat.nba.com 
    '''
    #def decorator(data):
        #@wraps(data)
    def processor(*args, **kwargs):
        res = data(*args, **kwargs)
        out = {}
        for item in res.get('resultSets')[0]['rowSet']:
            for index, key in enumerate(res.get('resultSets')[0]['headers']):
                if key not in out.keys():
                    out[key] = []
                else:
                    out[key].append(item[index])
        return out

    return processor


def stat_parse(data):
    '''
    -- Parse the JSON format data returned from stat.nba.com
    
    data: JSON source returned from stat.nba.com 
    '''
    out = {}
    for item in data.get('resultSets')[0]['rowSet']:
        for index, key in enumerate(data.get('resultSets')[0]['headers']):
            if key not in out.keys():
                out[key] = []
            else:
                out[key].append(item[index])
    return out

