import unittest


def fib(n):

    arr = [0, 1]
    if n<0:
        raise ValueError("bolo")     
    while len(arr) < n + 1: 
        arr.append(0)      
    if n <= 1:
       return n
    else:
       if arr[n - 1] ==  0:
           arr[n - 1] = fib(n - 1)
     
       if arr[n - 2] ==  0:
           arr[n - 2] = fib(n - 2)
     
       arr[n] = arr[n - 2] + arr[n - 1]
    return arr[n]
    

    


















# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)