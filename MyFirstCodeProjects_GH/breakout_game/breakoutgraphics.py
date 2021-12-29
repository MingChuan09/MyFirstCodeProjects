"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

This program construct the element of the breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window_width-self.paddle.width)/2,
                        y=(self.window_height-self.paddle.height-paddle_offset))

        # Draw bricks
        change_time = brick_rows / 5
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick_x = j * (brick_width + brick_spacing)
                brick_y = brick_offset + i * (brick_height + brick_spacing)
                self.brick = GRect(width=brick_width, height=brick_height, x=brick_x, y=brick_y)
                self.brick.filled = True
                if i < 1 * change_time:
                    self.brick.fill_color = 'red'
                elif i < 2 * change_time:
                    self.brick.fill_color = 'orange'
                elif i < 3 * change_time:
                    self.brick.fill_color = 'yellow'
                elif i < 4 * change_time:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)

        # Center a filled ball in the graphical window
        self.ball_org_x = self.window_width / 2 - ball_radius
        self.ball_org_y = self.window_height / 2 - ball_radius
        self.ball = GOval(width=ball_radius*2, height=ball_radius*2, x=self.ball_org_x, y=self.ball_org_y)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        self.same_round = False             # like a switch to identify if the game starts

        onmouseclicked(self.start_game)
        onmousemoved(self.reset_paddle)

        self.ball_hit_obj()

        if self.ball_out():
            self.ball_restart()

        self.brick_number = 0      # the number of bricks deleted
        self.total_brick = brick_cols*brick_rows   # the total bricks number

    def win_game(self):
        """
        When the bricks are all deleted
        :return: True
        """
        win = self.brick_number == self.total_brick
        return win

    def ball_hit_obj(self):
        """
        Check the 4 angle of the ball.
        If the ball hit paddle, the ball will bounce.
        If the ball hit bricks, the bricks will be deleted and the ball will bounce.
        """
        point_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        point_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        point_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        point_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        if point_1 is not None:
            if point_1 is not self.paddle:
                self.window.remove(point_1)
                self.brick_number += 1
                self.__dy *= -1
            elif self.__dy > 0:              # to avoid the ball sticks at the paddle
                self.__dy *= -1
        elif point_2 is not None:
            if point_2 is not self.paddle:
                self.window.remove(point_2)
                self.brick_number += 1
                self.__dy *= -1
            elif self.__dy > 0:
                self.__dy *= -1
        elif point_3 is not None:
            if point_3 is not self.paddle:
                self.window.remove(point_3)
                self.brick_number += 1
                self.__dy *= -1
            elif self.__dy > 0:
                self.__dy *= -1
        elif point_4 is not None:
            if point_4 is not self.paddle:
                self.window.remove(point_4)
                self.brick_number += 1
                self.__dy *= -1
            elif self.__dy > 0:
                self.__dy *= -1

    def ball_restart(self):
        """
        If ball reaches the bottom of window, and the game is not over,
        the game will restart.
        """
        self.window.remove(self.ball)
        self.window.add(self.ball, x=self.ball_org_x, y=self.ball_org_y)
        self.same_round = False                        # change the switch to the default value
        self.__dx = 0                                  # change the velocity to the default value
        self.__dy = 0

    def ball_out(self):
        """
        If ball reaches the bottom of window.
        :return: True , when the ball reaches the bottom of window.
        """
        out_of_window = self.ball.y + self.ball.height >= self.window_height
        return out_of_window

    def reset_paddle(self, event):
        """
        :param event: the position of the mouse moves
        :return: the middle of the paddle will follow the mouse
        """
        self.paddle.x = event.x - self.paddle.width / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif (self.paddle.x + self.paddle.width) >= self.window_width:
            self.paddle.x = self.window_width - self.paddle.width

    def start_game(self, mouse):
        """
        when users click mouse, the game starts.
        """
        if not self.same_round:
            self.same_round = True      # when the game start, clicking mouse will not affect the game
            self.set_ball_velocity()

    def set_ball_velocity(self):
        """
        To define the ball velocity.
        """
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # setter
    def set_dx(self, vx):
        self.__dx *= -1

    # setter
    def set_dy(self, vy):
        self.__dy *= -1

    # getter
    def get_dx(self):
        return self.__dx

    # getter
    def get_dy(self):
        return self.__dy
