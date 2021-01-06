import re
from sys import exit

def readability():
    
    text = input("Text: ")
    
    word = len(re.findall('\s', text))
    if word == 0:
        print("Before Grade 1")
        exit(1)
    word+=1
    
    L = (len(re.findall('\w', text))/word) * 100
    S = (len(re.findall('[.!?]', text))/word) * 100
    grade = 0.0588 * L - 0.296 * S - 15.8
   
    grade = round(grade)
    
    if grade >= 16:
        print("Grade 16+")
    elif grade < 1:
        print("Before Grade 1")
    else:
        print("Grade " + str(grade))


readability()
