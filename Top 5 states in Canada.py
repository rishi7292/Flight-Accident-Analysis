#Description: This program counts the top 10 states in CANADA causing the most number of injuries.
#The calculation is based upon fatal and severe injuries and plots the corresponding states with injury frequency.


#importing Packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd,collections

#importing operator
import operator

data1 = pd.read_csv('Flight_data.csv',quotechar='"',skipinitialspace=True, delimiter=',').fillna(0)
#fetching Matrix of data1 in data2
data2 = data1.as_matrix()

#Variable dict1 for storing the dictionary list
dict1 = collections.defaultdict(list)

#Getting top 5 places in Canada with most number of injuries
maskcan =  (data2[:,5] == 'Canada')

#fetching data from csv file regarding locations in CANADA with most injuries in accident.col[4]
for row in data2[maskcan]:
    fetch_2 = row[4]
    if fetch_2 == "" or fetch_2 == 0: continue

#most injuries will be summation of fatal and serious injuries col[24] and col[25]
    most_injury_2 = 0 if(row[24]) =="" else float(row[24]+row[25])

#summming the most injuries with respect to country and state    
    dict1.setdefault(fetch_2,[]).append(most_injury_2)


# create another dictionary dict3
dict3 = {}

#For total injuries greater than 0 add the value to dictionary dict1
for key, value in dict1.items(): dict3[key] = sum(value)

#Top 5 states in Canada with most number of injuries.
top_5_can = dict(sorted(dict3.items(), key=operator.itemgetter(1), reverse=True)[:5])
print(top_5_can)

# plotting bar graph to identify the top 5 places contributing to most injuries.
#getting dictionary values to y_position variable 
y_position_2 = np.arange(len(top_5_can))
for h,j in zip(y_position_2, top_5_can.values()):
	plt.text(h-0.25, j, str(j))

plt.bar(y_position_2, top_5_can.values(), align='center', alpha=0.5, color='b')

plt.xticks(y_position_2, top_5_can.keys(), rotation=0)

plt.ylabel('FREQUENCY OF INJURY/STATE')

plt.title('TOP 5 STATES IN CANADA WITH MAX INJURIES')

#plt.savefig('INJURY FREQUENCY VS STATE Canada.png', bbox_inches='tight')

plt.show()
#end
