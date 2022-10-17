# wap to check the percentage given by the user and given the message accordingly:-
# A - if the percentage is above 90
# B - if the percentage is between 90 and above 80
# C - if the percentage is between 80 and above 60
# D - if the percentage is between 60 and above 35
# F - if the percentage is below 35

perc = int(input('Enter your percentage: '))

if 0 <= perc <= 100:
    if perc >= 35:
        print('Congratulations! You\'ve been passed')

        if perc > 90:
            print('You have got "A" grade')
        elif 80 < perc <= 90:
            print('You have got "B" grade')
        elif 60 < perc <= 80:
            print('You have got "C" grade')
        else:
            print('You have got "D" grade')
    else:
        print('Sorry, you\'ve been failed. You got "F" grade.')
else:
    print('Enter a valid mark')
