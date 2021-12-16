import unittest
import Ejercicio7


class TestE7(unittest.TestCase):
    def test_1(self):
        D1 = Ejercicio7.Subseq([7, 7, 7, 7, 7])
        result1 = D1.desarrollo()
        self.assertEqual(result1, 16)  # add assertion here

    def test_2(self):
        D2 = Ejercicio7.Subseq([2, 4, 6, 8, 10])
        result2 = D2.desarrollo()
        self.assertEqual(result2, 7)  # add assertion here

    def test_3(self):
        D3 = Ejercicio7.Subseq([2, 6, 10, 11, 5])
        result3 = D3.desarrollo()
        self.assertEqual(result3, 1)  # add assertion here

    def test_4(self):
        D4 = Ejercicio7.Subseq([2, 2, 4])
        result4 = D4.desarrollo()
        self.assertEqual(result4, 0)  # add assertion here

    def test_5(self):
        D5 = Ejercicio7.Subseq([5, 6])
        result5 = D5.desarrollo()
        self.assertEqual(result5, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()