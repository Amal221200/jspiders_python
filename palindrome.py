num = input("Enter the number or string: ")

num_rev = num[::-1]

if num_rev == num:
    print("Your number or string is a palindrome")
else:
    print("Your number or string is not a palindrome")
