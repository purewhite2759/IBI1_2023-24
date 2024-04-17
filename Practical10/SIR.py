#import labraries
import numpy as np
import matplotlib.pyplot as plt

#define variables
S=9999
I=1
R=0
beta=0.3
gamma=0.05
n=1000

population=[]# create the population list
S_number=0
I_number=0
time_point=0
while S_number<S:
    S_number+=1
    population.append('S')
while I_number<I:
    I_number+=1
    population.append('I')
#create lists to record number of people in different stages
index=[0]#used to record x axis
susceptible=[S]
infected=[I]
recovered=[R]

#make loops
while time_point<n:
    index.append(time_point+1)
    time_point+=1
    new_population=[]#record the new population, clear up when new loop starts
    j=0
    while j<(S+I+R):
        #for each person, draw random number to determine whether he goes into next stage, and record in new_population
        if population[j]=='S':
            betacheck=np.random.random()
            if betacheck<=(beta*population.count('I')/(S+I+R)):
                new_population.append('I')
            else:
                new_population.append('S')
        if population[j]=='I':
            gammacheck=np.random.random()
            if gammacheck<=gamma:
                new_population.append('R')
            else:
                new_population.append('I')
        if population[j]=='R':
            new_population.append('R')
        j+=1
    population=new_population
    #record number of people in different stages
    susceptible.append(population.count('S'))
    infected.append(population.count('I'))
    recovered.append(population.count('R'))

#create the figure
plt.figure()
plt.plot(index,susceptible)
plt.plot(index,infected)
plt.plot(index,recovered)
plt.legend(['susceptible','infected','recovered'])
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.show()

