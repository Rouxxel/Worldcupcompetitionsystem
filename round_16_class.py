#!/usr/bin/env python
# coding: utf-8

#Round 16 class
class Round16:
    #Empty list as an attribute to pass the winners to quarter finals
    round_16_winners=[]
    
    #Constructor with only goals and penalties for input just the results of each match one by one
    def __init__(self, c1_goals=0, c2_goals=0, c1_penalties=0, c2_penalties=0,group_winners=[0]*16,
                round_16_winners=round_16_winners):
        self.c1_goals = c1_goals
        self.c2_goals = c2_goals
        self.c1_penalties = c1_penalties
        self.c2_penalties = c2_penalties
        self.group_winners = [group_winners[0],group_winners[1],group_winners[2],group_winners[3],
                            group_winners[4],group_winners[5],group_winners[6],group_winners[7],
                            group_winners[8],group_winners[9],group_winners[10],group_winners[11],
                            group_winners[12],group_winners[13],group_winners[14],group_winners[15]]
        self.round_16_winners = round_16_winners
    
    #Functions for printing the results of the match 1
    def round_1_result(self):
        print("Round 16=")
        print()
        print("Match 1:")
        
        if self.c1_goals==self.c2_goals:
            print(self.group_winners[0],self.c1_goals,"("+str(self.c1_penalties)+")")
            print(self.group_winners[3],self.c2_goals,"("+str(self.c2_penalties)+")")
            
            if self.c1_penalties==self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties>self.c2_penalties:
                print("WINNER:",self.group_winners[0])
                self.round_16_winners.append(self.group_winners[0])
            else:
                print("WINNER:",self.group_winners[3])
                self.round_16_winners.append(self.group_winners[3])
            
        elif self.c1_goals!=self.c2_goals:
            print(self.group_winners[0],self.c1_goals)
            print(self.group_winners[3],self.c2_goals)
            
            if self.c1_goals>self.c2_goals:
                print("WINNER:",self.group_winners[0])
                self.round_16_winners.append(self.group_winners[0])
            elif self.c1_goals<self.c2_goals:
                print("WINNER:",self.group_winners[3])
                self.round_16_winners.append(self.group_winners[3])

    #Functions for printing the results of the match 2
    def round_2_result(self):
        print()
        print("Match 2:")
        
        if self.c1_goals==self.c2_goals:
            print(self.group_winners[4],self.c1_goals,"("+str(self.c1_penalties)+")")
            print(self.group_winners[7],self.c2_goals,"("+str(self.c2_penalties)+")")
            
            if self.c1_penalties==self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties>self.c2_penalties:
                print("WINNER:",self.group_winners[4])
                self.round_16_winners.append(self.group_winners[4])
            else:
                print("WINNER:",self.group_winners[7])
                self.round_16_winners.append(self.group_winners[7])
            
        elif self.c1_goals!=self.c2_goals:
            print(self.group_winners[4],self.c1_goals)
            print(self.group_winners[7],self.c2_goals)
            
            if self.c1_goals>self.c2_goals:
                print("WINNER:",self.group_winners[4])
                self.round_16_winners.append(self.group_winners[4])
            elif self.c1_goals<self.c2_goals:
                print("WINNER:",self.group_winners[7])
                self.round_16_winners.append(self.group_winners[7])
                
    #Functions for printing the results of the match 3
    def round_3_result(self):
        print()
        print("Match 3:")
        
        if self.c1_goals==self.c2_goals:
            print(self.group_winners[8],self.c1_goals,"("+str(self.c1_penalties)+")")
            print(self.group_winners[11],self.c2_goals,"("+str(self.c2_penalties)+")")
            
            if self.c1_penalties==self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties>self.c2_penalties:
                print("WINNER:",self.group_winners[8])
                self.round_16_winners.append(self.group_winners[8])
            else:
                print("WINNER:",self.group_winners[11])
                self.round_16_winners.append(self.group_winners[11])
            
        elif self.c1_goals!=self.c2_goals:
            print(self.group_winners[8],self.c1_goals)
            print(self.group_winners[11],self.c2_goals)
            
            if self.c1_goals>self.c2_goals:
                print("WINNER:",self.group_winners[8])
                self.round_16_winners.append(self.group_winners[8])
            elif self.c1_goals<self.c2_goals:
                print("WINNER:",self.group_winners[11])  
                self.round_16_winners.append(self.group_winners[11])

    #Functions for printing the results of the match 4
    def round_4_result(self):
        print()
        print("Match 4:")
        
        if self.c1_goals==self.c2_goals:
            print(self.group_winners[12],self.c1_goals,"("+str(self.c1_penalties)+")")
            print(self.group_winners[15],self.c2_goals,"("+str(self.c2_penalties)+")")
            
            if self.c1_penalties==self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties>self.c2_penalties:
                print("WINNER:",self.group_winners[12])
                self.round_16_winners.append(self.group_winners[12])
            else:
                print("WINNER:",self.group_winners[15])
                self.round_16_winners.append(self.group_winners[15])
            
        elif self.c1_goals!=self.c2_goals:
            print(self.group_winners[12],self.c1_goals)
            print(self.group_winners[15],self.c2_goals)
            
            if self.c1_goals>self.c2_goals:
                print("WINNER:",self.group_winners[12])
                self.round_16_winners.append(self.group_winners[12])
            elif self.c1_goals<self.c2_goals:
                print("WINNER:",self.group_winners[15])
                self.round_16_winners.append(self.group_winners[15])

    #Functions for printing the results of the match 5
    def round_5_result(self):
        print()
        print("Match 5:")
        
        if self.c1_goals==self.c2_goals:
            print(self.group_winners[1],self.c1_goals,"("+str(self.c1_penalties)+")")
            print(self.group_winners[2],self.c2_goals,"("+str(self.c2_penalties)+")")
            
            if self.c1_penalties==self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties>self.c2_penalties:
                print("WINNER:",self.group_winners[1])
                self.round_16_winners.append(self.group_winners[1])
            else:
                print("WINNER:",self.group_winners[2])
                self.round_16_winners.append(self.group_winners[2])
            
        elif self.c1_goals!=self.c2_goals:
            print(self.group_winners[1],self.c1_goals)
            print(self.group_winners[2],self.c2_goals)
            
            if self.c1_goals>self.c2_goals:
                print("WINNER:",self.group_winners[1])
                self.round_16_winners.append(self.group_winners[1])
            elif self.c1_goals<self.c2_goals:
                print("WINNER:",self.group_winners[2])
                self.round_16_winners.append(self.group_winners[2])
                
    #Functions for printing the results of the match 6
    def round_6_result(self):
        print()
        print("Match 6:")
        
        if self.c1_goals==self.c2_goals:
            print(self.group_winners[5],self.c1_goals,"("+str(self.c1_penalties)+")")
            print(self.group_winners[6],self.c2_goals,"("+str(self.c2_penalties)+")")
            
            if self.c1_penalties==self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties>self.c2_penalties:
                print("WINNER:",self.group_winners[5])
                self.round_16_winners.append(self.group_winners[5])
            else:
                print("WINNER:",self.group_winners[6])
                self.round_16_winners.append(self.group_winners[6])
            
        elif self.c1_goals!=self.c2_goals:
            print(self.group_winners[5],self.c1_goals)
            print(self.group_winners[6],self.c2_goals)
            
            if self.c1_goals>self.c2_goals:
                print("WINNER:",self.group_winners[5])
                self.round_16_winners.append(self.group_winners[5])
            elif self.c1_goals<self.c2_goals:
                print("WINNER:",self.group_winners[6])
                self.round_16_winners.append(self.group_winners[6])
                
    #Functions for printing the results of the match 7
    def round_7_result(self):
        print()
        print("Match 7:")
        
        if self.c1_goals==self.c2_goals:
            print(self.group_winners[9],self.c1_goals,"("+str(self.c1_penalties)+")")
            print(self.group_winners[10],self.c2_goals,"("+str(self.c2_penalties)+")")
            
            if self.c1_penalties==self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties>self.c2_penalties:
                print("WINNER:",self.group_winners[9])
                self.round_16_winners.append(self.group_winners[9])
            else:
                print("WINNER:",self.group_winners[10])
                self.round_16_winners.append(self.group_winners[10])
            
        elif self.c1_goals!=self.c2_goals:
            print(self.group_winners[9],self.c1_goals)
            print(self.group_winners[10],self.c2_goals)
            
            if self.c1_goals>self.c2_goals:
                print("WINNER:",self.group_winners[9])
                self.round_16_winners.append(self.group_winners[9])
            elif self.c1_goals<self.c2_goals:
                print("WINNER:",self.group_winners[10])
                self.round_16_winners.append(self.group_winners[10])
                
    #Functions for printing the results of the match 8
    def round_8_result(self):
        print()
        print("Match 8:")
        
        if self.c1_goals==self.c2_goals:
            print(self.group_winners[13],self.c1_goals,"("+str(self.c1_penalties)+")")
            print(self.group_winners[14],self.c2_goals,"("+str(self.c2_penalties)+")")
            
            if self.c1_penalties==self.c2_penalties:
                print("Invalid result, please restart")
            elif self.c1_penalties>self.c2_penalties:
                print("WINNER:",self.group_winners[13])
                self.round_16_winners.append(self.group_winners[13])
            else:
                print("WINNER:",self.group_winners[14])
                self.round_16_winners.append(self.group_winners[14])
            
        elif self.c1_goals!=self.c2_goals:
            print(self.group_winners[13],self.c1_goals)
            print(self.group_winners[14],self.c2_goals)
            
            if self.c1_goals>self.c2_goals:
                print("WINNER:",self.group_winners[13])
                self.round_16_winners.append(self.group_winners[13])
            elif self.c1_goals<self.c2_goals:
                print("WINNER:",self.group_winners[14])
                self.round_16_winners.append(self.group_winners[14])
            
    #Method to return winners list
    def round_16_winners_list(self):
        return self.round_16_winners

    #To insert the results and previous stage winners
    def insert_scores_round_16(self,groups_list):
        #General input instructions
        goals_ = " FT goals (integers only):"
        penalties_ = " penalties (integers only; if there are no penalties enter 0):" 
        
        #List of objects of Round 16
        print(groups_list[0]+" vs "+groups_list[3])

        round_16_match_1=Round16(int(input(groups_list[0]+goals_)),
                            int(input(groups_list[3]+goals_)),
                            int(input(groups_list[0]+penalties_)),
                            int(input(groups_list[3]+penalties_)),
                            groups_list)

        print()
        print(groups_list[4]+" vs "+groups_list[7])

        round_16_match_2=Round16(int(input(groups_list[4]+goals_)),
                            int(input(groups_list[7]+goals_)),
                            int(input(groups_list[4]+penalties_)),
                            int(input(groups_list[7]+penalties_)),
                            groups_list)

        print()
        print(groups_list[8]+" vs "+groups_list[11])

        round_16_match_3=Round16(int(input(groups_list[8]+goals_)),
                            int(input(groups_list[11]+goals_)),
                            int(input(groups_list[8]+penalties_)),
                            int(input(groups_list[11]+penalties_)),
                            groups_list)

        print()
        print(groups_list[12]+" vs "+groups_list[15])

        round_16_match_4=Round16(int(input(groups_list[12]+goals_)),
                            int(input(groups_list[15]+goals_)),
                            int(input(groups_list[12]+penalties_)),
                            int(input(groups_list[15]+penalties_)),
                            groups_list)

        print()
        print(groups_list[1]+" vs "+groups_list[2])

        round_16_match_5=Round16(int(input(groups_list[1]+goals_)),
                            int(input(groups_list[2]+goals_)),
                            int(input(groups_list[1]+penalties_)),
                            int(input(groups_list[2]+penalties_)),
                            groups_list)

        print()
        print(groups_list[5]+" vs "+groups_list[6])

        round_16_match_6=Round16(int(input(groups_list[5]+goals_)),
                            int(input(groups_list[6]+goals_)),
                            int(input(groups_list[5]+penalties_)),
                            int(input(groups_list[6]+penalties_)),
                            groups_list)

        print()
        print(groups_list[9]+" vs "+groups_list[10])

        round_16_match_7=Round16(int(input(groups_list[9]+goals_)),
                            int(input(groups_list[10]+goals_)),
                            int(input(groups_list[9]+penalties_)),
                            int(input(groups_list[10]+penalties_)),
                            groups_list)

        print()
        print(groups_list[13]+" vs "+groups_list[14])

        round_16_match_8=Round16(int(input(groups_list[13]+goals_)),
                            int(input(groups_list[14]+goals_)),
                            int(input(groups_list[13]+penalties_)),
                            int(input(groups_list[14]+penalties_)),
                            groups_list)
        
        rounds_list = [round_16_match_1, round_16_match_2, round_16_match_3, round_16_match_4, 
                        round_16_match_5, round_16_match_6, round_16_match_7, round_16_match_8]

        #Creating a sorted list of winners of Round16 for the quarter finals
        r16winners=Round16()
        return [r16winners.round_16_winners_list(), rounds_list] 

    #Printing all Round 16 match results
    def printRound16(self,rounds_list):
        #Printing the objects and results of Round16
        rounds_list[0].round_1_result()
        rounds_list[1].round_2_result()
        rounds_list[2].round_3_result()
        rounds_list[3].round_4_result()
        rounds_list[4].round_5_result()
        rounds_list[5].round_6_result()
        rounds_list[6].round_7_result()
        rounds_list[7].round_8_result()
