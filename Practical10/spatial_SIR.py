#make the 2D model
#import labraries
import numpy as np
import matplotlib.pyplot as plt

def spatial_SIR(time_point):
    """
    input: the interested time ponit
    code: simulate the spread of disease
    output: the population at the interested time point
    """
    #create an array of population
    #let '0' as susceptible, '1' as infected, '2' as recovered
    population=np.zeros((100,100))
    #randomly chose one of the 10000 people to be the first patient
    outbreak=np.random.choice(range(100),2)
    population[outbreak[0],outbreak[1]]=1
    #set up parameters

    beta=0.3
    gamma=0.05
    n=0#used to record the current time point
    while n<time_point:
        n+=1
        new_population=population#copy the previous population and work on the copy
        #create i and j to work on every person in the population
        i=0
        while i<100:
            j=0
            while j<100:
                #for every person, first check what stage he is in
                #if in susceptible or recovered stage, do no change
                #if in infected stage, firstly, work on his neighbors: check whether the neighbour can be infected (whether he is in stage susceptible). if so, use random to determine whether he is infected
                #                      then, work on himself: use random to determine whether he is recovered
                #special cases: for persons who live at edge, they don't have 8 neighbours. these people are recognized by following way.
                leftup=(i==0 and j==0)
                left=(i==0 and j!=0 and j!=99)
                leftdown=(i==0 and j==99)
                up=(i!=0 and i!=99 and j==0)
                down=(i!=0 and i!=99 and j==99)
                rightup=(i==99 and j==0)
                right=(i==99 and j!=0 and j!=99)
                rightdown=(i==99 and j==99)
                if population[i,j]==1:#check whether the person is infected
                    
                    #the first 'if group' is used as an example
                    if not (leftup or left or leftdown or up or rightup):#to recognize and inhibit some of the people living at the edge from doing the following
                        if population[i-1,j-1]==0:#to check whether this neighbour can be infected
                            if np.random.random()<beta:#to determine whether he is infected
                                new_population[i-1,j-1]=1
                    
                    #the others are just like that
                    if not (leftup or left or leftdown):
                        if population[i-1,j]==0:
                            if np.random.random()<beta:
                                new_population[i-1,j]=1
                    if not (leftup or left or leftdown or down or rightdown):
                        if population[i-1,j+1]==0:
                            if np.random.random()<beta:
                                new_population[i-1,j+1]=1
                    if not (leftup or up or rightup):
                        if population[i,j-1]==0:
                            if np.random.random()<beta:
                                new_population[i,j-1]=1
                    if not (leftdown or down or rightdown):
                        if population[i,j+1]==0:
                            if np.random.random()<beta:
                                new_population[i,j+1]=1
                    if not (leftup or up or rightup or right or rightdown):
                        if population[i+1,j-1]==0:
                            if np.random.random()<beta:
                                new_population[i+1,j-1]=1
                    if not (rightup or right or rightdown):
                        if population[i+1,j]==0:
                            if np.random.random()<beta:
                                new_population[i+1,j]=1
                    if not (leftdown or down or rightup or right or rightdown):
                        if population[i+1,j+1]==0:
                            if np.random.random()<beta:
                                new_population[i+1,j+1]=1
                    
                    #for himself, determine whether he is recovered
                    if np.random.random()<gamma:
                        new_population[i,j]=2
                j+=1
            i+=1
        population=new_population#update the population
    return population

#draw figures showing the distrbution of the population
plt.figure(1,figsize=(6,4),dpi=150)
plt.imshow(spatial_SIR(10),cmap='viridis',interpolation='nearest')
plt.figure(2,figsize=(6,4),dpi=150)
plt.imshow(spatial_SIR(50),cmap='viridis',interpolation='nearest')
plt.figure(3,figsize=(6,4),dpi=150)
plt.imshow(spatial_SIR(100),cmap='viridis',interpolation='nearest')
plt.show()