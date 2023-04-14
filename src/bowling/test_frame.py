import unittest

from bowling.frame import Frame


class TestFrames(unittest.TestCase):
    def test_Init_when_ScoreSumsToTen(self):
        frame = Frame(5, 5)
        self.assertEqual(frame.first_throw, 5)
        self.assertEqual(frame.second_throw, 5)

    def test_Init_when_ScoreSumsToLessThanTen(self):
        frame = Frame(3, 4)
        self.assertEqual(frame.first_throw, 3)
        self.assertEqual(frame.second_throw, 4)

    def test_Init_when_ScoreSumsToMoreThanTen(self):
        with self.assertRaises(Exception) as err:
            Frame(6, 5)

        self.assertEqual(
            str(err.exception),
            "First + Second throws should not equal to more than ten",
        )

    def test_Score(self):
        self.assertEqual(Frame(3, 6).score(), 9)
        self.assertEqual(Frame(3, 4).score(), 7)
        self.assertEqual(Frame(2, 8).score(), 10)
        self.assertEqual(Frame(10, 0).score(), 10)

    def test_IsStrike_when_FirstThrowIs10(self):
        frame = Frame(first_throw=10, second_throw=0)
        self.assertTrue(frame.is_strike())

    def test_IsStrike_when_SecondThrowIs10(self):
        frame = Frame(first_throw=0, second_throw=10)
        self.assertFalse(frame.is_strike())

    def test_IsStrike_when_ScoreIsLessThan10(self):
        frame = Frame(first_throw=2, second_throw=3)
        self.assertFalse(frame.is_strike())

    def test_IsSpare_when_ScoreIs10(self):
        frame = Frame(first_throw=2, second_throw=8)
        self.assertTrue(frame.is_spare())

    def test_IsSpare_when_ItIsStrike(self):
        frame = Frame(first_throw=10, second_throw=0)
        self.assertFalse(frame.is_spare())

    def test_IsSpare_when_ScoreIsLessThan10(self):
        frame = Frame(first_throw=6, second_throw=1)
        self.assertFalse(frame.is_spare())


if __name__ == "__main__":
    unittest.main()
