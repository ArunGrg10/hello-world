customer = {
    "name": "Arun",
    "email": "lmarungrg10@gmail.com",
    "age": "26",
    "verified": True
}                #each key should be unique.
customer["name"] = 'hello world'
customer["file"] = 'closed '
print(customer["name"])
print(customer.get("email"))
print(customer.get("AGE"))         #"none" represents absence of value in the terminal
print(customer.get("birthdate", "22nd Dec,1996"))
print(customer.get("file"))

#PROGRAM
phone = input('phone: ')
word_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "Six"

}
output = ''
for n in phone:
    output += word_mapping.get(n, "?????") + " "
print(output)

# Split and Emojies

words = input(">")
print(words.split(' '))
emojies = {
    ":)": "😂",
    ":(": "😞"
}
output = ''
for word in words:
    output += emojies.get(word, word) + " "

print(output)


