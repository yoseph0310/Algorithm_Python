class Calculator:
    def __init__(self, first_num: int, second_num: int):
        self._first_num = first_num
        self._second_num = second_num
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
        self._result = self._first_num + self._second_num

    def sub(self) -> None:
        self._result = self._first_num - self._second_num

    def mul(self) -> None:
        self._result = self._first_num * self._second_num

    def div(self) -> None:
        self._result = self._first_num / self._second_num
