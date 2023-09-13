import requests
from bs4 import BeautifulSoup
import pandas as pd
#import xlrx
import time

def get_player_stat(season, season_type='Regular', mode='PerGame', season_segment=''):
    '''
    -- Retrieve player-level data from stats.nba.com 
    
    season:
    season_type:
    mode:
    season_segment:
    '''

    headers = {
        'Connection': 'keep-alive',
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    link = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=' + mode + '&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + season + '&SeasonSegment=' + season_segment + '&SeasonType=' + season_type + '%20Season&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
    
    res = requests.get(link, headers=headers).json()
    return res

def stat_parse(data):
    '''
    -- Parse the json data returned from stat.nba.com
    
    data: json source returned from stat.nba.com 
    '''
    
    out = {}
    for item in data.get('resultSets')[0]['rowSet']:
        for index, key in enumerate(data.get('resultSets')[0]['headers']):
            if key not in out.keys():
                out[key] = []
        else:
            out[key].append(item[index])
    return out