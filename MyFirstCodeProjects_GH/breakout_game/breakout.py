"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is a game that users move the paddle to delete bricks.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    This game will start when users click mouse.
    Then users move the paddle to bounce the ball.
    Users have 3 lives.
    When the ball reach the bottom of window, users lose one life,
    and the game will restart.
    If users lose 3 lives or users delete all bricks,
    the game will stop.
    """
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    # Add animation loop here!
    while True:
        # pause
        pause(FRAME_RATE)
        # update
        vx = graphics.get_dx()
        vy = graphics.get_dy()
        graphics.ball.move(vx, vy)

        # if ball reaches the bottom of window, users will lose one life and the game restarts.
        if graphics.ball_out():
            lives -= 1
            if lives > 0:
                graphics.ball_restart()
            # if users have no life, the game will stop
            else:
                break

        # check
        # If ball hit bricks or the paddle, the ball will bounce. If ball hits bricks, bricks will be deleted.
        graphics.ball_hit_obj()
        if graphics.win_game():  # If users delete all bricks, the game will stop
            break
        # when ball reaches the left side or the right side or the top of window, the ball will bounce.
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window_width:
            graphics.set_dx(vx)
        if graphics.ball.y <= 0:
            graphics.set_dy(vy)


if __name__ == '__main__':
    main()
