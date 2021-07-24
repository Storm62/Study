def search4vowels (word):
    """Выводит гласные, найденные в ведённом слове"""
    vowels = set('аоеуэюяы')
    return vowels.intersection(set(word))
