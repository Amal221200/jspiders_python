def squareSum(num):
    digits = len(str(num))
    sqsum = 0
    for i in range(0, digits):
        sqsum += int(str(num)[i])**2
    return sqsum


'''for num in range(1, 101):
    n = num    
    while n != 1 or n != 7:
        n = squareSum(n)
        if n==1 or n==7:
            print(num, end=',')
            break
        elif n < 10:
            break
        else:
            continue'''

for num in range(1, 51):
    n = num
    for i in range(1, 11):
        n = squareSum(n)
        if n == 1 or n == 7:
            print(num)
            break
