import curses
from coordinate import Coordinate
from Snake import Snake
from time import sleep
import UI
from random import randint

# size of the window
HEIGHT = 22
WIDTH = 44

# basic boundary of the window
LEFT_BOUND = 1
RIGHT_BOUND = WIDTH-2
UP_BOUND = 0
DOWN_BOUND = HEIGHT-1

class MainGame:
	def init(self):
		"""
		Initialize the main window
		:return:
		"""
		UI.init(self.stdscr)
		self.window = UI.Window(self.stdscr)
		self.window.set_size(HEIGHT, WIDTH)      # Set the fixed window size
		self.window.draw_frame()             # Draw the initial frame(game boarder)
		self.snake = Snake(Coordinate(WIDTH//2, HEIGHT//2), LEFT_BOUND, RIGHT_BOUND, UP_BOUND, DOWN_BOUND)
		self.window.draw_snake(self.snake)

	def generate_food(self) -> Coordinate:
		"""
		Generate a postion of food.
		:return:
		"""
		x = randint(LEFT_BOUND+1, RIGHT_BOUND-1)
		y = randint(UP_BOUND+1, DOWN_BOUND-1)
		x -= x%2            # make sure the position is correct
		while self.snake.cover(Coordinate(x, y)):
			x = randint(LEFT_BOUND + 1, RIGHT_BOUND - 1)
			y = randint(UP_BOUND + 1, DOWN_BOUND - 1)
			x -= x % 2
		return Coordinate(x, y)

	def fail(self):
		"""
		Output information after the player has failed.
		:return:
		"""
		sleep(0.5)
		self.window.clear()
		self.window.draw_text(Coordinate(1, 1), 'You DIED!', 'RED', bold=True)
		self.window.draw_text(Coordinate(1, 2), f'Your snake is fed to the length of {self.snake.length()}!', 'YELLOW', bold=True)
		self.window.draw_text(Coordinate(1, 4), 'Quit in 5 secs', 'RED', bold=False)
		self.window.refresh()
		sleep(5)

	def game_loop(self):
		"""
		The main game loop
		:return:
		"""
		food_pos = self.generate_food()
		while True:
			self.window.draw_node(food_pos, 'RED')
			key = self.stdscr.getch()           # Get keyboard input from the player
			if key == ord('q'):                 # Quit the game when the user presses 'Q'
				break
			if key in [curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT]:
				dir_ = key-curses.KEY_DOWN              # change the direction into a number form
				self.snake.set_direction(dir_)          # change the snake's direction
			self.snake.move(food_pos)                           # make the snake move forward for 1 unit of distance
			if self.snake.fail():
				self.fail()
				break
			if self.snake.head_position() == food_pos:      # when the food is eaten, generate a new one
				food_pos = self.generate_food()

			# self.window.draw_node(food_pos, 'RED')
			self.window.draw_snake(self.snake)          # redraw the snake on the screen

	def __call__(self, stdscr):
		"""
		the main control function for the game
		:param stdscr:
		:return:
		"""
		if curses.LINES < HEIGHT or curses.COLS < WIDTH:              # Exit when terminal size is too small
			stdscr.addstr(1, 1, 'Your terminal window size is too small.')
			stdscr.addstr(2, 1, 'The game needs at least 22 lines and 44 columns.')
			stdscr.addstr(3, 1, f'Cuurent Size: {curses.LINES} * {curses.COLS}')
			stdscr.addstr(4, 1, 'Press any key to quit.')
			stdscr.getch()
			return
		self.stdscr = stdscr
		self.init()         # Set and draw the initial window
		self.game_loop()    # Run the game


if __name__ == '__main__':
	game = MainGame()
	curses.wrapper(game)