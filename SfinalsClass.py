#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Semi finals class
class Sfinals:

    #Empty list as an attribute to pass on the winners for the Final
    sfinalsw=[]
    
    #Empty list as an attribute to pass on the losers for third and fourth
    sfinalsl=[]
    
    #Constructor with only goals and penalties for inputing just the results of each match
    def __init__(self, c1goals=0, c2goals=0, c1penals=0, c2penals=0,qfinalswss=[0]*4,sfinalsws=sfinalsw,sfinalsls=sfinalsl):
        self.c1goals = c1goals
        self.c2goals = c2goals
        self.c1penals = c1penals
        self.c2penals = c2penals
        self.qfinalswss = [qfinalswss[0],qfinalswss[1],qfinalswss[2],qfinalswss[3]]
        self.sfinalsws = sfinalsws
        self.sfinalsls = sfinalsls
        
#Functions for printing the results of the match 1
    def sround1result(self):
        print("Semi finals=")
        print()
        print("Match 1:")
        
        if self.c1goals==self.c2goals:
            print(self.qfinalswss[0],self.c1goals,"("+str(self.c1penals)+")")
            print(self.qfinalswss[1],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")  
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.qfinalswss[0])
                self.sfinalsws.append(self.qfinalsws[0])
                self.sfinalsls.append(self.qfinalsws[1])
            else:
                print("WINNER:",self.qfinalswss[1])
                self.sfinalsws.append(self.qfinalsws[1])
                self.sfinalsls.append(self.qfinalsws[0])
            
             
        elif self.c1goals!=self.c2goals:
            print(self.qfinalswss[0],self.c1goals)
            print(self.qfinalswss[1],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.qfinalswss[0])
                self.sfinalsws.append(self.qfinalswss[0])
                self.sfinalsls.append(self.qfinalswss[1])
            else:
                print("WINNER:",self.qfinalswss[1])
                self.sfinalsws.append(self.qfinalswss[1])
                self.sfinalsls.append(self.qfinalswss[0])

#Functions for printing the results of the match 2
    def sround2result(self):
        print()
        print("Match 2:")
        
        if self.c1goals==self.c2goals:
            print(self.qfinalswss[2],self.c1goals,"("+str(self.c1penals)+")")
            print(self.qfinalswss[3],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")  
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.qfinalsws[2])
                self.sfinalsws.append(self.qfinalswss[2])
                self.sfinalsls.append(self.qfinalswss[3])
            else:
                print("WINNER:",self.qfinalsws[3])
                self.sfinalsws.append(self.qfinalswss[3])
                self.sfinalsls.append(self.qfinalswss[2])
            
             
        elif self.c1goals!=self.c2goals:
            print(self.qfinalswss[2],self.c1goals)
            print(self.qfinalswss[3],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.qfinalswss[2])
                self.sfinalsws.append(self.qfinalswss[2])
                self.sfinalsls.append(self.qfinalswss[3])
            else:
                print("WINNER:",self.qfinalswss[3])
                self.sfinalsws.append(self.qfinalswss[3])
                self.sfinalsls.append(self.qfinalswss[2])
                
#Method to return winners list
    def sfinalswinnerslist(self):
        return self.sfinalsws
    
#Method to return losers list
    def sfinalsloserslist(self):
        return self.sfinalsls


# In[2]:

#To insert the results and previous stage winners
def insertScoresSFinal(Qfinalslist):
    #General input instructions
    goals_= " FT goals (integers only):"
    penals_= " penals (integers only; if there are no penals enter 0):"

    #List of objects of Sfinals
    print(Qfinalslist[0]+" vs "+Qfinalslist[1])

    sfinalsmatch1=Sfinals(int(input(Qfinalslist[0]+goals_)),
                          int(input(Qfinalslist[1]+goals_)),
                          int(input(Qfinalslist[0]+penals_)),
                          int(input(Qfinalslist[1]+penals_)),
                         Qfinalslist)

    print()
    print(Qfinalslist[2]+" vs "+Qfinalslist[3])

    sfinalsmatch2=Sfinals(int(input(Qfinalslist[2]+goals_)),
                          int(input(Qfinalslist[3]+goals_)),
                          int(input(Qfinalslist[2]+penals_)),
                          int(input(Qfinalslist[3]+penals_)),
                         Qfinalslist)

    
    roundSfinalList = [sfinalsmatch1, sfinalsmatch2]
    #Creating the list of winners of Sfinals for the Final
    swinners=Sfinals()
    swinnerpass=swinners.sfinalswinnerslist()

    #Creating the list of losers of Sfinals for third and fourth
    slosers=Sfinals()
    sloserpass=slosers.sfinalsloserslist()
    return [swinnerpass, sloserpass, roundSfinalList] 


# In[3]:

#Printing all Sfinals results
def printSfinal(roundSfinalList):
    #Printing the objects and results of Sfinals
    roundSfinalList[0].sround1result()
    roundSfinalList[1].sround2result()

