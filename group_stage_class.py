#!/usr/bin/env python
# coding: utf-8

import random
from TeamClass import *

class GroupStage:
    #group structure <<dict of group with teamObjects>> key=group_name : value= {key=country: value=teamObject } 
    group_stage_dict = {
            'GroupA' : [], 
            'GroupB' : [], 
            'GroupC' : [], 
            'GroupD' : [], 
            'GroupE' : [], 
            'GroupF' : [], 
            'GroupG' : [], 
            'GroupH' : []}
    team_data = {}

    def __init__(self, group = group_stage_dict, team_list = team_data):
        self.group = group             # <<dict of group with teamObjects>> key=group_name : value= {key=country: value=teamObject } 
        self.team_list = team_list     # <<dict of objects>> key=country : value=teamObject 
        
    #print the table results of the group stage 
    def print_group_stage(self):
        
        validation = [1 if len(self.group[each]) == 0 else 0 for each in self.group] #checking if there is a empty list
        if validation.count(1) == 8:
            print('There is not table to show, or there is a missing value. /n Please call the function objectName.create_groups')                
        else:
            print('Group Stage Table \n')

            for each in self.group:
                print(f'\n {each}: \n ')
                print('\t\t MP, W, D, L, GF, GA, GD, Pts \t Last 3')
                
                names = list(self.group[each].keys())
                scores = list(self.group[each].values())
    
                for n in range(0,4):
                    matches = self.group[each][names[n]].printMatches()
                    #printing table 
                    print(f'{names[n]} : \t{list(self.group[each][names[n]].results.values())} \t {matches[0]} {matches[1]} {matches[2]}')
            
    #create the groups by manual input and store in a json file with the route file_path 
    def create_groups(self, file_path):

        list_of_teams = {}
        for each in self.group:

            print(f'Please insert the teams of {each}:')
            for _ in range(1,5):
                print(f'Insert the name of the team {_}/{4}: ')
                team_name = input('').capitalize()
                list_of_teams[team_name] = Team(team_name) #create the team object and store in a dict 
                self.team_list[team_name] = Team(team_name) 

            self.group[each] = list_of_teams #insert the dict of 4 teams in the key for each group 
            list_of_teams = {}

        for each in self.team_list:
            pushData_team(self.team_list[each], file_path) #store the data in json file <<dict of objects>> key=country value=teamObject 
    
    #create random groups giving a <<dict of objects>> key=country : value=teamObject 
    def random_Groups(self, data_teams):        

        names = list(data_teams.keys()) #getting the names of each team
        random.shuffle(names) #shuffle the teams 
        counter = 0
        each_group = {}
        for each in self.group:
            while counter < 32:
                #insert each teamObject in each group of 4
                each_group[names[counter]] = data_teams[names[counter]]
                self.team_list[names[counter]] = data_teams[names[counter]]
                counter+=1
                if counter % 4 == 0:
                    self.group[each] = each_group
                    each_group = {}
                    break

    #create groups using existing data getting this data from a <<dict of objects>> key=country : value=teamObject                                 
    def load_data(self, data_teams):
        names = list(data_teams.keys())
        counter = 0
        each_group = {}
        for each in self.group:
            while counter < 32:
                each_group[names[counter]] = data_teams[names[counter]]
                self.team_list[names[counter]] = data_teams[names[counter]]
                counter+=1
                if counter % 4 == 0:
                    self.group[each] = each_group
                    each_group = {}
                    break
    
    #method that allow save the data of all the groups in a json file 
    #group_teams = <<dict of group with teamObjects>> key=group_name : value= {key=country: value=teamObject } 
    #file_path = address where is located the clean file 
    def saving_data(self, group_teams, file_path):
        for group in list(group_teams.keys()):
            for each in list(group_teams[group].keys()):
                pushData_team(group_teams[group][each], file_path)
    
    #method that allow user input each match or do it randomly 
    #group_teams = <<dict of group with teamObjects>> key=group_name : value= {key=country: value=teamObject } 
    #option : 'random' to add random scores, default as None  
    def add_scores(self, group_teams, option): #function to play 3 games max on each team 
        
        game = 1
        match_order  = [[0,1,2,3],[0,2,1,3],[0,3,1,2]] #secuence to play just 2 teams from each 2 groups by day. 
        order = 0
        while order < 3: #play 3 rounds each team 
            position = 0
            for each in group_teams: #getting the data of <<dict of group with teamObjects>>
                print('\n', each)
                name_list = list(group_teams[each].keys()) #getting the Country 4 names of each Group ['name1', 'name2', 'name3', 'name4']
                while position < 4:
                    pos = match_order[order][position] #getting the position on the list order 
                    pos2 = match_order[order][position+1]
                    team_1 = group_teams[each][name_list[pos]] #getting the team object 
                    team2 = group_teams[each][name_list[pos2]]
                    flag = True
                    while flag:
                        print(f'Please insert the scores of game {game}:\n  ')
                        print(f'{team_1.country} vs {team2.country} \n')
                        #if user input random, create random scores 
                        if option == 'random':
                            score_team_1 = random.randint(0, 8) #random score values 
                            score_team2 = random.randint(0, 8)
                            print(f'{score_team_1} - {score_team2}')
                            flag = False #close loop validation 
                        else:
                            print(f'{team_1.country}: ')
                            score_team_1  = input()
                            print(f'{team2.country}: ')
                            score_team2  = input()
                            
                            #make sure the input is numeric 
                            if score_team_1.isnumeric() == False or score_team2.isnumeric() == False:
                                print('\033[1m \033[91m' + 'You enter a wrong input, just number are accepted' + '\033[0m')
                            else:
                                #make sure the input is int 
                                score_team_1 = int(score_team_1)
                                score_team2 = int(score_team2)
                                flag = False #close loop validation 
                    
                    #adding each score to the result attributes of each team calling the methods of the teamClass 
                    team_1.add_GF(score_team_1)
                    team_1.add_GA(score_team2)
                    team2.add_GF(score_team2)
                    team2.add_GA(score_team_1)

                    if score_team_1 == score_team2:

                        team_1.add_Draw()
                        team2.add_Draw()

                    elif score_team_1 > score_team2:
                        team_1.add_Win()
                        team2.add_Lose()
                    else:
                        team2.add_Win()
                        team_1.add_Lose()

                    position+=2 #increase 2 step to the right to just allow a team play just one game by round  
                    game+=1
                position = 0
            order+= 1 #changing the order of the matches to avoid repeat a team play 2 games in a round 

    #get the team_groups <<dict of group with teamObjects>> key=group_name : value= {key=country: value=teamObject } 
    def get_groups(self):
        return self.group
    
    #method to check the list of teams 
    def get_teams(self):
        if len(list(self.team_list.values())) !=0:
            for each in self.team_list:
                print(each)
        else: 
            print('There is not teams to show') 

    #method tha return the list of 16 names of teams that pass to the round 16, 
    #sequence [1GA, 2GA, 1GB, 2GB .... 1GH, 2GH]
    def get_winners_16(self):
        
        final_sort=[]
        #function to sort the data by the option 
        #option = 'Pts' or 'GD' or 'GF' 
        #list_name, list of teams that have the same amount of points [in the chosen option]
        #group_name, the name of  the group the evalue 'GroupA', 'GroupB'..'GroupH'
        #group_list = <<dict of group with teamObjects>> key=group_name : value= {key=country: value=teamObject } 
        def dic_sort(group_name, group_list, list_name, option):
            option_dict = {}
            
            for each in list_name:
                option_dict[each] = group_list[group_name][each].results[option] #getting each country name : value [in the chosen option]
            points = sorted(option_dict.values(), reverse = 1) #create a list with the values sorted from Max to Min 

            sorted_list = []
            draw_list = []
            value = 0
            while value < len(points):
                values = list(option_dict.values()) #get the list of values for each key 
                pos = values.index(points[value]) #get the pos of the value [in the points list] in the array values
                key = list(option_dict.keys())[pos] #getting the name of the team according the position 
                #validation if there is the same amount of points [in the chosen option] for left 
                if points[value] == points[value-1]:
                    draw_list.append(key) #append to a draw list 
                    option_dict.pop(key)  #remove the team from the object to avoid call again 
                    sorted_list.append(0) #insert a 0 value if the team goes to draw list  
                    value+=1
                #validation if there is the same amount of points [in the chosen option] for the right 
                elif points[value] == points[value+1-len(points)]:
                    option_dict.pop(key)
                    sorted_list.append(0)
                    draw_list.append(key)
                    value+=1
                else:
                    #if there is not same amount of points append to sorted list 
                    sorted_list.append(key)
                    value+=1
            
            #return the sorted list and draw list 
            results = [sorted_list, draw_list]
            return results
    
        #sorting all the groups 
        finalists_16_list = []
        for each in self.group:
            #print(each)

            #getting the list of names by sorting the points 
            sorted_by_points = dic_sort(each, self.group, list(self.group[each].keys()), 'Pts')
            #print('points:', sorted_by_points)
            if len(sorted_by_points[1]) != 0: #checking if the drawList is empty 
                #if two teams have the same points let's check GD
                sorted_by_GD = dic_sort(each, self.group, sorted_by_points[1], 'GD')
                #print(sorted_by_GD)

                if len(sorted_by_GD[1]) != 0: #checking if the drawList is empty 
                    #if two teams have the same points let's check GF
                    sorted_by_GF = dic_sort(each, self.group, sorted_by_GD[1], 'GF')
                    #print(sorted_by_GF)
                    if len(sorted_by_GF[1]) != 0: 
                        final_sort = sorted_by_GF[1]
                    else:
                        final_sort = sorted_by_GF[0]  
                else:
                    final_sort = sorted_by_GD[0]
            else:
                None
                #print('there is not teams with the same points values')

            counter = 0
            new_list = [] #new list with the teams sorted by Pts, GD and GF 
            for n in range(0, len(sorted_by_points[0])):   
                if sorted_by_points[0][n] == 0:
                    new_list.append(final_sort[counter]) #final_sort have the team of the drawList sorted 
                    counter+=1    
                else:
                    new_list.append(sorted_by_points[0][n])

            #updating the values  
            #print(new_list)
            new_group_list = {}
            i = 0
            for eachTeam in new_list: #loop in the sorted list of the 4 teams 
                new_group_list[eachTeam] = self.group[each][eachTeam] #insert the value of each team in order (sorted)
                if i <2:
                    finalists_16_list.append(eachTeam) #append the first 2 teams of each group 
                    i+=1

            self.group[each] = new_group_list #update the dict of teams on each group 
        return finalists_16_list
