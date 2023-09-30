import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from functools import wraps
from create_output import output_dataframe

def get_playtype_stat(season, playtype='Isolation', season_type='Regular Season', mode='PerGame', advance_filters={}):
    '''
    -- Retrieve player-level playtype data from stats.nba.com 
    -- Visit nba.com to understand some of the paramterers below

    playtype: string
        ex. Isolation
    season: string
        The nba season to retrieve
    season_type: string
        The type of season to retrieve, default 'Regular Season'
    mode: string 
        The aggregation method to use, ex. 'PerGame'
    '''

    headers = {
        'Connection': 'keep-alive',
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    link = 'https://stats.nba.com/stats/synergyplaytypes?LeagueID=00&PerMode=' + mode + '&PlayType=' + playtype +'&PlayerOrTeam=P&SeasonType='+ season_type +'&SeasonYear='+ season +'&TypeGrouping=offensive'
    res = requests.get(link, headers=headers).json()
    return res


def get_dashboard_stat(season, season_type='Regular Season', mode='PerGame', shot_range='', advance_filters={}):
    '''
    -- Retrieve player-level playtype data from stats.nba.com 
    -- Visit nba.com to understand some of the paramterers below

    playtype: string

    season: string
        The nba season to retrieve
    season_type: string
        The type of season to retrieve, default 'Regular Season'
    mode: string 
        The aggregation method to use, ex. 'PerGame'
    season_segment: string

    '''

    headers = {
        'Connection': 'keep-alive',
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    
    link = 'https://stats.nba.com/stats/leaguedashplayerptshot?CloseDefDistRange=&College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&DribbleRange=&GameScope=&GameSegment=&GeneralRange='+ shot_range +'&Height=&LastNGames=0&LeagueID=00&Location=&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode='+ mode +'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+ season +'&SeasonSegment=&SeasonType='+ season_type +'&ShotClockRange=&ShotDistRange=&StarterBench=&TeamID=0&TouchTimeRange=&VsConference=&VsDivision=&Weight='
    
    res = requests.get(link, headers=headers).json()
    return res


def get_tracking_stat():
    '''
    -- Retrieve player-level tracking data from stats.nba.com 
    -- Visit nba.com to understand some of the paramterers below

    playtype: string

    season: string
        The nba season to retrieve
    season_type: string
        The type of season to retrieve, default 'Regular Season'
    mode: string 
        The aggregation method to use, ex. 'PerGame'
    season_segment: string

    '''
    pass


#@output_dataframe
def stat_parse(data):
    '''
    -- Parse the JSON format data returned from stat.nba.com
    
    data: JSON source returned from stat.nba.com 
    '''
    #def decorator(data):
        #@wraps(data)
    def processor(*args, **kwargs):
        #res = data(*args, **kwargs)
        out = {}
        for item in data(*args, **kwargs).get('resultSets')[0]['rowSet']:
            for index, key in enumerate(data(*args, **kwargs).get('resultSets')[0]['headers']):
                if key not in out.keys():
                    out[key] = []
                else:
                    out[key].append(item[index])
        return out

    return processor
    