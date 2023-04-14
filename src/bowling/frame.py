MAX_SCORE = 10


class Frame:
    first_throw: int
    second_throw: int

    def __init__(self, first_throw: int, second_throw: int) -> None:
        if first_throw + second_throw > MAX_SCORE:
            raise Exception("First + Second throws should not equal to more than ten")

        self.first_throw = first_throw
        self.second_throw = second_throw

    def score(self) -> int:
        """The score of a single frame"""

        return self.first_throw + self.second_throw

    def is_strike(self) -> bool:
        """Return whether the frame is a strike or not"""

        return self.first_throw == MAX_SCORE

    def is_spare(self) -> bool:
        """Return whether the frame is a spare or not"""

        return self.score() == 10 and self.first_throw < MAX_SCORE

    def is_last_frame(self) -> bool:
        """Return whether the frame is a last frame of the game"""
        # To be implemented
        pass

    def bonus(self) -> int:
        """Bonus throw"""
        # To be implemented
        pass
