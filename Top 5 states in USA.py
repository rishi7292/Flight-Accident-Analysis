#Author-Ninad Panda
#Description: This program counts the top 10 states in the USA causing the most number of injuries.
#             The calculation is based upon fatal and severe injuries and plots the corresponding states with injury frequency.


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

#Getting top 5 places in United states with most number of injuries
maskUS =  (data2[:,5] == 'United States')

#fetching data from csv file regarding locations in united states with most injuries in accident.col[4]
for row in data2[maskUS]:
    fetch = row[4]
    if fetch == "" or fetch == 0: continue

#most injuries will be summation of fatal and serious injuries col[24] and col[25]
    most_injury = 0 if(row[24]) =="" else float(row[24]+row[25])


#summming the most injuries with respect to country and state    
    dict1.setdefault(fetch,[]).append(most_injury)

# create another dictionary dict2
dict2 = {}

#For total injuries greater than 0 add the value to dictionary dict1
for key, value in dict1.items(): dict2[key] = sum(value)

#Top 5 states in United states with most number of injuries.
top_5 = dict(sorted(dict2.items(), key=operator.itemgetter(1), reverse=True)[:5])
print(top_5)


# plotting bar graph to identify the top 5 places contributing to most injuries.
#getting dictionary values to y_position variable 
y_position = np.arange(len(top_5))
for f,g in zip(y_position, top_5.values()):
	plt.text(f-0.25, g+2, str(g))

plt.bar(y_position, top_5.values(), align='center', alpha=0.5, color='g')

plt.xticks(y_position, top_5.keys(), rotation=0)

plt.ylabel('FREQUENCY OF INJURY/STATE')

plt.title('TOP 5 STATES IN USA WITH MAX INJURIES')

#plt.savefig('INJURY FREQUENCY VS STATE:USA.png', bbox_inches='tight')

plt.show()
#end