from unittest import TestCase

from game import Game, GameResult


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

    def test_correct_answer(self):
        self.game.set_answer("123")
        result: GameResult = self.game.guess("123")
        self.assertIsNotNone(result)
        self.assertEqual(result.get_solved(), True)
        self.assertEqual(result.get_strikes(), 3)
        self.assertEqual(result.get_balls(), 0)

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
