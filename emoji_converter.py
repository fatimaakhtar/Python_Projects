message = input("Enter your message: ")
words = message.split(' ')
emojis ={
    ":)" :"😊",
    ":(" : "😔",
    "OwO" : "😯"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "

print(output)