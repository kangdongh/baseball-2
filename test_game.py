from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_create(self):
        self.assertIsNotNone(self.game)

    def test_wrong_type_answer(self):
        self.assert_illegal_argument_for_answer(None)

    def test_wrong_type_guess(self):
        self.assert_illegal_argument_for_guess(None)

    def test_wrong_answer_4digits(self):
        self.assert_illegal_argument_for_answer("1234")

    def test_wrong_answer_2digits(self):
        self.assert_illegal_argument_for_answer("12")

    def test_wrong_guess_4digits(self):
        self.assert_illegal_argument_for_guess("1234")

    def test_wrong_guess_2digits(self):
        self.assert_illegal_argument_for_guess("12")

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
