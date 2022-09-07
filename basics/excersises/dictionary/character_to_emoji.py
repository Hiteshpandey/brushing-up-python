message = input('Enter text with emoji')

# split string by spaces
words = message.split(' ')

emojis = {
    ":)" : '😊',
    ":(" : '🙁'
}

output = ''
for word in words:
    # If the character/word not in emoji map, we return the word as a default value
    output += emojis.get(word, word)

print(output)
