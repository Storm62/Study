vowels = ['а', 'о', 'е', 'у', 'э', 'ю', 'я']
word = input("Введите слово :")
found = []
for letter in word:
    if letter in vowels:
#        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
print(len(found))