from sys import argv, exit
import csv
import re

def dna():
    
    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    else:  
        database = []
        with open(argv[1], 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                database.append(row)

        with open(argv[2]) as file:
            sequence = file.read()

        frequency = []

        for i in range(1, len(database[0])):
            temp = re.split("[A-Z]+", re.sub(database[0][i],"1", sequence))
            num = 0
            for j in range(len(temp)):
                if(temp[j] != ""):
                    if(len(temp[j]) > num):
                        num = len(temp[j])
                        
            frequency.append(num)


        for i in range(1, len(database)):
            num = 0
            for j in range (1, len(database[0])):
                if(int(database[i][j]) == frequency[j - 1]):
                    num+=1
            if(num == len(frequency)):
                print(database[i][0])
                exit(1)
            
        

        print("No match")
        exit(1)

dna()
