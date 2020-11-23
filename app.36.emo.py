message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😔",  # for emojis Win and press(. )
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# print(words)  # ali gel ---> ['ali', 'gel']
