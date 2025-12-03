#while_basic.py

x = 1
l = 11
while x < 10:
    y = 1
    while y <= x:
        print(y,end=" ")
        y+=1
    print()
    x +=1
print()
a = 10
while a >= 1:
    b = 10
    while b >= l - a:
        #
        print(b,end=" ")
        b -=1
    print()
    a -= 1