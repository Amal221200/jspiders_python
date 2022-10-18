# wap to print 1 to 5 using while loop
'''
count = 1

while count <= 5:
    print(count)
    count += 1
'''
# print('\n########################\n')
# wap to print 5 to 1 using while loop
'''
count = 5

while count >= 1:
    print(count)
    count -= 1
'''
# wap to print even numbers from 0 to 10
'''
count = 1

while count <=10:
    if count%2==0:
        print(count)
    count+=2
'''
# wap to print odd numbers from 10 to 1
'''
count = 10

while count>=1:
    if count%2!=0:
        print(count)
    count-=1
'''
# wap to print multiples of 7 from 1 to 100
'''
count = 1

while count <= 100:
    if count%7==0:
        print(count)
    count += 1
'''
# wap to print multiples of 7 and 5, 7 or 5 from 1 to 100

count = 1

while count <= 100:
    if count%7==0 and count%5==0:
        print('Multiple of 5 and 7 :-',count)
    elif count%7==0 or count%5==0:
        print('Multiple of 5 or 7 :-',count)
    count += 1
