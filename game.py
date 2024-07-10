class Game:
    _answer: str

    def set_answer(self, digits: str):
        if len(digits) != 3:
            raise ValueError()
        self._answer = digits

    def guess(self, digits: str):
        if len(digits) != 3:
            raise ValueError()
