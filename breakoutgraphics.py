"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 5        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT, x=window_width/2-PADDLE_WIDTH/2, y=window_height-PADDLE_OFFSET)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2, x=window_width/2-BALL_RADIUS, y=window_height/2-BALL_RADIUS)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball)
        self.dx = 0
        self.dy = 0
        # Default initial velocity for the ball

        # Initialize our mouse listeners
        self.game_start = False
        onmouseclicked(self.click)
        onmousemoved(self.catch)

        self.count = 0
        self.all_bricks = BRICK_ROWS*BRICK_COLS
        self.break_number = 0 #  Number of the bricks which are hit and removed

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=j*(BRICK_WIDTH+BRICK_SPACING), y=BRICK_OFFSET+i*(BRICK_HEIGHT+BRICK_SPACING))
                self.brick.filled = True
                if i%10 == 0 or i%10 == 1:
                    self.brick.fill_color = 'red'
                elif i%10 == 2 or i%10 == 3:
                    self.brick.fill_color = 'orange'
                elif i%10 == 4 or i % 10 == 5:
                    self.brick.fill_color = 'yellow'
                elif i%10 == 6 or i%10 == 7:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)

    def click(self, event):
        if not self.game_start:
            self.game_start = True
            self.dx=random.randint(1, MAX_X_SPEED)
            if (random.random() > 0.5):
                self.dx = -self.dx
            self.dy = INITIAL_Y_SPEED


    def run(self):
        self.ball.move(self.dx, self.dy)
        if self.ball.x < 0:
            self.dx = -self.dx
        elif self.ball.x > self.window.width:
            self.dx = -self.dx
        if self.ball.y < 0:
            self.dy = -self.dy
        elif self.ball.y > self.window.height:
            self.count += 1
            self.ball.x=self.window.width/2-BALL_RADIUS  # For initial ball reset
            self.ball.y=self.window.height/2-BALL_RADIUS
            self.dx = 0
            self.dy = 0
            self.game_start = False

            # self.dy = -self.dy


    def catch(self, event):  # for paddle
        if 0 < event.x < self.window.width-PADDLE_WIDTH:
            self.paddle.x = event.x - PADDLE_WIDTH/2
        elif event.x <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = self.window.width-PADDLE_WIDTH


    def play(self):
        for i in range(2):
            for j in range(2):
                obj = self.window.get_object_at(self.ball.x+i*2*BALL_RADIUS, self.ball.y+j*2*BALL_RADIUS)
                if obj is not None:
                    if obj is not self.paddle:
                        self.window.remove(obj)
                        self.break_number += 1
                    self.dy = -self.dy
                    return


                    # obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
                    # obj2 = self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y)
                    # obj3 = self.window.get_object_at(self.ball.x, self.ball.y+2*BALL_RADIUS)
                    # obj4 = self.window.get_object_at(self.ball.x+2*BALL_RADIUS, self.ball.y+2*BALL_RADIUS)
                    # if obj1 is not None and obj1 is not self.paddle:
                    #     self.window.remove(obj1)
                    # if obj1 is not None and obj1 is not self.paddle:
                    #     self.window.remove(obj1)
                    # if obj1 is not None and obj1 is not self.paddle:
                    #     self.window.remove(obj1)
                    # if obj1 is not None and obj1 is not self.paddle:
                    #     self.window.remove(obj1)