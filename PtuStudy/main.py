import random as rand
import typing

from PtuStudy.Calculator import Calculator
from PtuStudy.Calculator import Calculator2
from PtuStudy.Number import Number

first_num: Number = Number(2)
second_num: Number = Number(3)

calculator: Calculator = Calculator(
    first_num=first_num,
    second_num=second_num,
)

calculator2: Calculator2 = Calculator2(
    first_num=first_num,
    second_num=second_num,
)

# calculator2.add()
# print(calculator2.result)

calculator.add()
print(calculator.result)

# calculator2.mul()
# print(calculator.result)

calculator.mul()
print(calculator.result)



calculator.div()
print(calculator.result)

# calculator2.sub()
# print(calculator.result)

calculator.sub()
print(calculator.result)

print(first_num == calculator.result)

number_list: typing.List = list()

for _ in range(10):
    number_list.append(
        Number(
            number=rand.randint(0, 1000)
        ).number
    )

print(number_list)
number_list.sort()
print(number_list)





