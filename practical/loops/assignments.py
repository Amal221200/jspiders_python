# 01. print even numbers from 1 - 20

'''
count = 1

while count <= 20:
    if count %2==0:
        print(count, end=' ')
    count+=1
'''

# 02. print odd numbers from 20 - 1

'''
count = 20

while count >= 1:
    if count %2!=0:
        print(count, end=' ')
    count-=1
'''

# 03. print even indexed elements from the list

'''l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = 0

while index < len(l):
    if index % 2 == 0:
        print(l[index], end=' ')
    index += 1'''

# 04. print odd indexed elements from the list in reverse
'''
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = len(l)-1

while index >= 0:
    if index % 2 != 0:
        print(l[index], end=' ')
    index -= 1'''

# 05. extract all the odd indexed characters and store them inside a list 

'''s = 'Hulk smash'
l = []
index = 0

while index < len(s):
    if index % 2 != 0:
        l.append(s[index])
    index += 1
print(l)'''

# 05. extract all the odd indexed characters and store them inside a list 

'''s = 'Hulk smash'
l = []
index = 0

while index < len(s):
    if s[index] in 'aeiouAEIOU':
        l.append(s[index])
    index += 1
print(l)'''

# 06. extract all the characters and store them inside a dictionary with its index as the value of the corresponding character as the key 

'''[s = 'Hulk smash'
d = {}
index = 0

while index < len(s):
    d.update({index: s[index]})
    index += 1
print(d)]'''

# 07. add all the words from a string and its length  as a pair inside a dictionary 

'''s = 'Programming is fun with python'
l_of_words = s.split(' ')
d = {}
index = 0

while index < len(l_of_words):
    d.update({len(l_of_words[index]): l_of_words[index]})
    index += 1
print(d)'''

# 12. extract all the numbers in the strings an print the sum of the digits 

s = 'jacaob.smith12345@gmail.com'

summation = 0
index = 0

while index < len(s):
    if '0' <=s[index] <= '9':
        summation += int(s[index])
    index += 1
print(summation)
