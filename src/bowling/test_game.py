import unittest
from bowling.frame import Frame

from bowling.game import BowlingGame


class TestGames(unittest.TestCase):
    game: BowlingGame

    def setUp(self) -> None:
        self.game = BowlingGame()
        return super().setUp()

    def test_Init_when_ItShouldInitAnEmptyFrameList(self):
        game = BowlingGame()
        self.assertListEqual(game.frames, [])

    def test_AddFrame_when_FirstFrame(self):
        frame = Frame(3, 4)
        self.game.add_frame(frame)

        self.assertEqual(len(self.game.frames), 1)
        self.assertEqual(self.game.frames[0], frame)

    def test_AddFrame_when_ItShouldKeepAddOrder(self):
        frame1 = Frame(3, 4)
        frame2 = Frame(4, 5)
        frame3 = Frame(10, 0)
        self.game.add_frame(frame1)
        self.game.add_frame(frame2)
        self.game.add_frame(frame3)

        self.assertEqual(len(self.game.frames), 3)
        self.assertEqual(self.game.frames[0], frame1)
        self.assertEqual(self.game.frames[1], frame2)
        self.assertEqual(self.game.frames[2], frame3)

    def test_AddFrame_when_GameHas9(self):
        added_frames: list[Frame] = []
        for i in range(9):
            frame = Frame(1, i + 1)
            self.game.add_frame(frame)
            added_frames.append(frame)

        last_frame = Frame(3, 5)
        self.game.add_frame(last_frame)

        for i, frame in enumerate(added_frames):
            self.assertEqual(self.game.frames[i], frame)

        self.assertEqual(self.game.frames[9], last_frame)

    def test_AddFrame_when_AlreadyGameHas10(self):
        added_frames: list[Frame] = []
        for i in range(10):
            frame = Frame(0, i)
            self.game.add_frame(frame)
            added_frames.append(frame)

        with self.assertRaises(Exception) as err:
            self.game.add_frame(Frame(3, 5))

        self.assertEqual(str(err.exception), "Game already has 10 frames")

    def test_SetBonus_when_GameHasLessThan10Frames(self):
        for i in range(9):
            self.game.add_frame(Frame(0, i))

        with self.assertRaises(Exception) as err:
            self.game.set_bonus(4)

        self.assertEqual(
            str(err.exception),
            "Game must have at least 10 frames to have a bonus throw",
        )

    def test_SetBonus_when_GameHas10FramesButLastIsNotAStrikeOrSpare(self):
        for i in range(10):
            self.game.add_frame(Frame(0, i))

        with self.assertRaises(Exception) as err:
            self.game.set_bonus(4)

        self.assertEqual(
            str(err.exception),
            "Games last frame must be either a strike or spare for a bonus to be added",
        )

    def test_SetBonus_when_LastFrameIsStrike(self):
        for i in range(1, 11):
            self.game.add_frame(Frame(i, 0))

        self.game.set_bonus(4)

        self.assertEqual(self.game.frames[-1].bonus_throw, 4)

    def test_SetBonus_when_LastFrameIsSpare(self):
        for i in range(10):
            self.game.add_frame(Frame(1, i))

        self.game.set_bonus(4)

        self.assertEqual(self.game.frames[-1].bonus_throw, 4)

    def test_Score_when_NoSparesOrStrikes(self):
        for i in range(10):
            self.game.add_frame(Frame(i, 0))

        self.assertEqual(self.game.score(), 45)

    def test_Score_when_HasSpares(self):
        self.game.add_frame(Frame(3, 0))
        self.game.add_frame(Frame(4, 6))
        self.game.add_frame(Frame(4, 2))

        self.assertEqual(self.game.score(), 3 + 10 + 6 + 6)

    def test_Score_when_HasSequentialSpares(self):
        self.game.add_frame(Frame(3, 0))
        self.game.add_frame(Frame(4, 6))
        self.game.add_frame(Frame(0, 10))
        self.game.add_frame(Frame(4, 2))

        self.assertEqual(self.game.score(), 3 + 10 + 10 + 10 + 6 + 6)

    def test_Score_when_HasStrike(self):
        self.game.add_frame(Frame(3, 0))
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(4, 2))
        self.game.add_frame(Frame(7, 0))

        self.assertEqual(self.game.score(), 3 + 10 + 6 + 6 + 7 + 7)

    def test_Score_when_HasSequentialStrikes(self):
        self.game.add_frame(Frame(3, 0))  # 3
        self.game.add_frame(Frame(10, 0))  # 10 10 6
        self.game.add_frame(Frame(10, 0))  # 10 6 7
        self.game.add_frame(Frame(4, 2))  # 6
        self.game.add_frame(Frame(7, 0))  # 7

        self.assertEqual(self.game.score(), 3 + 10 + 10 + 6 + 10 + 6 + 7 + 6 + 7)


if __name__ == "__main__":
    unittest.main()
