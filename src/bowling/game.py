from bowling.contants import MAX_NUM_FRAMES
from bowling.frame import Frame


class BowlingGame:
    _frames: list[Frame]

    def __init__(self) -> None:
        self._frames = []

    @property
    def frames(self):
        return self._frames

    def add_frame(self, frame: Frame):
        """Add a frame to the game"""

        if len(self.frames) == MAX_NUM_FRAMES:
            raise Exception("Game already has 10 frames")

        self.frames.append(frame)

    def set_bonus(self, first_throw: int, second_throw: int = 0):
        """The the bonus throw
        I didn't find a use for the second_throw value
        """

        if len(self.frames) < MAX_NUM_FRAMES:
            raise Exception("Game must have at least 10 frames to have a bonus throw")

        last_frame = self.frames[-1]

        if not last_frame.is_strike() and not last_frame.is_spare():
            raise Exception(
                "Games last frame must be either a strike or spare for a bonus to be added"
            )

        last_frame.set_bonus_throw(first_throw)

    def score(self) -> int:
        """Get the score from the game"""
        # To be implemented
        pass

    def is_next_frame_bonus(self) -> bool:
        """Get if the next frame is bonus"""
        # To be implemented
        pass
