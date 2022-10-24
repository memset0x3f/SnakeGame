import curses
from coordinate import Coordinate
from Snake import Snake

'''
Color1: fr: BLACK, bg: BLACK
Color2: fr: WHITE, bg: WHITE
Color3: fr: RED, bg:RED
Color4: fr: CYAN, bg:CYAN
Color5: fr: GREEN, bg:GREEN
Color6: fr: RED, bg: BLACK
Color7: fr: Yellow, bg: BLACK
'''

def init(stdscr):
	"""
	initialize some color pairs and some curses settings.
	:return:
	"""
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_RED)
	curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_CYAN)
	curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_GREEN)
	curses.init_pair(6, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.noecho()             # Turn off terminal echo
	curses.curs_set(0)          # Remove the curser from the window
	stdscr.timeout(300)

class Window:
	def __init__(self, screen):
		"""
		Initialize a window to process the drawing
		:param screen:
		"""
		self.stdscr = screen
		self.height = curses.LINES
		self.width = curses.COLS
		self.color_blocks = {'BLACK':1, 'WHITE':2, 'RED':3, 'CYAN':4, 'GREEN':5}
		self.colors = {'RED': 6, 'YELLOW': 7}

	def set_size(self, height, width):
		"""
		set the window's size
		:param height:
		:param width:
		:return:
		"""
		self.height = height
		self.width = width

	def clear(self):
		"""
		Clear all the content in the current window
		:return:
		"""
		self.stdscr.clear()
		self.stdscr.refresh()

	def refresh(self):
		"""
		Refresh the window
		:return:
		"""
		self.stdscr.refresh()

	def draw_text(self, pos, text, color, bold=False):
		"""
		Display a single line of text on the screen at pos.
		:param pos: the start position of the text(Coordinate instance).
		:param text: the text to be printed
		:param color: the color of drawing(str), options: RED, YELLOW
		:param bold: set the text to bold style if bold=True
		:return:
		"""
		if color not in self.colors:
			raise IndexError('Invalid Color.')
		self.stdscr.addstr(pos.y, pos.x, text, curses.color_pair(self.colors[color]) | (bold*curses.A_BOLD))
		self.stdscr.refresh()

	def draw_node(self, pos, color):
		"""
		Draw a single node on the screen at pos.
		:param pos: the start position of the node(Coordinate instance).
		:param color: the color of drawing(str), options: BLACK, WHITE, RED, GREEN, CYAN.
		:return:
		"""
		if color not in self.color_blocks:
			raise IndexError('Invalid Color.')
		self.stdscr.addstr(pos.y, pos.x, "  ", curses.color_pair(self.color_blocks[color]))    # add 2 spaces to form a square

	def draw_frame(self):
		"""
		Draw the boarder of the game
		:return:
		"""
		for i in range(2, self.width-2, 2):
			for j in range(1, self.height-1):
				self.draw_node(Coordinate(i, j), 'WHITE')
		for i in range(self.height):
			self.draw_node(Coordinate(0, i), 'CYAN')
			self.draw_node(Coordinate(self.width-2, i), 'CYAN')
		for i in range(0, self.width, 2):
			self.draw_node(Coordinate(i, 0), 'CYAN')
			self.draw_node(Coordinate(i, self.height-1), 'CYAN')

	def draw_snake(self, snake: Snake):
		"""
		Draw the snake on the terminal screen stdscr.
		:param stdscr:
		:param snake: A Snake instance
		:return:
		"""
		self.draw_frame()
		self.draw_node(snake.nodes[0], 'GREEN')
		for node in snake.nodes[1:]:
			self.draw_node(node, 'BLACK')
