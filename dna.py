import csv
import re
from sys import argv, exit


if len(argv) != 3 or not argv[1].endswith('.csv')or not argv[2].endswith('.txt'):
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

data = []
with open(argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        data.append(row)

strings = []
for i in range (1,len(data[0])):
    strings.append(data[0][i])
    

with open(argv[2]) as file:
    sequence = file.read()
    
x = []

for i in range (len(strings)):
    String = strings[i]
    max = 0;
    while re.search(String, sequence):
        String+=strings[i]
        max+=1
    x.append(max)
    max = 0

for i in range (1,len(data)):
    check = 0
    for j in range (len(x)):
        if(x[j] == int(data[i][j+1])):
            check = 1
        else:
            check = 0
            break
    if(check == 1):
        print(data[i][0])
        exit(1)
  
print("No match")
exit(0)
