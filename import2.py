from sys import argv, exit
import csv
import sqlite3


def Import():
    
    if len(argv) != 2:
        print("Usage: python import.py characters.csv")
        exit(1)
        
    with open(argv[1], 'r') as file:
        reader = csv.reader(file)

        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()

        for row in reader:
            name = row[0].split(" ")
            names = len(row[0].split())
            if names == 2:
                x = (name[0], None, name[1], row[1], row[2])
            elif names == 3:
                x = (name[0], name[1], name[2], row[1], row[2])

            if not names == 1:    
                cursor.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", x)

        connection.commit()
        cursor.close()
        connection.close()   


Import()
