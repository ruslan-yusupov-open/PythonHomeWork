# викторина, вопросы заданы в виде массива, поддерживается несколько вариантов ответа
# примечаение: если нужна производительность, список ответов эффективнее задать словарём

questions = [
    {
        "question": "сколько будет два плюс два",
        "answers": ["4", "четыре"]
    },
    {
        "question": "какого цвета может быть светофор",
        "answers": ["зеленый", "желтый", "красный"]
    },
    {
        "question": "назовите день недели",
        "answers": ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    },
]

for question in questions:
    while input("Внимание, вопрос: {}? ".format(question["question"])) not in question["answers"]:
        print("Неверно! Попробуйте ещё раз!")
    print("Верно!")
