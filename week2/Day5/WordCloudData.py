import string
import re
import unittest

class wCloudData(object):

	#print(scores)	

	def __init__(self, input_string):

		ep = r"\.|!|\?"
		sen = re.split(ep, input_string)

		self.w2c = {}
		for se in sen:
			ws = re.split(r"[^a-zA-Z0-9-']+", se)
			for w in ws:
				if w != '-':
					self.w2c[w] = self.w2c.get(w, 0) + 1
#print(scores)	
		def cap_w(w):
			return w[0:1] in string.uppercase
#print(scores)	
		for w, count in self.w2c.items():
			if cap_w(w) and w.lower() in self.w2c:
				self.w2c[w.lower()] += self.w2c[w]
				del self.w2c[w]
				#print(scores)	
		# return self.w2c
		


















# Tests

# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

	def test_simple_se(self):
		input = 'I like cake'

		w_cloud = wCloudData(input)
		actual = w_cloud.w2c

		expected = {'I': 1, 'like': 1, 'cake': 1}
		self.assertEqual(actual, expected)

	def test_longer_se(self):
		input = 'Chocolate cake for dinner and pound cake for dessert'

		w_cloud = wCloudData(input)
		actual = w_cloud.w2c

		expected = {
			'and': 1,
			'pound': 1,
			'for': 2,
			'dessert': 1,
			'Chocolate': 1,
			'dinner': 1,
			'cake': 2,
		}
		self.assertEqual(actual, expected)

	def test_punctuation(self):
		input = 'Strawberry short cake? Yum!'

		w_cloud = wCloudData(input)
		actual = w_cloud.w2c

		expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
		self.assertEqual(actual, expected)

	def test_hyphenated_ws(self):
		input = 'Dessert - mille-feuille cake'

		w_cloud = wCloudData(input)
		actual = w_cloud.w2c

		expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
		self.assertEqual(actual, expected)

	def test_ellipses_between_ws(self):
		input = 'Mmm...mmm...decisions...decisions'

		w_cloud = wCloudData(input)
		actual = w_cloud.w2c

		expected = {'mmm': 2, 'decisions': 2}
		self.assertEqual(actual, expected)

	def test_apostrophes(self):
		input = "Allie's Bakery: Sasha's Cakes"

		w_cloud = wCloudData(input)
		actual = w_cloud.w2c

		expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
		self.assertEqual(actual, expected)


unittest.main(verbosity=2)