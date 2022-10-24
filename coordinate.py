X_STEP = 2  # use 2 steps on the physical x-axis as 1 step in snake game so the color block is a square
Y_STEP = 1

class Coordinate():
	def __init__(self, x, y):                   # receive a coordinate (x, y), create a new Coordinate instance
		self.x = x
		self.y = y
		self.dir_ = [(0, Y_STEP), (0, -Y_STEP), (-X_STEP, 0), (X_STEP, 0)]

	def __call__(self, *args, **kwargs):        # return current head position
		return self.x, self.y

	def __add__(self, right):
		return Coordinate(self.x+right.x, self.y+right.y)

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def left(self):
		return Coordinate(self.x - X_STEP, self.y)

	def right(self):
		return Coordinate(self.x + X_STEP, self.y)

	def up(self):
		return Coordinate(self.x, self.y - Y_STEP)

	def down(self):
		return Coordinate(self.x, self.y + Y_STEP)

	def next(self, dir_:int):
		return Coordinate(self.x+self.dir_[dir_][0], self.y+self.dir_[dir_][1])