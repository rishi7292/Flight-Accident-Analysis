#Description: This program show the survival and death rate for 25 years of air accidents reported.
# This will help in visulaizing the pattern and how frequently people were taking flights.
#Importing packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections
#importing Ordered dictionary
from collections import OrderedDict
#importing itemgetter
from operator import itemgetter

#reading csv file Flights_data
defi = pd.read_csv('Flight_data.csv',quotechar='"',skipinitialspace=True, delimiter=',').fillna(0)
#moving the read data to a matrix variable data_1
data_1 = defi.as_matrix()

dat_Death = collections.defaultdict(list)
dat_Srv = collections.defaultdict(list)

#loop for analysing deaths and survival based on Aircraft damage: Destroyed or Substantial.

for row in data_1:
#fetching data till 2016 year and collecting data for destroyed and substantial aircrafts.    
	if row[3] < '1992-01-01': continue
	if row[11] == 'Destroyed' or row[11] == 'Substantial':
		fetch = row[3][0:4]
#checking for fatal injuries contributing to death		
		cal_1 = 0 if(row[23]) ==""  else float(row[23])
		dat_Death.setdefault(fetch,[]).append(cal_1)
#checking for serious and minor injuries and uninjured 		
		cal_2 = 0 if(row[24] or row[25] or row[26]) =="" else float(row[24]) + float(row[25]) + float(row[26])
		dat_Srv.setdefault(fetch,[]).append(cal_2)

#creating new dictionary for storing deaths year wise		
dat2_Death = {}
for key, value in dat_Death.items(): dat2_Death[key] = sum(value)
for key2, value2 in dat2_Death.items(): 
#printing total deaths
    print ("{}:{} Death count".format(key2,value2))

#creating new dictionary for storing survival year wise		
dat2_Srv = {}
for key3, value3 in dat_Srv.items(): dat2_Srv[key3] = sum(value3)
for key4, value4 in dat2_Srv.items(): 
#printing total survival
    print ("{}:{} Survival count".format(key4,value4))


# Sorting dictionary dict2 increaseing order
sort = OrderedDict(sorted(dat2_Srv.items(), key=itemgetter(1)))

# Sorting dictionary dict2 increaseing order
sort1 = OrderedDict(sorted(dat2_Death.items(), key=itemgetter(1)))

#Getting all the survivors values from dictionary
Srv_values = sort.values()
#Getting all Death values from Dictionary
death_values = sort1.values()

#plotting death and Survival rate. 
y_position = np.arange(len(dat2_Death))

#ploting stacked graph
plt_1 = plt.bar(y_position, Srv_values, color = '#8888ff')
plt_2 = plt.bar(y_position, death_values, color = 'r', bottom = Srv_values)
#x axis headngs
plt.xticks(y_position, dat2_Srv.keys(), rotation=90)
#graph title
plt.title('DEATH & SURVIVAL RATE')
#x label
plt.xlabel('RESPECTIVE YEARS')
#y label
plt.ylabel('DEATH/SURVIVAL PERCENTAGE')

#graph legend
plt.legend((plt_1[0], plt_2[0]), ('SURVIVORS', 'DEATHS'))

for var1,var2,var3 in zip(y_position, Srv_values, death_values):
#adjusting graph texts    
	plt.text(var1-0.25, 650, str("%.0f" % (var2 / ((var2+var3) / 100))) + '%', rotation=90, color = 'black')
	plt.text(var1-0.25, var2+var3+650, str("%.0f" % (var3 / ((var2+var3) / 100))) + '%', rotation=90)

#saving graph
#plt.savefig('Death and survival over 25 years.png', bbox_inches='tight')
#show plot
plt.show()
#end