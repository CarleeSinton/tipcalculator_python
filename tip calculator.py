print("Select tip percentage: \n"
      "1. 5% \n"
      "2. 10% \n"
      "3. 15% \n"
      "4. 20% \n"
      "5. 25% \n"
      "6. All of the above \n"
      "7. Other Amount \n")
select = input("Select percentage from 1, 2, 3, 4, 5, 6, or 7: ")

number_1 = int(input("Enter bill total: "))

if select == '7':
    number_2 = int(input("Enter other tip percentage: "))


def add(num1, num2):
    return num1 + num2


def percentage1(num1):
    return num1 * .05


def percentage2(num1):
    return num1 * .10


def percentage3(num1):
    return num1 * .15


def percentage4(num1):
    return num1 * .20


def percentage5(num1):
    return num1 * .25


def percentage_other(num1, num2):
    return num1 * (num2 / 100)


if select == '1':
    print("$", number_1, "+", "$", percentage1(number_1), "=", "$", add(number_1, percentage1(number_1)))

if select == '2':
    print("$", number_1, "+", "$", percentage2(number_1), "=", "$", add(number_1, percentage2(number_1)))

if select == '3':
    print("$", number_1, "+", "$", percentage3(number_1), "=", "$", add(number_1, percentage3(number_1)))

if select == '4':
    print("$", number_1, "+", "$", percentage4(number_1), "=", "$", add(number_1, percentage4(number_1)))

if select == '5':
    print("$", number_1, "+", "$", percentage5(number_1), "=", "$", add(number_1, percentage5(number_1)))

if select == '6':
    print("5%   ", "$", number_1, "+", "$", percentage1(number_1), "=", "$", add(number_1, percentage1(number_1)))
    print("10%  ", "$", number_1, "+", "$", percentage2(number_1), "=", "$", add(number_1, percentage2(number_1)))
    print("15%  ", "$", number_1, "+", "$", percentage3(number_1), "=", "$", add(number_1, percentage3(number_1)))
    print("20%  ", "$", number_1, "+", "$", percentage4(number_1), "=", "$", add(number_1, percentage4(number_1)))
    print("25%  ", "$", number_1, "+", "$", percentage5(number_1), "=", "$", add(number_1, percentage5(number_1)))

if select == '7':
    print("$", number_1, "+", "$", percentage_other(number_1, number_2), "=", "$", add(number_1, percentage_other(number_1, number_2)))