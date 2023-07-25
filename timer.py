class TickTimer:
    """Simple counter object decreasing a set number until it hits 0"""
    def __init__(self):
        self.ticks_left = 0

    def set_ticks(self, ticks):
        # Set the timer
        if self.ticks_left == 0:
            self.ticks_left = ticks

    def tick(self):
        # Count down if greater 0
        if self.ticks_left > 0:
            self.ticks_left -= 1
