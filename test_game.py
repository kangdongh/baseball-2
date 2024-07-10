from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_create(self):
        self.assertIsNotNone(self.game)

    def test_invalid_answer(self):
        invalid_inputs = [None, "1234", "12", "12s", "121"]
        for invalid_input in invalid_inputs:
            with self.subTest(f"Invalid_Answer_{invalid_input}"):
                self.assert_illegal_argument_for_answer(invalid_input)
            with self.subTest(f"Invalid_Guess_{invalid_input}"):
                self.assert_illegal_argument_for_guess(invalid_input)

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
