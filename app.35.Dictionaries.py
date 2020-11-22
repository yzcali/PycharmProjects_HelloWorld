# a costumer has a bunch of attributes like name, email, phone etc
costumer = {
    "name": "john Smith ",
    "age": 30,
    "is _verified": True
}
# {} values are uniques so we cant do duplicate

print(costumer["name"])
print(costumer.get("birthdate"))  # None
print(costumer.get("birthdate", " 01-jan-84"))  # 01-jan-84 bu sekilde ekleme yapabiliriz
print()

# exercise : Phone : 1234 like  we digit number translate the words one two three four
phone = input("Phone: ")
digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""
for ch in phone:
    output += digit_mapping.get(ch, "!")+" "
print(output)
