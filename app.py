#!/usr/bin/env python 
# Kevin Lizarazo
# CSV to cleaner textfile, when dealing with FENSinformation files 
# TO-DO . . . remove topics with certain keywords + parameters for extra columns (event desc., source links)

import csv

avoidlist = set()

print; print "This script cleans up a CSV file from fensinformation.com. Make sure the script and CSV file are in the same directory before proceeding."; print

fh = open('words_to_avoid.txt')
for element in fh:
    element = element.rstrip()
    avoidlist.add(element)
fh.close()

user_input = raw_input('Please enter the full CSV filename (ex: "events.csv"): ')

eventlist = []
eventobject = ''
count = 0
position = 0 

fh = open(user_input, 'rB') 
reader = csv.reader(fh)

for line in reader: 
    title = line[0]
    date = line[1][5:10]
    if any(word in title for word in avoidlist):
        continue
    eventobject = date + ' : ' + title 
    eventlist.append(eventobject + '\n')
    count = count + 1

    
fh.close()

sortedevents = sorted(eventlist)

user_input_2 = raw_input('Please enter a name for the new file: ')

print "Now writing a new file . . . "

while position < count:
    nfh = open(user_input_2 + '.txt', 'a')
    nfh.write(sortedevents[position])
    nfh.close()
    position = position + 1

print "A new file, {}.txt, has been created in the same directory where this script is located.".format(user_input_2)