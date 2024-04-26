#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Round 16 class
class Round16:
      
    #Empty list as an attribute to pass the winners to Qfinals
    round16w=[]
    
    #Constructor with only goals and penalties for inputing just the results of each match one by one
    def __init__(self, c1goals=0, c2goals=0, c1penals=0, c2penals=0,groupws=[0]*16,round16ws=round16w):
        self.c1goals = c1goals
        self.c2goals = c2goals
        self.c1penals = c1penals
        self.c2penals = c2penals
        self.groupws = [groupws[0],groupws[1],groupws[2],groupws[3],groupws[4],groupws[5],groupws[6],
                        groupws[7],groupws[8],groupws[9],groupws[10],groupws[11],groupws[12],groupws[13],
                        groupws[14],groupws[15]]
        self.round16ws = round16ws
    
#Functions for printing the results of the match 1
    def round1result(self):
        print("Round 16=")
        print()
        print("Match 1:")
        
        if self.c1goals==self.c2goals:
            print(self.groupws[0],self.c1goals,"("+str(self.c1penals)+")")
            print(self.groupws[3],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.groupws[0])
                self.round16ws.append(self.groupws[0])
            else:
                print("WINNER:",self.groupws[3])
                self.round16ws.append(self.groupws[3])
            
        elif self.c1goals!=self.c2goals:
            print(self.groupws[0],self.c1goals)
            print(self.groupws[3],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.groupws[0])
                self.round16ws.append(self.groupws[0])
            elif self.c1goals<self.c2goals:
                print("WINNER:",self.groupws[3])
                self.round16ws.append(self.groupws[3])

#Functions for printing the results of the match 2
    def round2result(self):
        print()
        print("Match 2:")
        
        if self.c1goals==self.c2goals:
            print(self.groupws[4],self.c1goals,"("+str(self.c1penals)+")")
            print(self.groupws[7],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.groupws[4])
                self.round16ws.append(self.groupws[4])
            else:
                print("WINNER:",self.groupws[7])
                self.round16ws.append(self.groupws[7])
            
        elif self.c1goals!=self.c2goals:
            print(self.groupws[4],self.c1goals)
            print(self.groupws[7],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.groupws[4])
                self.round16ws.append(self.groupws[4])
            elif self.c1goals<self.c2goals:
                print("WINNER:",self.groupws[7])
                self.round16ws.append(self.groupws[7])
                
#Functions for printing the results of the match 3
    def round3result(self):
        print()
        print("Match 3:")
        
        if self.c1goals==self.c2goals:
            print(self.groupws[8],self.c1goals,"("+str(self.c1penals)+")")
            print(self.groupws[11],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.groupws[8])
                self.round16ws.append(self.groupws[8])
            else:
                print("WINNER:",self.groupws[11])
                self.round16ws.append(self.groupws[11])
            
        elif self.c1goals!=self.c2goals:
            print(self.groupws[8],self.c1goals)
            print(self.groupws[11],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.groupws[8])
                self.round16ws.append(self.groupws[8])
            elif self.c1goals<self.c2goals:
                print("WINNER:",self.groupws[11])  
                self.round16ws.append(self.groupws[11])

#Functions for printing the results of the match 4
    def round4result(self):
        print()
        print("Match 4:")
        
        if self.c1goals==self.c2goals:
            print(self.groupws[12],self.c1goals,"("+str(self.c1penals)+")")
            print(self.groupws[15],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.groupws[12])
                self.round16ws.append(self.groupws[12])
            else:
                print("WINNER:",self.groupws[15])
                self.round16ws.append(self.groupws[15])
            
        elif self.c1goals!=self.c2goals:
            print(self.groupws[12],self.c1goals)
            print(self.groupws[15],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.groupws[12])
                self.round16ws.append(self.groupws[12])
            elif self.c1goals<self.c2goals:
                print("WINNER:",self.groupws[15])
                self.round16ws.append(self.groupws[15])

#Functions for printing the results of the match 5
    def round5result(self):
        print()
        print("Match 5:")
        
        if self.c1goals==self.c2goals:
            print(self.groupws[1],self.c1goals,"("+str(self.c1penals)+")")
            print(self.groupws[2],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.groupws[1])
                self.round16ws.append(self.groupws[1])
            else:
                print("WINNER:",self.groupws[2])
                self.round16ws.append(self.groupws[2])
            
        elif self.c1goals!=self.c2goals:
            print(self.groupws[1],self.c1goals)
            print(self.groupws[2],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.groupws[1])
                self.round16ws.append(self.groupws[1])
            elif self.c1goals<self.c2goals:
                print("WINNER:",self.groupws[2])
                self.round16ws.append(self.groupws[2])
                
#Functions for printing the results of the match 6
    def round6result(self):
        print()
        print("Match 6:")
        
        if self.c1goals==self.c2goals:
            print(self.groupws[5],self.c1goals,"("+str(self.c1penals)+")")
            print(self.groupws[6],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.groupws[5])
                self.round16ws.append(self.groupws[5])
            else:
                print("WINNER:",self.groupws[6])
                self.round16ws.append(self.groupws[6])
            
        elif self.c1goals!=self.c2goals:
            print(self.groupws[5],self.c1goals)
            print(self.groupws[6],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.groupws[5])
                self.round16ws.append(self.groupws[5])
            elif self.c1goals<self.c2goals:
                print("WINNER:",self.groupws[6])
                self.round16ws.append(self.groupws[6])
                
#Functions for printing the results of the match 7
    def round7result(self):
        print()
        print("Match 7:")
        
        if self.c1goals==self.c2goals:
            print(self.groupws[9],self.c1goals,"("+str(self.c1penals)+")")
            print(self.groupws[10],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.groupws[9])
                self.round16ws.append(self.groupws[9])
            else:
                print("WINNER:",self.groupws[10])
                self.round16ws.append(self.groupws[10])
            
        elif self.c1goals!=self.c2goals:
            print(self.groupws[9],self.c1goals)
            print(self.groupws[10],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.groupws[9])
                self.round16ws.append(self.groupws[9])
            elif self.c1goals<self.c2goals:
                print("WINNER:",self.groupws[10])
                self.round16ws.append(self.groupws[10])
                
#Functions for printing the results of the match 8
    def round8result(self):
        print()
        print("Match 8:")
        
        if self.c1goals==self.c2goals:
            print(self.groupws[13],self.c1goals,"("+str(self.c1penals)+")")
            print(self.groupws[14],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.groupws[13])
                self.round16ws.append(self.groupws[13])
            else:
                print("WINNER:",self.groupws[14])
                self.round16ws.append(self.groupws[14])
            
        elif self.c1goals!=self.c2goals:
            print(self.groupws[13],self.c1goals)
            print(self.groupws[14],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.groupws[13])
                self.round16ws.append(self.groupws[13])
            elif self.c1goals<self.c2goals:
                print("WINNER:",self.groupws[14])
                self.round16ws.append(self.groupws[14])
            
#Method to return winners list
    def round16winnerslist(self):
        return self.round16ws


# In[2]:

#To insert the results and previous stage winners
def insertScoresRound16(Groupslist):
    #General input instructions
    goals_ = " FT goals (integers only):"
    penals_ = " penals (integers only; if there are no penals enter 0):" 
    
    #List of objects of Round 16
    print(Groupslist[0]+" vs "+Groupslist[3])
 
    round16match1=Round16(int(input(Groupslist[0]+goals_)),
                          int(input(Groupslist[3]+goals_)),
                          int(input(Groupslist[0]+penals_)),
                          int(input(Groupslist[3]+penals_)),
                          Groupslist)

    print()
    print(Groupslist[4]+" vs "+Groupslist[7])

    round16match2=Round16(int(input(Groupslist[4]+goals_)),
                          int(input(Groupslist[7]+goals_)),
                          int(input(Groupslist[4]+penals_)),
                          int(input(Groupslist[7]+penals_)),
                         Groupslist)

    print()
    print(Groupslist[8]+" vs "+Groupslist[11])

    round16match3=Round16(int(input(Groupslist[8]+goals_)),
                          int(input(Groupslist[11]+goals_)),
                          int(input(Groupslist[8]+penals_)),
                          int(input(Groupslist[11]+penals_)),
                         Groupslist)

    print()
    print(Groupslist[12]+" vs "+Groupslist[15])

    round16match4=Round16(int(input(Groupslist[12]+goals_)),
                          int(input(Groupslist[15]+goals_)),
                          int(input(Groupslist[12]+penals_)),
                          int(input(Groupslist[15]+penals_)),
                         Groupslist)

    print()
    print(Groupslist[1]+" vs "+Groupslist[2])

    round16match5=Round16(int(input(Groupslist[1]+goals_)),
                          int(input(Groupslist[2]+goals_)),
                          int(input(Groupslist[1]+penals_)),
                          int(input(Groupslist[2]+penals_)),
                         Groupslist)

    print()
    print(Groupslist[5]+" vs "+Groupslist[6])

    round16match6=Round16(int(input(Groupslist[5]+goals_)),
                          int(input(Groupslist[6]+goals_)),
                          int(input(Groupslist[5]+penals_)),
                          int(input(Groupslist[6]+penals_)),
                         Groupslist)

    print()
    print(Groupslist[9]+" vs "+Groupslist[10])

    round16match7=Round16(int(input(Groupslist[9]+goals_)),
                          int(input(Groupslist[10]+goals_)),
                          int(input(Groupslist[9]+penals_)),
                          int(input(Groupslist[10]+penals_)),
                         Groupslist)

    print()
    print(Groupslist[13]+" vs "+Groupslist[14])

    round16match8=Round16(int(input(Groupslist[13]+goals_)),
                          int(input(Groupslist[14]+goals_)),
                          int(input(Groupslist[13]+penals_)),
                          int(input(Groupslist[14]+penals_)),
                         Groupslist)
    
    roundsList = [round16match1, round16match2, round16match3, round16match4, 
                  round16match5, round16match6, round16match7, round16match8]

    #Creating a sorted list of winners of Round16 for the Qfinals
    r16winners=Round16()
    return [r16winners.round16winnerslist(), roundsList] 


# In[3]:

#Printing all Round 16 match results
def printRound16(roundsList):
    #Printing the objects and results of Round16
    roundsList[0].round1result()
    roundsList[1].round2result()
    roundsList[2].round3result()
    roundsList[3].round4result()
    roundsList[4].round5result()
    roundsList[5].round6result()
    roundsList[6].round7result()
    roundsList[7].round8result()

