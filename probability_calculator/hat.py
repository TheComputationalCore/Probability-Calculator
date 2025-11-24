import random


class Hat:
    """
    A hat that contains balls of various colors.
    Allows drawing balls at random without replacement.
    """

    def __init__(self, **kwargs):
        """
        Initialize the hat with keyword arguments where each key is a color
        and each value is a count of balls of that color.

        Example:
            Hat(red=3, blue=2)
        """
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        """
        Draw a number of balls at random without replacement.
        If num_balls >= total contents, return all balls.
        """
        if num_balls >= len(self.contents):
            drawn = list(self.contents)
            self.contents.clear()
            return drawn

        drawn = random.sample(self.contents, num_balls)

        for ball in drawn:
            self.contents.remove(ball)

        return drawn

    def __repr__(self):
        return f"Hat({self.contents})"
