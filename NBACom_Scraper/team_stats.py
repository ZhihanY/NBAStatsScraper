import requests
from bs4 import BeautifulSoup
from advanced_stats import stat_parse

@stat_parse
def get_team_stat(season, measure_type='Base', season_type='Regular%20Season', mode='PerGame', season_segment=''):
    '''
    -- Retrieve team-level data from stats.nba.com

    measure_type: string
        The type of player metrics to retrieve, Default Base
        [Base, Advanced, Scoring, Usage, Defense]
    season: string
        The nba season to retrieve
    season_type: string
        The type of season to retrieve, default 'Regular%20Season'
    mode: string 
        The aggregation method to use, ex. 'PerGame'
    '''
    headers = {
        'Connection': 'keep-alive',
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    link = 'https://stats.nba.com/stats/leaguedashteamstats?Conference=&DateFrom=&DateTo=&Division=&GameScope=&GameSegment=&Height=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType='+ measure_type \
        +'&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode='+ mode +'&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season='+ season +'&SeasonSegment='+ season_segment +'&SeasonType='+ season_type +'&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision='
    
    res = requests.get(link, headers=headers).json()
    return res

@stat_parse
def get_boxscores(season, season_type='Regular%20Season', season_segment=''):
    '''
    -- Retrieve team-level box scores from stats.nba.com
    -- Visit nba.com to understand some of the paramterers below

    season: string
        The nba season to retrieve
    season_type: string
        The type of season to retrieve, default 'Regular'
    season_segment: string
    '''
    headers = {
        'Connection': 'keep-alive',
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    link = 'https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=&DateTo=&Direction=DESC&ISTRound=&LeagueID=00&PlayerOrTeam=T&Season='+ season +'&SeasonType='+ season_type +'&Sorter=DATE'
    
    res = requests.get(link, headers=headers).json()
    return res

@stat_parse
def get_advanced_boxscores(season, measure_type='Base', season_type='Regular%20Season', season_segment=''):
    '''
    -- Retrieve team-level box scores from stats.nba.com
    -- Visit nba.com to understand some of the paramterers below

    season: string
        The nba season to retrieve
    season_type: string
        The type of season to retrieve, default 'Regular'
    season_segment: string
    '''
    headers = {
        'Connection': 'keep-alive',
        'Referer': 'https://www.nba.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200',
        'Accept-Encoding': 'gzip, deflate, br'
    }

    link = 'https://stats.nba.com/stats/teamgamelogs?DateFrom=&DateTo=&GameSegment=&ISTRound=&LastNGames=0&LeagueID=00&Location=&MeasureType='+ measure_type +'&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlusMinus=N&Rank=N&Season='+ season +'&SeasonSegment='+ season_segment +'&SeasonType='+ season_type +'&ShotClockRange=&VsConference=&VsDivision='
    
    res = requests.get(link, headers=headers).json()
    return res