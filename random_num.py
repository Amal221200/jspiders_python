import random

num = random.randint(1, 100)
is_found = False
for i in range(0, 3):
    un = int(input('Enter a number from 1 to 100:\n'))
    if un == num:
        is_found = True
        print("Booyeah!")
        break
    elif un > num:
        print("Your num is greater.")
    elif un < num:
        print("Your num is smaller.")

if(not is_found):
    print('Sorry your chance is over, try next time, the number was {}'.format(num))
