class Number:

    def __init__(self, number: int) -> None:
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: int):
        self._number = number

    def __add__(self, other: int) -> int:
        return self._number + other

    def __sub__(self, other: int) -> int:
        return self._number - other

    def __mul__(self, other: int) -> int:
        return self._number * other

    def __div__(self, other) -> int:
        return int(self._number / other)

