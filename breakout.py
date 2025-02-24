"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 20         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    while True:
        pause(FRAME_RATE)
        if graphics.game_start:
            graphics.run()
            graphics.play()
            if graphics.count > 2:
                graphics.window.remove(graphics.ball)
                break
            if graphics.break_number == graphics.all_bricks:
                break

    # Add the animation loop here!


if __name__ == '__main__':
    main()
