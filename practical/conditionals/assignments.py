# 1. check whether the acii value of a character is even or odd

'''char = input('enter a character: ')

if ord(char) % 2 == 0:
    print('the ascii value of the entered character is even')
else:
    print('the ascii value of the entered character is odd')'''

# 2. write a program to take key from user check if its present in the dict, if present then increment the value by 1 else initialise the value by 1
'''marks = {'social': 89, "maths": 34, 'chemistry': 90, 'physics': 99}

key = input('Enter a subject: ')

if key in marks.keys():
    marks[key] = marks[key] + 1
    print(marks)
else:
    marks[key] = 1
    print(marks)'''

# 3. check if the string is ending with the vowel or not
'''char = input('Enter a string: ')

if char[-1] in 'aeiouAEIOU':
    print('The string is ending with a vowel')
else:
    print('The string is not ending with a vowel')'''

# 4. check if the given integer is positive, negative or zero

'''num = int(input('Enter any integer: '))

if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')'''

# 5. check if the given number is divisible by 5 or 7, both 5 and 7 or not

'''num = int(input('Enter any integer: '))

if num % 5 == 0 and num % 7 == 0:
    print('The number is divisible by both 5 and 7')
elif num % 5 == 0 or num % 7 == 0:
    print('The number is divisible by either 5 or 7')
else:
    print('The number is not divisible by both 5 and 7')'''

# 6. convert the positive numner to negative and vise-versa

'''num = int(input('Enter any integer: '))

print(-1*num)'''

# 7. check the number is one digit, two digit, three digit, or more than three digit

'''num = input('Enter any integer: ')

if len(num) == 1:
    print('The entered number is a single digit number')
elif len(num) == 2:
    print('The entered number is a two digit number')
elif len(num) == 3:
    print('The entered number is a three digit number')
else:
    print('The entered number has more than three digit')'''
