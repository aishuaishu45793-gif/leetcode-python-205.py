num = int(input("Enter a number: "))

total = 0

for digit in str(num):
    factorial = 1

    for i in range(1, int(digit) + 1):
        factorial *= i

    total += factorial

if num >= 0 and total == num:
    print("Strong Number")
else:
    print("Not a Strong Number")