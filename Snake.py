from coordinate import Coordinate

'''
KEY_VALUE: KEY_DOWN:258, KEY_UP:259, KEY_LEFT:260, KEY_RIGHT:261
directions: 0-down, 1-up, 2-left, 3-right
'''

class Snake:
	def __init__(self, pos: Coordinate, left_bound, right_bound, up_bound, down_bound):
		"""
		Recieve a Coordinate instanceand set the initial position of snake to it.
		:param pos:
		"""
		self.dir = 2                        # current direction
		self.nodes = [pos.left(), pos, pos.right()]  # nodes(list) stores every position of nodes of the snake's body
		# bound cannot be crossed or even touched
		self.left_bound = left_bound
		self.right_bound = right_bound
		self.up_bound = up_bound
		self.down_bound = down_bound

	def head_position(self) -> Coordinate:
		"""
		Return the position of the snake's head(Coordinate instance).
		:return:
		"""
		return self.nodes[0]

	def length(self) -> int:
		"""
		Return snake's length(int).
		:return:
		"""
		return len(self.nodes)

	def set_direction(self, dir_: int):
		"""
		Set the snake's moving direction to the given argument.

		Directions: 0-down, 1-up, 2-left, 3-right
		:param dir_:
		:return:
		"""
		if (dir_ == 0 and self.dir == 1) or (dir_ == 1 and self.dir == 0):
			return
		if (dir_ == 2 and self.dir == 3) or (dir_ == 3 and self.dir == 2):
			return
		self.dir = dir_

	def move(self, food_pos: Coordinate):
		"""
		Move the snake in the current direction.
		:return:
		"""
		new_head_pos = self.head_position().next(self.dir)
		self.nodes.insert(0, new_head_pos)
		if new_head_pos != food_pos:        # if snake eats the food, no need to pop the tail
			self.nodes.pop()

	def _out_of_bound(self) -> bool:
		"""
		Check whether the snake reaches the boundary.
		:return:
		"""
		head = self.head_position()
		return head.x <= self.left_bound or head.x >= self.right_bound or head.y <= self.up_bound or head.y >= self.down_bound

	def _self_crash(self) -> bool:
		"""
		Check whether the snake crashes on itself.
		:return:
		"""
		head = self.head_position()
		for node in self.nodes[1:]:
			if head == node:
				return True
		return False

	def fail(self):
		"""
		Check if the snake fail the game
		:return:
		"""
		return self._out_of_bound() or self._self_crash()

	def cover(self, pos: Coordinate) -> bool:
		"""
		Check if the snake cover the position pos
		:param pos:
		:return:
		"""
		for node in self.nodes:
			if node == pos:
				return True
		return False