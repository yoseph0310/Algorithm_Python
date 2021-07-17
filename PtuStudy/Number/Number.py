class Number:

    def __init__(self, number: int) -> None:
        self._number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number: int):
        self._number = number
