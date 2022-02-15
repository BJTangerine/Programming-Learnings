# loads CSV data and identifies months with highest crime number

import csv
from datetime import datetime
from collections import Counter


# creates Python file object in read mode
csvfile = open('crime_sampler.csv', 'r')

# creates empty crime data list
crime_data = list()

# loops over csv reader on the file object to add date, crime type, location description, and arrest data
for row in csv.reader(csvfile):

    crime_data.append((row[0], row[2], row[4], row[5]))
    
# removes the headers from crime_data
crime_data.pop(0)


# creates counter object
crimes_by_month = Counter()

# loop over crime data to convert 1st element of each item into datetime object and
# increment counter object for the month associated with row by 1.
for i in crime_data:

    date = datetime.strptime(i[0], '%m/%d/%Y %I:%M:%S %p')

    crimes_by_month[date.month] += 1
    

# prints the 3 most common months for crime
print(crimes_by_month.most_common(3))