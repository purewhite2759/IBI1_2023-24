#create the dictionary
activity={'sleeping':8,'classes':6,'studying':3.5,'TV':2,'music':1,'other':3.5}
print(activity)
print('The average number of hours spent on sleeping',activity['sleeping'],'hours')
#word "sleeping" can be replaced by other activities (change the two 'sleeping' at the same time)
#create pie chart
import matplotlib.pyplot as plt
#parameter setting
activity_labels=['sleeping','classes','studying','TV','music','other']
time=[activity['sleeping'],activity['classes'],activity['studying'],activity['TV'],activity['music'],activity['other']]
#draw the figure
plt.figure()
plt.pie(time,labels=activity_labels)
plt.show()