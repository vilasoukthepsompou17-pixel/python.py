x = 0
while x < 10:
    print(x)
    x += 1
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()



x = 9

while x > 0:
    y = 1
    while y <= x:
        print(y, end=" ")
        y += 1
    print()
    x -= 1
    
