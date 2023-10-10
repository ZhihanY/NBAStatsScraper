import pandas as pd
from requests import get
from bs4 import BeautifulSoup
from datetime import datetime
from unidecode import unidecode
import re


def get_box_scores(date, team1, team2, period='GAME', stat_type='BASIC'):
    """
    Get the box scores for a given game between two teams on a given date.

    Args:
        date (str): The date of the game in 'YYYY-MM-DD' format.
        team1 (str): The abbreviation of the first team.
        team2 (str): The abbreviation of the second team.
        period (str, optional): The period of the game to retrieve stats for. Defaults to 'GAME'.
        stat_type (str, optional): The type of stats to retrieve. Must be 'BASIC' or 'ADVANCED'. Defaults to 'BASIC'.

    Returns:
        dict: A dictionary containing the box scores for both teams.
    """
    if stat_type not in ['BASIC', 'ADVANCED']:
        raise ValueError('stat_type must be "BASIC" or "ADVANCED"')
    date = pd.to_datetime(date)
    #suffix = get_game_suffix(date, team1, team2)
    boxscore_url="https://www.basketball-reference.com"+suffix
    response = get(boxscore_url)
    dfs = []
    if stat_type == 'BASIC':
        table_selector_ids={
            team1:f"box-{team1}-game-basic",
            team2:f"box-{team2}-game-basic",
        }
    if stat_type == 'ADVANCED':
        table_selector_ids={
            team1:f"box-{team1}-game-advanced",
            team2:f"box-{team2}-game-advanced"
        }

    if response.status_code==200:
        for team,selector_id in table_selector_ids.items():
            soup = BeautifulSoup(response.content, 'html.parser')
            table = soup.select(f"#{selector_id}")
            raw_df = pd.read_html(str(table))[0]
            df = _process_box(raw_df)
            df['PLAYER'] = df['PLAYER'].apply(lambda name: remove_accents(name, team, date.year))
            dfs.append(df)
        return {team1: dfs[0], team2: dfs[1]}
    else:
        raise Exception(f"Response status code: {response.status_code}")
    

def _process_box(df):
    """ Perform basic processing on a box score - common to both methods

    Args:
        df (DataFrame): the raw box score df

    Returns:
        DataFrame: processed box score
    """
    df.columns = list(map(lambda x: x[1], list(df.columns)))
    df.rename(columns = {'Starters': 'PLAYER'}, inplace=True)
    if 'Tm' in df:
        df.rename(columns = {'Tm': 'TEAM'}, inplace=True)
    reserve_index = df[df['PLAYER']=='Reserves'].index[0]
    df = df.drop(reserve_index).reset_index().drop('index', axis=1) 
    return df
