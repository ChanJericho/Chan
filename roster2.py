from sys import argv
import sqlite3


def roster():
    if len(argv) != 2:
        print("Usage: python roster.py House")
        exit(1)
    else:
        
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        cursor.execute("SELECT first, middle, last, birth FROM 'students' WHERE house = ? ORDER BY last, first", (argv[1],))
        record = cursor.fetchall()
        for i in range (0, len(record), 1):
            print(record[i][0], end = " ")
            if(record[i][1] is not None):
                print(record[i][1], end = " ")
            print(record[i][2], end = "")
            print(f", born {record[i][3]}")

        cursor.close()
        connection.close()

roster()
