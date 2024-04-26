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
# - groupMatches (wins = 1, draw = '-', lose = '0', not played = 'x'
# - players keys = 'Goalkeepers', 'Defenders', 'Midfielders', 'Forwards'

# In[1]:


import json 
import os


# In[2]:


# function to load a new team to the json file 
def pushData_team(teamObject, filepath):
    
    if os.stat(filepath).st_size == 0:
        dataList = {'teams' : []}
    else:
        with open(filepath, encoding="utf8") as f:
            dataList = json.load(f)

    dataList['teams'].append({
          "country": teamObject.country,
          "results": teamObject.results,
          "groupMatches": teamObject.groupMatches, 
          "players": teamObject.players, 
          "worldCups": teamObject.worldCups})

    with open(filepath,"w", encoding="utf-8") as fw:
            #str(dataList).encode('utf-8')
            json.dump(dataList, fw, indent=4, ensure_ascii=False)

    print('Successfully appended to the JSON file in the path rute :', filepath)


# In[3]:


#load the data of all the teams of the json file, and convert to and object 
def pullData(filepath):
    
    if os.stat(filepath).st_size == 0: 
        print('There is not data to load, please add manually')  
        teamObj = {'teams' : []}
    else:
        with open(filepath, encoding="utf8") as f:
            data = json.load(f)

        # getting  the  keys of each team 
        team_list = []
        for l in data['teams']:
            team_list.append(l['country'])

        #creating each object for each team 
        teamObj = {}
        for n in range(0, len(team_list)):
            teamObj[data['teams'][n]['country']] = Team(data['teams'][n]['country'], 
                                                            data['teams'][n]['results'], 
                                                            data['teams'][n]['groupMatches'], 
                                                            data['teams'][n]['players'],
                                                            data['teams'][n]['worldCups'])
    return teamObj
 


# In[4]:


#class to get the information of each object team 
class Team:
    results_init  =  {'MP':0, 'W':0, 'D':0, 'L':0, 'GF':0, 'GA':0, 'GD':0, 'Pts':0}
    groupMatches_init = [] #max 5 matches
    players_init = {
              "Goalkeepers": [],
              "Defenders": [],
              "Midfielders": [],
              "Forwards": []
            }
    worldCups_init = []
    
    #initialize teamObject
    def __init__(self, country, results = results_init, groupMatches = groupMatches_init, 
                 players = players_init, worldCups =  worldCups_init):
        self.country = country 
        self.results = results
        self.groupMatches = groupMatches
        self.players = players
        self.worldCups = worldCups 
        
    def info(self):
        print('Information of the team: \n')
        print('Country: ', self.country)
        print('Group Stage Results: ', self.results)
        print('List of Players: ', self.players)
        print('World Cups Won: ', self.worldCups)
        
    def printMatches(self):
        toPrint = []
        for pos in range(0, len(self.groupMatches)):
            
            if self.groupMatches[pos] == 1:
                toPrint.append('\u2705')
            elif self.groupMatches[pos] == '-':
                toPrint.append('\u229D')
            elif self.groupMatches[pos] == 0:
                toPrint.append('\u274c')
            else:
                None
                
        return toPrint                
        
    def add_Win(self):
        self.results['MP']+=1
        self.results['W']+=1
        self.results['Pts']+=3
        self.groupMatches.append(1)
    
    def add_Draw(self):
        self.results['MP']+=1
        self.results['D']+=1
        self.results['Pts']+=1
        self.groupMatches.append('-')
        
    def add_Lose(self):
        self.results['MP']+=1
        self.results['L']+=1
        self.groupMatches.append(0)
        
    def add_GF(self, score):
        self.results['GF'] = self.results['GF'] + score
        self.results['GD'] = self.results['GF'] - self.results['GA']
    
    def add_GA(self, score):
        self.results['GA'] = self.results['GA'] + score
        self.results['GD'] = self.results['GF'] - self.results['GA']     

