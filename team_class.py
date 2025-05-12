#!/usr/bin/env python
# coding: utf-8

# How To Read The Soccer Table
# 
# - Pos – Ranking position of the teams throughout the league’s season
# - Team – the names of all the club’s participating in the league
# - MP/Pld – number of games played
# - W – the number of games won from the total number of games played
# - D – the number of games that ended in a draw from the total number of games played
# - L – the number of games that a team loss from the total number of games played
# - Pts – the total number of points a team has accumulated from games played
# - GF/GS – number of goals scored by a team after X number of games played
# - GA – number of goals a team concedes after X number of games played
# - GD - the number of goals scored and conceded by a team during a tournament. GS - GA 
# 
# How to score football points
# 
# - 3 for a win
# - 1 for a draw
# - 0 for a loss 
# 
# 
# Documentation 
# 
# - group_matches (wins = 1, draw = '-', lose = '0', not played = 'x'
# - players keys = 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'

import json
import os

def push_data_team(team_object, file_path):
    """
    Append a team object to the JSON file at `file_path`.

    Parameters:
        team_object (TeamClass): The team object to serialize and store.
        file_path (str): Path to the JSON file.
    """
    # If the file is empty, start with a basic structure
    if os.stat(file_path).st_size == 0:
        data_list = {'teams': []}
    else:
        with open(file_path, encoding="utf8") as f:
            data_list = json.load(f)

    # Append the team’s data as a dictionary
    data_list['teams'].append({
        "country": team_object.country,
        "results": team_object.results,
        "group_matches": team_object.group_matches,
        "players": team_object.players,
        "world_cups": team_object.world_cups
    })

    # Write updated data to the JSON file
    with open(file_path, "w", encoding="utf-8") as fw:
        json.dump(data_list, fw, indent=4, ensure_ascii=False)
    print('Successfully appended to the JSON file in the path route:', file_path)

def pull_data(file_path):
    """
    Load team objects from a JSON file and return them as a dictionary of TeamClass instances.

    Parameters:
        file_path (str): Path to the JSON file.

    Returns:
        dict: A dictionary mapping country names to TeamClass objects.
    """
    if os.stat(file_path).st_size == 0:
        print('There is no data to load, please add manually.')
        return {'teams': []}

    with open(file_path, encoding="utf8") as f:
        data = json.load(f)

    team_obj = {}
    for team_data in data['teams']:
        country = team_data['country']
        team_obj[country] = TeamClass(
            country,
            team_data['results'],
            team_data['groupMatches'],
            team_data['players'],
            team_data['worldCups']
        )
    return team_obj

class TeamClass:
    """
    Represents a national football team participating in a tournament.
    Stores team stats, match history, player info, and world cup history.
    """
    
    # Default initial values
    results_init = {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'GF': 0, 'GA': 0, 'GD': 0, 'Pts': 0}
    group_matches_init = []  # Max 5 matches
    players_init = {
        "Goalkeepers": [],
        "Defenders": [],
        "Midfielders": [],
        "Forwards": []
    }
    world_cups_init = []

    def __init__(self, country, results=results_init, group_matches=group_matches_init,
                players=players_init, world_cups=world_cups_init):
        """
        Initialize a team instance.

        Parameters:
            country (str): Name of the country.
            results (dict): Match results and points.
            group_matches (list): Outcomes of group stage matches.
            players (dict): Players grouped by position.
            world_cups (list): World Cup titles or years won.
        """
        self.country = country
        self.results = results
        self.group_matches = group_matches
        self.players = players
        self.world_cups = world_cups

    def team_info(self):
        """Print team details including results, players, and World Cups won."""
        print('Information of the team:\n')
        print('Country:', self.country)
        print('Group Stage Results:', self.results)
        print('List of Players:', self.players)
        print('World Cups Won:', self.world_cups)

    def print_matches(self):
        """
        Return symbols for group match results.

        Returns:
            list: Symbols representing wins (✔), draws (⊝), and losses (❌).
        """
        matches_to_print = []
        for result in self.group_matches:
            if result == 1:
                matches_to_print.append('\u2705')   # ✔
            elif result == '-':
                matches_to_print.append('\u229D')   # ⊝
            elif result == 0:
                matches_to_print.append('\u274C')   # ❌
        return matches_to_print

    def add_win(self):
        """Update results to reflect a win."""
        self.results['MP'] += 1
        self.results['W'] += 1
        self.results['Pts'] += 3
        self.group_matches.append(1)

    def add_draw(self):
        """Update results to reflect a draw."""
        self.results['MP'] += 1
        self.results['D'] += 1
        self.results['Pts'] += 1
        self.group_matches.append('-')

    def add_lose(self):
        """Update results to reflect a loss."""
        self.results['MP'] += 1
        self.results['L'] += 1
        self.group_matches.append(0)

    def add_GF(self, score):
        """
        Add goals scored to the team's stats and update goal difference.

        Parameters:
            score (int): Number of goals scored in a match.
        """
        self.results['GF'] += score
        self.results['GD'] = self.results['GF'] - self.results['GA']

    def add_GA(self, score):
        """
        Add goals against to the team's stats and update goal difference.

        Parameters:
            score (int): Number of goals conceded in a match.
        """
        self.results['GA'] += score
        self.results['GD'] = self.results['GF'] - self.results['GA']
