import csv
import pandas as pd
import plotly.express as px
from sys import exit

csv_File = input("CSV file to be processed: ")

df = pd.read_csv(csv_File)

while(True):
    region = input("Region: ")

    print("\n1 - The number of positive cases for each province of the region")
    print("2 - The number of active cases for each province of the region")
    print("3 - The number of positive cases by sex for the region")
    print("4 - The number of positive cases by each age group for the region")
    print("5 - The number of positive cases by health status")
    print("6 - The number of deaths by sex for the region")
    print("7 - The number of deaths by each age group for the region")
    print("8 - The number of asymptomatic cases for each province of the region")
    print("9 - Back")
    print("0 - Exit\n")
    choice = int(input("Choice: "))
    print("")

    if(choice == 0):
        exit(1)

    elif(choice == 1):
        df1 = df[(df.RegionRes == region)]
        df2 = df1.groupby(["CityMunRes"]).count().reset_index()
        fig = px.bar(df2,y=df1.groupby(["CityMunRes"]).size(),x="CityMunRes",color='CityMunRes')
        fig.show()

    elif(choice == 2):
        df1 = df[(df.RegionRes == region)&(df.HealthStatus != 'RECOVERED') & (df.HealthStatus != 'DIED')]
        df2 = df1.groupby(["CityMunRes"]).count().reset_index()
        fig = px.bar(df2,y=df1.groupby(["CityMunRes"]).size(),x="CityMunRes",color='CityMunRes')
        fig.show()

    elif(choice == 3):
        #cursor.execute("SELECT COUNT (*), Sex FROM cases WHERE Region = (?) GROUP BY Sex", (region,))
        df1 = df[(df.RegionRes == region)]
        df2 = df1.groupby(["Sex"]).count().reset_index()
        fig = px.bar(df2,y=df1.groupby(["Sex"]).size(),x="Sex",color='Sex')
        fig.show()

    elif(choice == 4):
        #cursor.execute("SELECT COUNT (*), AgeGroup FROM cases WHERE Region = (?) GROUP BY AgeGroup ORDER BY AgeGroup", (region,))
        df1 = df[(df.RegionRes == region)]
        df2 = df1.groupby(["AgeGroup"]).count().reset_index()
        fig = px.bar(df2,y=df1.groupby(["AgeGroup"]).size(),x="AgeGroup",color='AgeGroup')
        fig.show()

    elif(choice == 5):
        #cursor.execute("SELECT COUNT (*), Status FROM cases GROUP BY Status")
        df1 = df.groupby(["HealthStatus"]).count().reset_index()
        fig = px.bar(df1,y=df.groupby(["HealthStatus"]).size(),x="HealthStatus",color='HealthStatus')
        fig.show()

    elif(choice == 6):
        #cursor.execute("SELECT COUNT (*), Sex FROM cases WHERE Region = (?) AND Status = 'DIED' GROUP BY Sex", (region,))
        df1 = df[(df.RegionRes == region)&(df.HealthStatus == 'DIED')]
        df2 = df1.groupby(["Sex"]).count().reset_index()
        fig = px.bar(df2,y=df1.groupby(["Sex"]).size(),x="Sex",color='Sex')
        fig.show()

    elif(choice == 7):
        #cursor.execute("SELECT COUNT (*), AgeGroup FROM cases WHERE Region = (?) AND Status = 'DIED' GROUP BY AgeGroup ORDER BY AgeGroup", (region,))
        df1 = df[(df.RegionRes == region)&(df.HealthStatus == 'DIED')]
        df2 = df1.groupby(["AgeGroup"]).count().reset_index()
        fig = px.bar(df2,y=df1.groupby(["AgeGroup"]).size(),x="AgeGroup",color='AgeGroup')
        fig.show()

    elif(choice == 8):
        #cursor.execute("SELECT COUNT (*), City FROM cases WHERE Region = (?) AND Status = 'ASYMPTOMATIC' GROUP BY City", (region,))
        df1 = df[(df.RegionRes == region)&(df.HealthStatus == 'ASYMPTOMATIC')]
        df2 = df1.groupby(["CityMunRes"]).count().reset_index()
        fig = px.bar(df2,y=df1.groupby(["CityMunRes"]).size(),x="CityMunRes",color='CityMunRes')
        fig.show()

