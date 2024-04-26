#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Thirdnfourth class
class Tnf:

    #Constructor with only goals and penalties for inputing just the last match
    def __init__(self,c1goals=0,c2goals=0,c1penals=0,c2penals=0,sfinalslss=[0]*2):
        self.c1goals = c1goals
        self.c2goals = c2goals
        self.c1penals = c1penals
        self.c2penals = c2penals
        self.sfinalslss = [sfinalslss[0],sfinalslss[1]]
        
#Function for printing the results of the last match
    def tnfround1result(self):
        print("Third place play-off=")
        print()
        
        if self.c1goals==self.c2goals:
            print(self.sfinalslss[0],self.c1goals,"("+str(self.c1penals)+")")
            print(self.sfinalslss[1],self.c2goals,"("+str(self.c2penals)+")")
            print()
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")  
            elif self.c1penals>self.c2penals:
                print("Third:",self.sfinalslss[0])
                print("Fourth:",self.sfinalslss[1])
            else:
                print("Third:",self.sfinalslss[1])
                print("Fourth:",self.sfinalslss[0])
            
             
        elif self.c1goals!=self.c2goals:
            print(self.sfinalslss[0],self.c1goals)
            print(self.sfinalslss[1],self.c2goals)
            print()
            
            if self.c1goals>self.c2goals:
                print("Third:",self.sfinalslss[0])
                print("Fourth:",self.sfinalslss[1])
            else:
                print("Third:",self.sfinalslss[1])
                print("Fourth:",self.sfinalslss[0])



# In[2]:

#To insert the results and previous stage winners
def insertScoresThirdnFourthRound(sloserpass):#List for inserting sfinals losers 
    Sfinalslist=[sloserpass[0],sloserpass[1]]

    #General input instructions
    goals_= " FT goals (integers only):"
    penals_= " penals (integers only; if there are no penals enter 0):"
    #List of objects of ThirdnFourth
    print(Sfinalslist[0]+" vs "+Sfinalslist[1])

    tnfmatch=Tnf(int(input(Sfinalslist[0]+goals_)),
                 int(input(Sfinalslist[1]+goals_)),
                 int(input(Sfinalslist[0]+penals_)),
                 int(input(Sfinalslist[1]+penals_)),
                Sfinalslist)
    
    #Printing the objects and results of Final
    tnfmatch.tnfround1result()

