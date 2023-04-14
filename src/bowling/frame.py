from bowling.contants import MAX_SCORE


class Frame:
    _first_throw: int
    _second_throw: int

    _bonus_throw: int | None = None

    def __init__(self, first_throw: int, second_throw: int) -> None:
        if first_throw + second_throw > MAX_SCORE:
            raise Exception("First + Second throws should not equal to more than ten")

        self._first_throw = first_throw
        self._second_throw = second_throw

    @property
    def first_throw(self):
        return self._first_throw

    @property
    def second_throw(self):
        return self._second_throw

    @property
    def bonus_throw(self):
        return self._bonus_throw

    def score(self) -> int:
        """The score of a single frame
        It doesn't take into account when the frame is a strike, spare or bonus, the game should handle those
        """

        return self._first_throw + self._second_throw

    def is_strike(self) -> bool:
        """Return whether the frame is a strike or not"""

        return self._first_throw == MAX_SCORE

    def is_spare(self) -> bool:
        """Return whether the frame is a spare or not"""

        return not self.is_strike() and self.score() == MAX_SCORE

    def set_bonus_throw(self, bonus_throw: int):
        """Adds a bonus throw to this frame"""

        if bonus_throw > MAX_SCORE:
            raise Exception("A bonus can only have a max of 10 points")

        if not self.is_spare() and not self.is_strike():
            raise Exception(
                "A bonus can only be set when frame has either a spare or strike"
            )

        self._bonus_throw = bonus_throw
