x1 = int(input())
x2 = int(input())
x3 = int(input())
count = 0
while x3 != 0:
    
    if(x2 > x1 and x2 > x3):
        print("Value:", end=" " )
        print(count - 1)
        count = 0
    a = int(input())
    count += 1
    x1 = x2
    x2 = x3 
    x3 = a