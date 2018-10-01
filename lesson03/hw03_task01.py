# проверка на русскую и английскую панграмму
# без использования функции string.lower()

russian_alphabet = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
russian_alphabet_capital = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ"
english_alphabet = "abcdefghijklmnopqrstuvwxyz"
english_alphabet_capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# словари со счетчиком вхождения букв
russian_dictionary = {}
english_dictionary = {}

# замена больших букв на маленькие
russian_dictionary_alias = {}
english_dictionary_alias = {}


def fill_dictionaries():
    for the_letter in russian_alphabet:
        russian_dictionary[the_letter] = 0
    for the_letter in english_alphabet:
        english_dictionary[the_letter] = 0
    i = 0
    for the_letter in russian_alphabet_capital:
        russian_dictionary_alias[the_letter] = russian_alphabet[i]
        i += 1
    i = 0
    for the_letter in english_alphabet_capital:
        english_dictionary_alias[the_letter] = english_alphabet[i]
        i += 1


def check_russian_pangram(the_phrase):
    for char in phrase:
        if char in russian_dictionary_alias:
            char = russian_dictionary_alias[char]
        if char in russian_dictionary:
            russian_dictionary[char] += 1

    not_enough_to_russian_pangram = ""

    for char, count in russian_dictionary.items():
        if count == 0:
            not_enough_to_russian_pangram += char

    if not_enough_to_russian_pangram == "":
        print("Фраза является русской панграммой")
    elif not_enough_to_russian_pangram == russian_alphabet:
        print("Фраза не содержит русских букв")
    else:
        print("До русской панграммы не хватает букв: {}".format(not_enough_to_russian_pangram))


def check_english_pangram(the_phrase):
    for char in the_phrase:
        if char in english_dictionary_alias:
            char = english_dictionary_alias[char]
        if char in english_dictionary:
            english_dictionary[char] += 1

    not_enough_to_english_pangram = ""

    for char, count in english_dictionary.items():
        if count == 0:
            not_enough_to_english_pangram += char

    if not_enough_to_english_pangram == "":
        print("Фраза является английской панграммой")
    elif not_enough_to_english_pangram == english_alphabet:
        print("Фраза не содержит английских букв")
    else:
        print("До английской панграммы не хватает букв: {}".format(not_enough_to_english_pangram))


phrase = input("Проверка на русскую и английскую панграммы. Введите фразу: ")

fill_dictionaries()
check_english_pangram(phrase)
check_russian_pangram(phrase)