import sqlite3 
 
connection = sqlite3.connect("covid.db") 
  
crsr = connection.cursor()

n = input("Enter City: ")
 
crsr.execute("SELECT COUNT (*) FROM CovidCases WHERE CityMun LIKE (?) AND DateRepConf LIKE '30-Apr%'", (n,))  
ans = crsr.fetchone()  
print("COVID-19 positive cases:", ans[0]) 

crsr.execute("SELECT COUNT (*) FROM CovidCases WHERE CityMun LIKE (?) AND Sex LIKE 'Male' AND DateRepConf LIKE '30-Apr%'", (n,))  
ans = crsr.fetchone()  
print("\nFor Males:", ans[0]) 

crsr.execute("SELECT COUNT (*) FROM CovidCases WHERE CityMun LIKE (?) AND Sex LIKE 'Female'AND DateRepConf LIKE '30-Apr%'", (n,))  
ans = crsr.fetchone()  
print("For Females:", ans[0])

crsr.execute("SELECT COUNT (*) FROM CovidCases WHERE CityMun LIKE (?) AND SymptomType LIKE 'Asymptomatic'AND DateRepConf LIKE '30-Apr%'", (n,))  
ans = crsr.fetchone()  
print("For Asymptomatic:", ans[0]) 

crsr.execute("SELECT COUNT (*) FROM CovidCases WHERE CityMun LIKE (?) AND SymptomType LIKE 'Mild'AND DateRepConf LIKE '30-Apr%'", (n,))  
ans = crsr.fetchone()  
print("For Mild:", ans[0])

crsr.execute("SELECT COUNT (*) FROM CovidCases WHERE CityMun LIKE (?)  AND SymptomType LIKE 'Recovered'AND DateRepConf LIKE '30-Apr%'", (n,))  
ans = crsr.fetchone()  
print("For Recovered:", ans[0]) 

crsr.execute("SELECT COUNT (*) FROM CovidCases WHERE CityMun LIKE (?)  AND SymptomType LIKE 'Died'AND DateRepConf LIKE '30-Apr%'", (n,))  
ans = crsr.fetchone()  
print("For Died:", ans[0]) 

