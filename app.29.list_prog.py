numbers = [2, 5, 6, 4, 10, 8, 3]
print(max(numbers))
print(min(numbers))
print()
max1 = numbers[0]
for number in numbers:
    if number > max1:
        max1 = number
print(max1)
