# prime

for num in range(1,101):
    count = 0
    if num != 1:
        for n in range(1, (num**2)+1):
            if num % n == 0:
                count+=1
    if not count > 2:
        print(num)