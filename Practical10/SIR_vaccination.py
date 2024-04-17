#mostly the same as SIR.py
#but this focus only on the number of infected people
#besides, vaccinated people were add into this population.
#it won't change over time but it was identified at the begining

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

index=[0]
time_point=0
while time_point<n:
    index.append(time_point+1)
    time_point+=1

def SIR(vaccination):
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
    V_number=0
    time_point=0
    V=vaccination*(S+I+R)
    S=S-V
    while S_number<S:
        S_number+=1
        population.append('S')
    while I_number<I:
        I_number+=1
        population.append('I')
    while V_number<V:
        V_number+=1
        population.append('V')
    #create lists to record number of people in different stages
    infected=[I]

    #make loops
    while time_point<n:
        time_point+=1
        new_population=[]#record the new population, clear up when new loop starts
        j=0
        while j<(S+I+R):
            #for each person, draw random number to determine whether he goes into next stage, and record in new_population
            if population[j]=='S':
                betacheck=np.random.random()
                if betacheck<=(beta*population.count('I')/(S+I+R+V)):
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
            if population[j]=='V':
                new_population.append('V')
            j+=1
        population=new_population
        #record number of people in different stages
        infected.append(population.count('I'))
    return infected

#create the figure
plt.figure()
plt.plot(index,SIR(0))
plt.plot(index,SIR(0.1))
plt.plot(index,SIR(0.2))
plt.plot(index,SIR(0.3))
plt.plot(index,SIR(0.4))
plt.plot(index,SIR(0.5))
plt.plot(index,SIR(0.6))
plt.plot(index,SIR(0.7))
plt.plot(index,SIR(0.8))
plt.plot(index,SIR(0.9))
plt.plot(index,SIR(1))
plt.legend(['0','10%','20%','30%','40%','50%','60%','70%','80%','90%','100%'])
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rate')
plt.show()

