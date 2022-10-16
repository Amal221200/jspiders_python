# 1. write a program to check if the given character is an alphabet, number or special character

'''char = input("Enter a character: ")

if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
    print('entered character is an alphabet')
elif ('0' <= char <= '9'):
    print('entered character is a number')
else:
    print('entered character is a special character')'''

# 2. write a program to check the greatest of two numbers

'''a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

if a > b:
    print('a is the greatest')
elif b > a:
    print('b is the greatest')
else:
    print('both are equal')'''

# 3. write a program to check the greatest of three numbers

'''a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

if a > b > c or a > c > b:
    print('a is the greatest')
elif b > a > c or b > c > a:
    print('b is the greatest')
elif c > a > b or c > b > a:
    print('c is the greatest')
else:
    print('all three are equal')

if a > b and a > c:
    print('a is the greatest')
elif b > a and b > c:
    print('b is the greatest')
elif c > a and c > b:
    print('c is the greatest')
else:
    print('all three are equal')'''
