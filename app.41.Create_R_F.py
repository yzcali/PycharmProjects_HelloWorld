def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😔",  # for emojis Win and press(. )
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
# result = emoji_converter(message) we can make it shorter
# print(result)
print(emoji_converter(message))
