#Description: This program plot the chart for fatal injuries record over 25 year from 1993 till 2016 
# majorly comprises of death or fatal injuries. 

#Importing packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict
import collections
#importing itemgetter
from operator import itemgetter

#defining variable and matrix
defi = pd.read_csv('Flight_data.csv',quotechar='"',skipinitialspace=True, delimiter=',').fillna(0)
data1 = defi.as_matrix()

#defining dictionary to collect data 
data_Death = collections.defaultdict(list)

#Collecting death information for past 25 years
for row in data1:
	if row[3] < '1992-01-01': continue
	fetch = row[3][0:4]
	cal = 0 if(row[23]) ==""  else float(row[23])
#Collect fatal injuries data contributing to death over the years and adding to collection list data_Death	
	data_Death.setdefault(fetch,[]).append(cal)

#defining new dictionary for storing death values per year		
data2_Death = {}
for key, value in data_Death.items(): data2_Death[key] = sum(value)
for key2, value2 in data2_Death.items(): 
    print ("{}:{} Fatal injury count".format(key2,value2))

# Sorting dictionary dict2 increaseing order
sort = OrderedDict(sorted(data2_Death.items(), key=itemgetter(1)))


#plotting bar graph for fatal injury records over the years
y_position = np.arange(len(data2_Death))

#defining bar graph
plt.bar(y_position, sort.values())


#defining x-label
plt.xticks(y_position, sort.keys(), rotation=90)

#defining title
plt.title('FATAL INJURY FREQUENCY RECORD OVER 25 YEARS')

#defining y-label
plt.ylabel('FATAL INJURY RECORD')
plt.xlabel('RESPECTIVE YEARS')
for c,d in zip(y_position, sort.values()):
#adjusting text 
	plt.text(c-0.25, 500, str("%.0f" % d), rotation=90, color = 'black')
#save plot
#plt.savefig('Fatal injuries over 25years.png', bbox_inches='tight')
#show plot
plt.show()
#end