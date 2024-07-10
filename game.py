class Game:
    _answer: str

    def set_answer(self, param):
        if len(param) != 3:
            raise ValueError()

    def guess(self, param):
        if len(param) != 3:
            raise ValueError()
