from PtuStudy.Number import Number

class Calculator2:
    def __init__(self, first_num: Number, second_num: Number):
        self._first_num = first_num.number
        self._second_num = second_num.number
        self._result = 0

    @property
    def first_num(self) -> int:
        return self._first_num

    @first_num.setter
    def first_num(self, first_num: int) -> None:
        self._first_num = first_num

    @property
    def second_num(self) -> int:
        return self._second_num

    @second_num.setter
    def second_num(self, second_num: int) -> None:
        self._second_num = second_num

    @property
    def result(self) -> int:
        return self._result

    def add(self) -> None:
        self._result = self._first_num.__add__(self._second_num)

    def sub(self) -> None:
        self._result = self._first_num.__sub__(self._second_num)

    def mul(self) -> None:
        self._result = self._first_num.__mul__(self._second_num)

    def div(self) -> None:
        self._result = self._first_num.__div__(self._second_num)
