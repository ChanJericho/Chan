import csv
from sys import argv, exit
import sqlite3

if len(argv) != 2 or not argv[1].endswith('.csv'):
    print("Usage: python import.py characters.csv")
    exit(1)

connection = sqlite3.connect("students.db")
crsr = connection.cursor()

with open(argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
        
    for row in csv_reader:
        name = row[0].split()
        if(len(row[0].split()) == 2):
            crsr.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",(name[0], None, name[1], row[1], row[2]))
        elif(len(row[0].split()) == 3):
            crsr.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)",(name[0], name[1], name[2], row[1], row[2]))

connection.commit()
connection.close()
