#from team_stats import *
#from advanced_stats import stat_parse
#from functools import wraps
import pandas as pd
import requests
from team_stats import *
from BBR_Scraper.seasons import *

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
    

def stat_parse(data):
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

@output_dataframe
@stat_parse
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

#df = get_playtype_stat('2022-23')
df = get_team_stat('2021-22')
#print(r)

