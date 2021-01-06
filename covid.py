import csv
from sys import exit
import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
import numpy as np

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%\n({v:d})'.format(p=pct,v=val)
    return my_autopct

csvFile = input("Input name of CSV file: ")

if not csvFile.endswith('.csv'):
    print("Error must end with .csv")
    exit(1)

connection = sqlite3.connect("cases.db")
crsr = connection.cursor()
crsr.execute("DROP TABLE IF EXISTS cases")
crsr.execute("CREATE TABLE cases(AgeGroup varchar(255), Sex varchar(255), Region varchar(255), City varchar(255), Status varchar(255))")

with open(csvFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
        
    for row in csv_reader:
        crsr.execute("INSERT INTO cases (AgeGroup, Sex, Region, City, Status) VALUES(?, ?, ?, ?, ?)",(row[2], row[3], row[11], row[13], row[17]))
        

connection.commit()
choice = 1

while(choice != 0):
    labels = []
    values = []
    title = ""
    region = input("Input name of the region: ")
    print("\nChoose Visualization")
    print("[1] The number of positive cases for each province of the region")
    print("[2] The number of active cases for each province of the region")
    print("[3] The number of positive cases by sex for the region")
    print("[4] The number of positive cases by each age group for the region")
    print("[5] The number of positive cases by health status")
    print("[6] The number of deaths by sex for the region")
    print("[7] The number of deaths by each age group for the region")
    print("[8] The number of asymptomatic cases for each province of the region")
    print("[0] Exit\n")
    choice = int(input("Choice: "))
    print("")

    if(choice == 0):
        exit(1)

    elif(choice == 1):
        crsr.execute("SELECT COUNT (*), City FROM cases WHERE Region = (?) GROUP BY City", (region,))
        ans = crsr.fetchall()
        for i in range(len(ans)):
            values.append(ans[i][0])
            if(ans[i][1] == ""):
                labels.append("No City Stated")
            else:
                labels.append(ans[i][1])
        title = "Number of Positive Cases for each Province of the Region " + region

    elif(choice == 2):
        crsr.execute("SELECT COUNT (*), City FROM cases WHERE Region = (?) AND Status != 'RECOVERED' AND Status != 'DIED'GROUP BY City", (region,))
        ans = crsr.fetchall()
        for i in range(len(ans)):
            values.append(ans[i][0])
            if(ans[i][1] == ""):
                labels.append("No City Stated")
            else:
                labels.append(ans[i][1])
        title = "Number of Active Cases for each Province of the Region " + region

    elif(choice == 3):
        crsr.execute("SELECT COUNT (*), Sex FROM cases WHERE Region = (?) GROUP BY Sex", (region,))
        ans = crsr.fetchall()
        for i in range(len(ans)):
            values.append(ans[i][0])
            labels.append(ans[i][1])
        title = "Number of Positive Cases by Sex for Region " + region

    elif(choice == 4):
        crsr.execute("SELECT COUNT (*), AgeGroup FROM cases WHERE Region = (?) GROUP BY AgeGroup ORDER BY AgeGroup", (region,))
        ans = crsr.fetchall()
        for i in range(len(ans)):
            values.append(ans[i][0])
            labels.append(ans[i][1])
        title = "Number of Positive Cases by each Age Group for Region " + region

    elif(choice == 5):
        crsr.execute("SELECT COUNT (*), Status FROM cases GROUP BY Status")
        ans = crsr.fetchall()
        for i in range(len(ans)):
            values.append(ans[i][0])
            labels.append(ans[i][1])
        title = "Number of Positive Cases by Health Status "

    elif(choice == 6):
        crsr.execute("SELECT COUNT (*), Sex FROM cases WHERE Region = (?) AND Status = 'DIED' GROUP BY Sex", (region,))
        ans = crsr.fetchall()
        for i in range(len(ans)):
            values.append(ans[i][0])
            labels.append(ans[i][1])
        title = "Number of Deaths by Sex for Region " + region

    elif(choice == 7):
        crsr.execute("SELECT COUNT (*), AgeGroup FROM cases WHERE Region = (?) AND Status = 'DIED' GROUP BY AgeGroup ORDER BY AgeGroup", (region,))
        ans = crsr.fetchall()
        for i in range(len(ans)):
            values.append(ans[i][0])
            labels.append(ans[i][1])
        title = "Number of Deaths by each Age Group for Region " + region

    elif(choice == 8):
        crsr.execute("SELECT COUNT (*), City FROM cases WHERE Region = (?) AND Status = 'ASYMPTOMATIC' GROUP BY City", (region,))
        ans = crsr.fetchall()
        for i in range(len(ans)):
            values.append(ans[i][0])
            if(ans[i][1] == ""):
                labels.append("No City Stated")
            else:
                labels.append(ans[i][1])
        title = "Number of Asymptomatic Cases for each Province of the Region " + region
    


    fig1, ax1 = plt.subplots()
    ax1.pie(values, labels=labels, autopct= make_autopct(values), pctdistance = 0.7, startangle=90, radius = 1.5)
    ax1.axis('equal')
    ax1.set_title(title)
    plt.show()

connection.close()






