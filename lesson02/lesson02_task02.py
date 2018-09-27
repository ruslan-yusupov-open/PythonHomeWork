# Есть текст, который лежит в string. Надо убрать из него все знаки препинания, и найти сколько раз встречается
# каждое слово. Вывести TOP-10 самых встречающихся слов, с указанием, какое это слово и сколько раз оно встретилось.

# под словом мы понимаем последовательность любых строчных и прописных латинских букв и цифр
testText = """Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, 
totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. 
Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, 
sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. 
Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, 
sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. 
Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, 
nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea 
voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"""

# составляем слово
word = ""
# словарь и частота встречающихся слов
dictionary = {}

# тут напрашивается регулярка, но, я думаю, это не спортивно
# без регулярки более читаемо это бы выглядело как c in "abcd ... 789", но это медленно
# так делать тоже не хорошо, т.к. зависит от таблицы символов
for c in testText:
    if (ord(c) in range(ord('a'), ord('z'))
            or ord(c) in range(ord('A'), ord('Z'))
            or ord(c) in range(ord('0'), ord('9'))):
        word += c
    else:
        if len(word) > 0:
            if word in dictionary:
                dictionary[word] += 1
            else:
                dictionary[word] = 1

            word = ""

print("Топ 10 встречающихся слов:")

i = 1
# самый вменяемо выглядищий метод сортировки по значению, который я нашел
for word in sorted(dictionary, key=lambda x: dictionary[x], reverse=True)[0:10]:
    print("{i}. Слово: '{word}', встречается раз: {count}".format(i=i, word=word, count=dictionary[word]))
    i += 1
