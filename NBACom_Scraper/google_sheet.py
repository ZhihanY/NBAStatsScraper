import pandas as pd
import gspread
from google.auth import default
from gspread_dataframe import get_as_dataframe, set_with_dataframe

# Connect and create google sheet for data storage --example 
creds, _ = default()

def access_gsheet(url):
    '''
    --

    '''
    gc = gspread.authorize(creds)  
    gs = gc.open_by_url(url)

def add_worksheet(googlesheet, worksheets):
    '''
    -- 

    '''
    for sheet in worksheets:
        googlesheet.add_worksheet(title=sheet, rows='2000', cols='50')  