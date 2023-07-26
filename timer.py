class TickTimer:
    """Simple counter object decreasing a set number until it hits 0"""

    def __init__(self, ticks_left=0):
        self.ticks_left = ticks_left

    def set_ticks(self, ticks):
        """Set the timer if it's not already set."""
        if self.ticks_left == 0:
            self.ticks_left = ticks

    def tick(self):
        """Decrease the timer by 1 if greater than 0."""
        if self.ticks_left > 0:
            self.ticks_left -= 1

    def modify(self, modifier):
        """Modify the timer by adding the given modifier, but don't let it go below 0."""
        self.ticks_left = max(0, self.ticks_left + modifier)

    def get_seconds(self):
        """Get the number of seconds remaining in the timer."""
        return self.ticks_left // 60
