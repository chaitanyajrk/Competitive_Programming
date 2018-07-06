import unittest


import unittest


def is_valid(strr):
	od = {'(': ')','[': ']','{': '}'}
	op = ['(', '[', '{']
	cl = [')', ']', '}']
	ol = []
	for i in range(len(strr)):
		if (strr[i] in op):
			ol.append(strr[i])
		elif (strr[i] in cl):
			if (len(ol)==0):
				return False
			else:
				if (od[ol.pop(len(ol)-1)] != strr[i]):
					return False
  	if len(ol)==0:
  		return True
  	else:
  		return False
	return len(ol)==0

















# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)
















# Tests

class Test(unittest.TestCase):

	def test_valid_short_strr(self):
		result = is_valid('()')
		self.assertTrue(result)

	def test_valid_longer_strr(self):
		result = is_valid('([]{[]})[]{{}()}')
		self.assertTrue(result)

	def test_mismatched_opener_and_closer(self):
		result = is_valid('([][]}')
		self.assertFalse(result)

	def test_missing_closer(self):
		result = is_valid('[[]()')
		self.assertFalse(result)

	def test_extra_closer(self):
		result = is_valid('[[]]())')
		self.assertFalse(result)

	def test_empty_string(self):
		result = is_valid('')
		self.assertTrue(result)


unittest.main(verbosity=2)