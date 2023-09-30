import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

# Connect and create google sheet for data storage --example 
#creds, _ = default()

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