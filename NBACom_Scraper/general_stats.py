import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_general_stat(season, measuretype='Base', season_type='Regular%20Season', mode='PerGame', season_segment='', advance_filters={}):
    '''
    -- Retrieve player-level data from stats.nba.com 
    -- Visit nba.com to understand some of the paramterers below

    measuretype: string
        The type of player metrics to retrieve, ex. Advanced; Default Base
        [Base, Advanced, Scoring, Usage, Defense]
    season: string
        The nba season to retrieve
    season_type: string
        The type of season to retrieve, default 'Regular'
    mode: string 
        The aggregation method to use, ex. 'PerGame'
    season_segment: string
        Specify the time segment of player stats to retrieve, three big segments including 'Last N Games', 'Month' and 'Season Segment' can be chosen.
        ex. 10, 'Post All-Star'
    '''

    headers = {
        'Connection': 'keep-alive',
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        'Accept-Encoding': 'gzip, deflate, br'
    }
    if season_segment != '':
        if season_segment in ['Pre All-Star', 'Post All-Star']:
            link = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=' + measuretype + '&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=' + mode + '&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + season + '&SeasonSegment=' + season_segment + '&SeasonType=' + season_type + '&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
        elif int(season_segment) in range(1, 12):
            link = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=' + measuretype + '&Month='+ season_segment +'&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=' + mode + '&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + season + '&SeasonSegment=&SeasonType=' + season_type + '&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
        else:
            pass
    else:
        link = 'https://stats.nba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=00&Location=&MeasureType=' + measuretype + '&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=' + mode + '&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=' + season + '&SeasonSegment=' + season_segment + '&SeasonType=' + season_type + '&ShotClockRange=&StarterBench=&TeamID=0&VsConference=&VsDivision=&Weight='
    
    res = requests.get(link, headers=headers).json()
    return res

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

