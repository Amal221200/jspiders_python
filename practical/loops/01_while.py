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

'''count = 1

while count <= 100:
    if count%7==0 and count%5==0:
        print('Multiple of 5 and 7 :-',count)
    elif count%7==0 or count%5==0:
        print('Multiple of 5 or 7 :-',count)
    count += 1'''

# wap to print even numbers in the entered range

'''n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the last number: '))

while n1 <= n2:
    if n1%2== 0:
        print(n1)
    n1+=1'''

# wap to print odd numbers in the entered range

'''n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the last number: '))

while n1 <= n2:
    if n1%2 != 0:
        print(n1)
    n1+=1'''

# wap to print find the sum of the digit enter by the user
'''
num = int(input('Enter the user: '))
sum = 0
count = 0
num_cpy = num
while count < len(str(num)):
    sum += num_cpy % 10
    num_cpy = num_cpy//10
    count+=1

print(sum)
'''

# password validator
'''
password = input('Enter your password: ')

index, upper, lower, spl, number, space = (0,0,0,0,0, 0)

if len(password) >= 8:

    while index < len(password):
        if password[index] == ' ':
            space +=1
            break
        elif 'A' <= password[index] <= 'Z':
            upper += 1
        elif 'a' <= password[index] <= 'z':
            lower += 1
        elif '0' <= password[index] <= '9':
            number += 1
        else:
            spl += 1

        index += 1

    if space != 0:
        print('Space is not allowed.')
    elif number >= 1 and upper >= 1 and lower >= 1 and spl >= 1:
        print('It is a valid password.')
    else:
        print('The password must contain atleast one uppercase, lowercase, number and special character.')
else:
    print('The pasword should be atleast 8 char')'''


# library charge

'''days = int(input('Enter the number of days you had the book: '))

charge = 0

start = 1'''
# while start <= days:
#     if start <= 5:
#         charge += 2
#     elif start <= 10:
#         charge += 3
#     elif start <= 15:
#         charge += 4
#     else:
#         charge += 5
#     start += 1

# print(f'The total charge is {charge}')

'''if days > 15:
    days_to_charge = days-15
    charge += days_to_charge*5
    days -= days_to_charge
    
if 10 <= days <= 15:
    days_to_charge = days-10
    charge += days_to_charge*4
    days-=days_to_charge

if 5<= days <= 10:
    days_to_charge = days-5
    charge += days_to_charge*3
    days-=days_to_charge

if 1<= days<= 5:
    charge += days*2

print(charge)'''

# rickshaw bill

'''kms = int(input('Enter the no. of km: '))
charge = 0
count = 1
if kms > 0:
    while count <= kms:
        if count <=10:
            charge += 11
        elif 11 <= count <= 100:
            charge += 10
        else:
            charge += 9
        count += 1
else:
    charge = 0

print(f'your charge is {charge}')'''

# electric bill

'''units = int(input('Enter the no. of units: '))
charge = 0
count = 1
if units > 0:
    while count <= units:
        if count <= 100:
            charge += 0
        elif count <= 300:
            charge += 2
        else:
            charge += 5
        count += 1
else:
    charge = 0

print(f'your charge is {charge}')'''

# print the extentions of the filename in the list

'''files = ['youtube.txt', 'yahoo.pdf',
         'microsoft.doc', 'apple.xls', 'amazon.xml']
index = 0
while index < len(files):
    file = files[index]
    print(file[-4:])
    index += 1'''

# print the extentions of the filename in the list

'''files = ['youtube.txt', 'amazon.pdf',
         'facebook.pdf', 'google.pdf', 'apple.doc']
index = 0
while index < len(files):
    file = files[index]
    if file[-3:] == 'pdf':
        print(file)
    index += 1'''

# extract number values from the given list and add into a new list

l = [1,2.0, 4+4j, (1,2,3), [1,2,3], '1,2,3,', {1,2,3}]
new_list = []
index = 0

while index < len(l):
    if isinstance(l[index],(int, float, complex)):
        new_list.append(l[index])
    index+=1

print(new_list)