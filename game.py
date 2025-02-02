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
        return self._get_result_from_counts(
            self._get_strikes_count(digits),
            self._get_balls_count(digits)
        )

    def _get_result_from_counts(self, strikes_count, balls_count):
        return GameResult(strikes_count == 3, strikes_count, balls_count)

    def _get_strikes_count(self, digits):
        strikes_count = 0
        for i in range(3):
            if digits[i] == self._answer[i]:
                strikes_count += 1
        return strikes_count

    def _get_balls_count(self, digits):
        balls_count = 0
        for i in range(3):
            if -1 < self._answer.find(digits[i]) != i:
                balls_count += 1
        return balls_count

    def _check_digit_valid(self, digits):
        if len(digits) != 3:
            raise TypeError()
        if not digits.isdigit():
            raise TypeError()
        if self._is_duplicated_digits(digits):
            raise TypeError()

    def _is_duplicated_digits(self, digits):
        return digits[0] == digits[1] or digits[0] == digits[2] or digits[1] == digits[2]
