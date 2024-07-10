class GameResult:
    def __init__(self, solved, strikes, balls):
        self._solved = solved
        self._strikes = strikes
        self._balls = balls

    def get_solved(self):
        return self._solved

    def get_strikes(self):
        return self._strikes

    def get_balls(self):
        return self._balls


class Game:
    _answer: str

    def set_answer(self, digits: str):
        self._check_digit_valid(digits)
        self._answer = digits

    def guess(self, digits: str):
        self._check_digit_valid(digits)
        if digits == self._answer:
            return GameResult(True, 3, 0)
        else:
            return GameResult(False, 0, 0)
    def _check_digit_valid(self, digits):
        if len(digits) != 3:
            raise TypeError()
        if not digits.isdigit():
            raise TypeError()
        if self._is_duplicated_digits(digits):
            raise TypeError()

    def _is_duplicated_digits(self, digits):
        return digits[0] == digits[1] or digits[0] == digits[2] or digits[1] == digits[2]
