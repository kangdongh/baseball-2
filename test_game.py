from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def generate_question(self, question="123"):
        self.game.set_answer(question)

    def test_create(self):
        self.assertIsNotNone(self.game)

    def assert_illegal_argument_for_answer(self, digits):
        try:
            self.game.set_answer(digits)
            self.fail()
        except TypeError:
            pass

    def assert_illegal_argument_for_guess(self, digits):
        try:
            self.game.guess(digits)
            self.fail()
        except TypeError:
            pass

    def test_invalid_answer(self):
        invalid_inputs = [None, "1234", "12", "12s", "121"]
        for invalid_input in invalid_inputs:
            with self.subTest(f"Invalid_Answer_{invalid_input}"):
                self.assert_illegal_argument_for_answer(invalid_input)
            with self.subTest(f"Invalid_Guess_{invalid_input}"):
                self.assert_illegal_argument_for_guess(invalid_input)

    def _assert_matched_number(self, result, expected_balls, expected_strikes):
        self.assertIsNotNone(result)
        self.assertEqual(result.get_solved(), expected_strikes == 3)
        self.assertEqual(result.get_strikes(), expected_strikes)
        self.assertEqual(result.get_balls(), expected_balls)

    def test_correct_answer(self):
        self.generate_question("123")
        self._assert_matched_number(self.game.guess("123"), 0, 3)

    def test_no_digits_matched(self):
        self.generate_question("123")
        self._assert_matched_number(self.game.guess("456"), 0, 0)
