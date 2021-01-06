from sys import exit

def readability():
    text = input("Text: ")

    if text == "":
        print("Before Grade 1")
        exit(1)
    
    res = text.split()
    words = len(text.split())
    letters = 0
    sentences = 0;
    
    for i in range (0, words):
        letters += (len(res[i]))
        if ('.' in res[i]) or ('!' in res[i]) or ('?' in res[i]):
            sentences+=1
        for j in range (0, len(res[i])):
            if not (res[i][j].isalpha() or res[i][j].isdigit()):
                letters-=1

    print(words)
    print(letters)
    print(sentences)
    L = letters/words * 100
    S = sentences/words * 100
    result = 0.0588 * L - 0.296 * S - 15.8
    
    index = round(result)
    if index < 1:
        print("Before Grade 1")
    elif index > 15:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


readability()
