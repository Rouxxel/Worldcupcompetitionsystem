#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Final class
class Final:

    #Constructor with only goals and penalties for inputing just the last match
    def __init__(self, c1goals=0, c2goals=0, c1penals=0, c2penals=0,sfinalswss=[0]*2):
        self.c1goals = c1goals
        self.c2goals = c2goals
        self.c1penals = c1penals
        self.c2penals = c2penals
        self.sfinalswss = [sfinalswss[0],sfinalswss[1]]
        
#Function for printing the results of the last match
    def fround1result(self):
        print("Grand Final=")
        print()
        
        if self.c1goals==self.c2goals:
            print(self.sfinalswss[0],self.c1goals,"("+str(self.c1penals)+")")
            print(self.sfinalswss[1],self.c2goals,"("+str(self.c2penals)+")")
            print()
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")  
            elif self.c1penals>self.c2penals:
                print("CHAMPION:",self.sfinalswss[0])
                print("Sub-champion:",self.sfinalswss[1])
            else:
                print("CHAMPION:",self.sfinalswss[1])
                print("Sub-champion:",self.sfinalswss[0])
            
             
        elif self.c1goals!=self.c2goals:
            print(self.sfinalswss[0],self.c1goals)
            print(self.sfinalswss[1],self.c2goals)
            print()
            
            if self.c1goals>self.c2goals:
                print("CHAMPION:",self.sfinalswss[0])
                print("Sub-champion:",self.sfinalswss[1])
            else:
                print("CHAMPION:",self.sfinalswss[1])
                print("Sub-champion:",self.sfinalswss[0])


# In[2]:

#To insert the results and previous stage winners
def insertScoresFinalRound(swinnerpass):

    #List for inserting sfinals winners                 
    Sfinalslist2=[swinnerpass[0],swinnerpass[1]]

    #General input instructions
    goals_= " FT goals (integers only):"
    penals_= " penals (integers only; if there are no penals enter 0):"

    #List of objects of Final
    print(Sfinalslist2[0]+" vs "+Sfinalslist2[1])

    finalmatch=Final(int(input(Sfinalslist2[0]+goals_)),
                      int(input(Sfinalslist2[1]+goals_)),
                      int(input(Sfinalslist2[0]+penals_)),
                      int(input(Sfinalslist2[1]+penals_)),
                    Sfinalslist2)
    
    #Printing the objects and results of Final
    finalmatch.fround1result()
    

