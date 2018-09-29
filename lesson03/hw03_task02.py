# игра поле чудес

the_question = "что дают коровы?"
word_to_guess = "молоко"

word_letters_dict = {}
already_used_letters_dict = {}


def fill_word_letters_dict():
    for c in word_to_guess:
        word_letters_dict[c] = 1


def show_word():
    the_word = ""
    for c in word_to_guess:
        if c in already_used_letters_dict:
            the_word += c
        else:
            the_word += '_'
        the_word += ' '
    return the_word


def check_letter_already_used(the_letter):
    return the_letter in already_used_letters_dict


def check_if_letter_correct(the_letter):
    return the_letter in word_letters_dict


def ask_letter():
    global unknown_letters_count
    the_letter = input("Отгадываем слово: {}, введите букву: ".format(show_word()))
    try:
        if check_letter_already_used(the_letter):
            raise ValueError("вы уже вводили эту букву!")
        if len(the_letter) != 1:
            raise ValueError("введите только одну букву!")

        if check_if_letter_correct(the_letter):
            print("есть такая буква в этом слове!")
            unknown_letters_count -= 1
        else:
            print("такой буквы нет!")
        already_used_letters_dict[the_letter] = 1

    except ValueError as val_error:
        print(val_error)


fill_word_letters_dict()

unknown_letters_count = len(word_letters_dict)

print("Внимание, вопрос: {}".format(the_question))

while unknown_letters_count > 0:
    ask_letter()

print("Поздравляем, вы угадали слово {}".format(word_to_guess))
