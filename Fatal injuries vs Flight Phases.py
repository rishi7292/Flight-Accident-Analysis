#Description: This program provides the frequency of fatalities caused during different phases of flight.
#It focuses on how the phases affect the criticality and fatal injuries. The plot shows different states of phases with corresponding fatal injury counts

#importing Packages 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import collections

#importing Ordered dictionary
from collections import OrderedDict
#importing itemgetter
from operator import itemgetter

data1 = pd.read_csv('Flight_data.csv',quotechar='"',skipinitialspace=True, delimiter=',').fillna(0)
#fetching Matrix of data1 in data2
data2 = data1.as_matrix()
#Variable dict1 for storing the collection list
dict1 = collections.defaultdict(list)
#fetching data from the csv file regarding flight phases column[28]
for row in data2:
    fetch = row[28]
    if fetch == "" or fetch == 0: continue

#For fatal injuries greater than 0 add the value to dictionary dict1
    fatal = 0 if(row[23]) ==""  else float(row[23])
    dict1.setdefault(fetch,[]).append(fatal)

# create another dictionary dict2
dict2 = {}
# sum the total number of fatality injury for each phase
print "Phases and corresponding total fatality:\n"
for key, value in dict1.items(): dict2[key] = sum(value)
for key, value in dict2.items(): 
    
    print ("{}:{}".format(key,value))

# Sorting dictionary dict2 increaseing order
sort = OrderedDict(sorted(dict2.items(), key=itemgetter(1)))


# plotting bar graph to identify the phases contributing to fatal injuries.
#getting dictionary values to y_position variable 
y_position = np.arange(len(dict2))

#setting text format
for d,v in zip(y_position, sort.values()):
	plt.text(d-0.25, v+10, str("%.0f" % v))

#plotting bar graph
plt.bar(y_position, sort.values(), align='center', alpha=0.5,color='r')

plt.xticks(y_position, sort.keys(), rotation=0)

plt.ylabel('FREQUENCY OF FATALITIES')

plt.title('FATALITIES VS FLIGHT PHASES')

#plt.savefig('FATALITIES VS FLIGHT PHASES.png', bbox_inches='tight')
#show bar graph
plt.show()
#end