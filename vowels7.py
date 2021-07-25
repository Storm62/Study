vowels = set('аоеуэюяы')
word = input("Введите слово: ")

found = vowels.intersection(set(word))

for vowels in found:
    print(vowels)