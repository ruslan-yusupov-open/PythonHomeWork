# простейший калькулятор

# состояние калькулятора - 0 ожидание числа, 1 ожидание действия
calculatorState = 0
# введенное действие
calculatorAction = ""
# итог
sumNumber = 0

while True:
    if calculatorState == 0:
        userInputText = "введите целое число или пустую строку для выхода: "
    else:
        userInputText = "введите действие (+-*/), целое число для нового расчета или пустую строку для выхода: "

    userInput = input(userInputText)

    if userInput == "":
        break

    if calculatorState == 1 and userInput in ["+", "-", "*", "/"]:
        calculatorAction = userInput
        userInsertedNumber = 0
    else:
        if userInput.isdigit():
            userInsertedNumber = int(userInput)
        else:
            print("Неверный ввод!")
            continue

    if calculatorAction == "":
        # начало, ввели число
        userInsertedNumber = int(userInput)
        sumNumber = userInsertedNumber
        # будем ожидать действие
        calculatorState = 1

    if calculatorAction in ["+", "-", "*", "/"]:
        if calculatorState == 0:
            if calculatorAction == "+":
                sumNumber = sumNumber + userInsertedNumber
            elif calculatorAction == "-":
                sumNumber = sumNumber - userInsertedNumber
            elif calculatorAction == "*":
                sumNumber = sumNumber * userInsertedNumber
            elif calculatorAction == "/":
                if userInsertedNumber != 0:
                    sumNumber = sumNumber / userInsertedNumber
                else:
                    print("На ноль делить нельзя, извините")
                    continue

            print("Промежуточный итог равен: {}".format(sumNumber))
            calculatorAction = ""
            calculatorState = 1
        else:
            calculatorState = 0

print("Итоговый результат равен: {}".format(sumNumber))
