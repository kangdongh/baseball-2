from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_create(self):
        self.assertIsNotNone(self.game)

    def test_invalid_answer(self):
        self.assert_illegal_argument_for_answer(None)
        self.assert_illegal_argument_for_answer("1234")
        self.assert_illegal_argument_for_answer("12")
        self.assert_illegal_argument_for_answer("12s")

    def test_invalid_guess(self):
        self.assert_illegal_argument_for_guess(None)
        self.assert_illegal_argument_for_guess("1234")
        self.assert_illegal_argument_for_guess("12")
        self.assert_illegal_argument_for_guess("12s")

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
