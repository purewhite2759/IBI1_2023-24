#link population to city name (uk for instance)
uk={0.56:'Edinburgh',0.62:'Glasgow',0.04:'Stirling',9.7:'London'}
uk_population=[0.56,0.62,0.04,9.7]
#sort uk_population
uk_ordered_population=sorted(uk_population)
uk_ordered_city=[]
#sort uk_city in population order
for i in range (len(uk_ordered_population)):
    uk_ordered_city.append(uk[uk_ordered_population[i]])
print(uk_ordered_population)
print('<'.join(uk_ordered_city))
#cn is quite same as uk
cn={0.58:'Haining',8.4:'Hangzhou',29.9:'Shanghai',22.2:'Beijing'}
cn_population=[0.58,8.4,29.9,22.2]
cn_ordered_population=sorted(cn_population)
cn_ordered_city=[]
for i in range (len(cn_ordered_population)):
    cn_ordered_city.append(cn[cn_ordered_population[i]])
print(cn_ordered_population)
print('<'.join(cn_ordered_city))
#create bar plots
import matplotlib.pyplot as plt
import numpy as np
#parameter setting
uk_ind=np.arange(len(uk_ordered_population))
cn_ind=np.arange(len(cn_ordered_population))
#create the first figure
plt.figure(1)
plt.bar(uk_ordered_city,uk_ordered_population)
plt.ylabel('population')
plt.title('UK')
#create the second figure
plt.figure(2)
plt.bar(cn_ordered_city,cn_ordered_population)
plt.ylabel('population')
plt.title('China')
plt.show()
plt.clf()