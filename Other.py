from numpy import array as numpy_array
from numpy import diag as diag
from numpy import fliplr as fliplr


class Other(object):

	def symbol_2_num(self, symbol):
		if symbol == 'x':
			return -1
		elif symbol == 'o':
			return 1
		else:
			print('Not a valid symbol')
			return 0

	def num_to_symbol(self, num):
		if num == 0:
			return ' '
		elif num == -1:
			return 'x'
		elif num == 1:
			return 'o'
		else:
			print("Error!")
			return 'E'

	def num_to_symbol_list(self, num_list):
		return [self.num_to_symbol(i) for i in num_list]

	def is_positive(self, num):
		if num > 0:
			return True
		else:
			return False

	def sign_to_list(self, l):
		return [1 if self.is_positive(element) is True else -1 for element in l]

	def sign_to_list_single_integer(self, l):
		return int(*self.sign_to_list(l))

	def find_num_in_list(self, num, l):
		l.index(num)
		return

	def extract_diagonals(self, matrix):
		main_diag = diag(numpy_array(matrix))
		second_diag = diag(fliplr(numpy_array(matrix)))

		return main_diag, second_diag


if __name__ == "__main__":
	ob = Other()
	l1 = [1, 2, 3, -10, -20, -2]
	l2 = ob.sign_to_list(l1)
	l3 = [-10]
	l4 = ob.sign_to_list_single_integer(l3)
	print(l1)
	print(l2)
	print(l3)
	print(l4)

	print(l2.index(-1))

	matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
	main_diag, second_diag = ob.extract_diagonals(matrix)
	print(main_diag)
	print(sum(main_diag))
	print(second_diag)
	print(sum(second_diag))
