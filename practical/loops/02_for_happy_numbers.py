def squareSum(num):
    digits = len(str(num))
    sum=0
    for i in range(0,digits):
        sum += int(str(num)[i])**2
    return sum

for num in range(1, 10001):
    n = num    
    while n != 1 or n != 7:
        n = squareSum(n)
        if n==1 or n==7:
            print(num, end=',')
            break
        elif n < 10:
            break
        else:
            continue