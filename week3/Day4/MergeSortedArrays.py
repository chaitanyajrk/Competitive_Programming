import unittest


def merge_lists(my_list, alices_list):

	# Combine the sorted lists into one large sorted list
	arr = []
	i = 0
	j = 0

	while(True):
		if(len(arr)==len(my_list)+len(alices_list)):
			break
		if i==len(my_list):
			for i in alices_list[j:]:
				arr.append(i)
		elif j==len(alices_list):
			for i in my_list[i:]:
				arr.append(i)
			# print(arr)
		# print(arr)
		else:
			if(my_list[i]<=alices_list[j]):
				arr.append(my_list[i])
				i = i+1
			else:
				arr.append(alices_list[j])
				j = j+1
		# print(arr)
	return arr


















# Tests

class Test(unittest.TestCase):

	def test_both_lists_are_empty(self):
		actual = merge_lists([], [])
		expected = []
		self.assertEqual(actual, expected)

	def test_first_list_is_empty(self):
		actual = merge_lists([], [1, 2, 3])
		expected = [1, 2, 3]
		self.assertEqual(actual, expected)

	def test_second_list_is_empty(self):
		actual = merge_lists([5, 6, 7], [])
		expected = [5, 6, 7]
		self.assertEqual(actual, expected)

	def test_both_lists_have_some_numbers(self):
		actual = merge_lists([2, 4, 6], [1, 3, 7])
		expected = [1, 2, 3, 4, 6, 7]
		self.assertEqual(actual, expected)

	def test_lists_are_different_lengths(self):
		actual = merge_lists([2, 4, 6, 8], [1, 7])
		expected = [1, 2, 4, 6, 7, 8]
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)