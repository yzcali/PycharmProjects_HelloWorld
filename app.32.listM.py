numbers = [2, 4, 6, 5, 8, 9, 4, 8, 5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

uniques.sort()
print(uniques)
uniques.reverse()
print(uniques)

