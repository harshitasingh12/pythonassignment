import unittest

def countDigit(n) :
    if (n == 0) :
        return 0
 
    return (1 + countDigit(n // 10))

def narcissistic_number(n):
    a = []
    for i in range(0, n):
        l = countDigit(i)
        dup = i 
        sm = 0
        while dup:
            sm = sm + pow(dup % 10, l)
            dup = dup // 10
        
        if i == sm:
            a.append(i)
    return a

class NarcissisticNumber(unittest.TestCase):

    def test_01(self):
        input_num = 154
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]

        self.assertEqual(narcissistic_number(input_num), output)

    def test_02(self):
        input_num = 323
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153]

        self.assertEqual(narcissistic_number(input_num), output)

    def test_03(self):
        input_num = 371
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370]

        self.assertEqual(narcissistic_number(input_num), output)

    def test_04(self):
        input_num = 1635
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634]

        self.assertEqual(narcissistic_number(input_num), output)

    def test_05(self):
        input_num = 1634
        output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]

        self.assertEqual(narcissistic_number(input_num), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)



