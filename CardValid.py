def mod10(card):
    y = len(card)
    digit = 0
    
    for x in range (0, y):
        if x%2 != 0:
            digit +=(card[x] * 2)
            if card[x]*2 >= 10:
                digit -= 9
        else:
            digit += (card[x])
            
    if digit%10 == 0:
        return 1
    else:
        return 0
        

    
def isValid(card):
    key = 1
    if len(card) < 13 or len(card) > 16:
        key = 0
    elif card[0] < 3 or card[0] > 6:
        key = 0
    elif card[0] == 3 and card[1] != 7:
        key = 0
    elif mod10(card[::-1]) == 0:
        key = 0
    
    return key
    
while True:
    try:
        num = int(input("Input Card Number: "))
    except ValueError:
        continue
    else:
            break

card = [int(x) for x in str(num)]

if isValid(card)== 1:
    print("CARD IS VALID")
elif isValid(card)== 0:
    print("CARD IS INVALID")


