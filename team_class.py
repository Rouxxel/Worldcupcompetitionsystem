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

# function to load a new team to the json file 
def push_data_team(team_object, file_path):
    
    if os.stat(file_path).st_size == 0:
        data_list = {'teams' : []}
    else:
        with open(file_path, encoding="utf8") as f:
            data_list = json.load(f)

    data_list['teams'].append({
                        "country": team_object.country,
                        "results": team_object.results,
                        "group_matches": team_object.group_matches, 
                        "players": team_object.players, 
                        "world_cups": team_object.world_cups})

    with open(file_path,"w", encoding="utf-8") as fw:
            #str(data_list).encode('utf-8')
            json.dump(data_list, fw, indent=4, ensure_ascii=False)
    print('Successfully appended to the JSON file in the path route :', file_path)

#load the data of all the teams of the json file, and convert to and object 
def pull_data(file_path):
    
    if os.stat(file_path).st_size == 0: 
        print('There is not data to load, please add manually')  
        team_obj = {'teams' : []}
    else:
        with open(file_path, encoding="utf8") as f:
            data = json.load(f)

        # getting  the  keys of each team 
        team_list = []
        for l in data['teams']:
            team_list.append(l['country'])

        #creating each object for each team 
        team_obj = {}
        for n in range(0, len(team_list)):
            team_obj[data['teams'][n]['country']] = TeamClass(data['teams'][n]['country'], 
                                                                data['teams'][n]['results'], 
                                                                data['teams'][n]['groupMatches'], 
                                                                data['teams'][n]['players'],
                                                                data['teams'][n]['worldCups'])
    return team_obj

#class to get the information of each object team 
class TeamClass:
    results_init  =  {'MP':0, 'W':0, 'D':0, 'L':0, 'GF':0, 'GA':0, 'GD':0, 'Pts':0}
    group_matches_init = [] #max 5 matches
    players_init = {
            "Goalkeepers": [],
            "Defenders": [],
            "Midfielders": [],
            "Forwards": []
            }
    world_cups_init = []
    
    #initialize team_object
    def __init__(self, country, results = results_init, group_matches = group_matches_init, 
                players = players_init, world_cups =  world_cups_init):
        self.country = country 
        self.results = results
        self.group_matches = group_matches
        self.players = players
        self.world_cups = world_cups 
        
    def team_info(self):
        print('Information of the team: \n')
        print('Country: ', self.country)
        print('Group Stage Results: ', self.results)
        print('List of Players: ', self.players)
        print('World Cups Won: ', self.world_cups)
        
    def print_matches(self):
        matches_to_print = []
        for pos in range(0, len(self.group_matches)):
            if self.group_matches[pos] == 1:
                matches_to_print.append('\u2705')
            elif self.group_matches[pos] == '-':
                matches_to_print.append('\u229D')
            elif self.group_matches[pos] == 0:
                matches_to_print.append('\u274c')
            else:
                None
                
        return matches_to_print                
        
    def add_win(self):
        self.results['MP']+=1
        self.results['W']+=1
        self.results['Pts']+=3
        self.group_matches.append(1)
    
    def add_draw(self):
        self.results['MP']+=1
        self.results['D']+=1
        self.results['Pts']+=1
        self.group_matches.append('-')
        
    def add_lose(self):
        self.results['MP']+=1
        self.results['L']+=1
        self.group_matches.append(0)
        
    def add_GF(self, score):
        self.results['GF'] = self.results['GF'] + score
        self.results['GD'] = self.results['GF'] - self.results['GA']
    
    def add_GA(self, score):
        self.results['GA'] = self.results['GA'] + score
        self.results['GD'] = self.results['GF'] - self.results['GA']     
