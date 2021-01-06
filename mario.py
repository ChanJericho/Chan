
while True:
    try:
        n = int(input("Height: "))
    except ValueError:
        continue
    else:
        if n >= 1 and n <= 8:
            break
k = n - 1

for i in range(0, n):
    for j in range(0,k):
    	print(" ", end = "")

    k = k-1
    
    for j in range (0, i+1):
    	print("#", end="")

    print(end="  ")

    for j in range (0, i+1):
        print("#", end="")
    print("\r")

