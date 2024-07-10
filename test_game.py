from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        self.game = Game()

    def test_create(self):
        self.assertIsNotNone(self.game)

    def test_wrong_type_answer(self):
        self.assertRaises(TypeError, self.game.set_answer, None)

    def test_wrong_type_guess(self):
        self.assertRaises(TypeError, self.game.guess, None)

    def test_wrong_answer_4digits(self):
        self.assertRaises(ValueError, self.game.set_answer, "1234")

    def test_wrong_answer_2digits(self):
        self.assertRaises(ValueError, self.game.set_answer, "12")

    def test_wrong_guess_4digits(self):
        self.game.set_answer("123")
        self.assertRaises(ValueError, self.game.guess, "1234")

    def test_wrong_guess_2digits(self):
        self.game.set_answer("123")
        self.assertRaises(ValueError, self.game.guess, "12")
