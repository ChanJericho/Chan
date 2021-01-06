from sys import argv
import sqlite3

    
if len(argv) != 2:
    print("Usage: python roster.py House")
    exit(1)
else:
    connection = sqlite3.connect("students.db")
    crsr = connection.cursor()

    crsr.execute("SELECT first, middle, last, birth FROM 'students' WHERE house = (?) ORDER BY last, first", (argv[1],))
    ans = crsr.fetchall()
    for i in range(0,len(ans)):
        if ans[i][1] == None:
            print(ans[i][0] + " " + ans[i][2] + ", born", ans[i][3])
        else:
            print(ans[i][0] + " " + ans[i][1] + " " + ans[i][2] + ", born", ans[i][3])

        
