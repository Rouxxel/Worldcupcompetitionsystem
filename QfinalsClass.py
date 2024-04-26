#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Quarter finals class
class Qfinals:
    
    #Empty list as an attribute to pass on the winners for the Semi-finals
    qfinalsw=[]
    
    #Constructor with only goals and penalties for inputing just the results of each match
    def __init__(self, c1goals=0, c2goals=0, c1penals=0, c2penals=0,r16wss=[0]*8,qfinalsws=qfinalsw):
        self.c1goals = c1goals
        self.c2goals = c2goals
        self.c1penals = c1penals
        self.c2penals = c2penals
        self.r16wss = [r16wss[0],r16wss[1],r16wss[2],r16wss[3],
                       r16wss[4],r16wss[5],r16wss[6],r16wss[7]]
        self.qfinalsws = qfinalsws
        

#Functions for printing the results of the match 1
    def qround1result(self):
        print("Quarter finals=")
        print()
        print("Match 1:")
        
        if self.c1goals==self.c2goals:
            print(self.r16wss[0],self.c1goals,"("+str(self.c1penals)+")")
            print(self.r16wss[1],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")  
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.r16wss[0])
                self.qfinalsws.append(self.r16wss[0])
            else:
                print("WINNER:",self.r16wss[1])
                self.qfinalsws.append(self.r16wss[1])
            
             
        elif self.c1goals!=self.c2goals:
            print(self.r16wss[0],self.c1goals)
            print(self.r16wss[1],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.r16wss[0])
                self.qfinalsws.append(self.r16wss[0])
            else:
                print("WINNER:",self.r16wss[1])
                self.qfinalsws.append(self.r16wss[1])

#Functions for printing the results of the match 2
    def qround2result(self):
        print()
        print("Match 2:")
        
        if self.c1goals==self.c2goals:
            print(self.r16wss[2],self.c1goals,"("+str(self.c1penals)+")")
            print(self.r16wss[3],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")  
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.r16wss[2])
                self.qfinalsws.append(self.r16wss[2])
            else:
                print("WINNER:",self.r16wss[3])
                self.qfinalsws.append(self.r16wss[3])
            
             
        elif self.c1goals!=self.c2goals:
            print(self.r16wss[2],self.c1goals)
            print(self.r16wss[3],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.r16wss[2])
                self.qfinalsws.append(self.r16wss[2])
            else:
                print("WINNER:",self.r16wss[3])
                self.qfinalsws.append(self.r16wss[3])
                
#Functions for printing the results of the match 3
    def qround3result(self):
        print()
        print("Match 3:")
        
        if self.c1goals==self.c2goals:
            print(self.r16wss[4],self.c1goals,"("+str(self.c1penals)+")")
            print(self.r16wss[5],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")  
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.r16wss[4])
                self.qfinalsws.append(self.r16wss[4])
            else:
                print("WINNER:",self.r16wss[5])
                self.qfinalsws.append(self.r16wss[5])
            
             
        elif self.c1goals!=self.c2goals:
            print(self.r16wss[4],self.c1goals)
            print(self.r16wss[5],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.r16wss[4])
                self.qfinalsws.append(self.r16wss[4])
            else:
                print("WINNER:",self.r16wss[5])
                self.qfinalsws.append(self.r16wss[5]) 
                
#Functions for printing the results of the match 4
    def qround4result(self):
        print()
        print("Match 4:")
        
        if self.c1goals==self.c2goals:
            print(self.r16wss[6],self.c1goals,"("+str(self.c1penals)+")")
            print(self.r16wss[7],self.c2goals,"("+str(self.c2penals)+")")
            
            if self.c1penals==self.c2penals:
                print("Invalid result, please restart")  
            elif self.c1penals>self.c2penals:
                print("WINNER:",self.r16wss[6])
                self.qfinalsws.append(self.r16wss[6])
            else:
                print("WINNER:",self.r16wss[7])
                self.qfinalsws.append(self.r16wss[7])
            
             
        elif self.c1goals!=self.c2goals:
            print(self.r16wss[6],self.c1goals)
            print(self.r16wss[7],self.c2goals)
            
            if self.c1goals>self.c2goals:
                print("WINNER:",self.r16wss[6])
                self.qfinalsws.append(self.r16wss[6])
            else:
                print("WINNER:",self.r16wss[7])
                self.qfinalsws.append(self.r16wss[7]) 


#Method to return winners list
    def qfinalswinnerslist(self):
        return self.qfinalsws 


# In[2]:

#To insert the results and previous stage winners
def insertScoresQFinal(R16list):
    #General input instructions
    goals_= " FT goals (integers only):"
    penals_= " penals (integers only; if there are no penals enter 0):"

    #List of objects of Qfinals
    print(R16list[0]+" vs "+R16list[1])

    qfinalsmatch1=Qfinals(int(input(R16list[0]+goals_)),
                          int(input(R16list[1]+goals_)),
                          int(input(R16list[0]+penals_)),
                          int(input(R16list[1]+penals_)),
                         R16list)

    print()
    print(R16list[2]+" vs "+R16list[3])

    qfinalsmatch2=Qfinals(int(input(R16list[2]+goals_)),
                          int(input(R16list[3]+goals_)),
                          int(input(R16list[2]+penals_)),
                          int(input(R16list[3]+penals_)),
                         R16list)

    print()
    print(R16list[4]+" vs "+R16list[5])

    qfinalsmatch3=Qfinals(int(input(R16list[4]+goals_)),
                          int(input(R16list[5]+goals_)),
                          int(input(R16list[4]+penals_)),
                          int(input(R16list[5]+penals_)),
                         R16list)

    print()
    print(R16list[6]+" vs "+R16list[7])

    qfinalsmatch4=Qfinals(int(input(R16list[6]+goals_)),
                          int(input(R16list[7]+goals_)),
                          int(input(R16list[6]+penals_)),
                          int(input(R16list[7]+penals_)),
                         R16list)
    
    roundsListQFinals = [qfinalsmatch1, qfinalsmatch2, qfinalsmatch3, qfinalsmatch4]
    #Creating the list of winners of Qfinals for the Sfinals
    qwinners=Qfinals()
    return [qwinners.qfinalswinnerslist(), roundsListQFinals] 


# In[3]:

#Printing all Qfinals match results
def printQfinal(roundsListQFinals):
   #Printing the objects and results of Qfinals
    roundsListQFinals[0].qround1result()
    roundsListQFinals[1].qround2result()
    roundsListQFinals[2].qround3result()
    roundsListQFinals[3].qround4result()

