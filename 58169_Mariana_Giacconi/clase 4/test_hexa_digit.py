import unittest
from hexa import (
    hexa,
    hexa_digit,
)


class TestDecimalToHexaDigit(unittest.TestCase):

    def test_0_to_hexa_digit(self):
        self.assertEqual(
            hexa_digit(0),
            '0',
        )

    def test_1_to_hexa_digit(self):
        self.assertEqual(
            hexa_digit(1),
            '1',
        )

    def test_5_to_hexa_digit(self):
        self.assertEqual(
            hexa_digit(5),
            '5',
        )

    def test_10_to_hexa_digit(self):
        self.assertEqual(
            hexa_digit(10),
            'A',
        )

    def test_11_to_hexa_digit(self):
        self.assertEqual(
            hexa_digit(11),
            'B',
        )

    def test_12_to_hexa_digit(self):
        self.assertEqual(
            hexa_digit(12),
            'C',
        )

    def test_15_to_hexa_digit(self):
        self.assertEqual(
            hexa_digit(15),
            'F',
        )

class TestDecimalToHexa(unittest.TestCase):

    def test_5_to_hexa(self):
        self.assertEqual(
            hexa(5),
            '5',
        )

    def test_10_to_hexa(self):
        self.assertEqual(
            hexa(10),
            'A',
        )

    def test_11_to_hexa(self):
        self.assertEqual(
            hexa(11),
            'B',
        )

    def test_12_to_hexa(self):
        self.assertEqual(
            hexa(12),
            'C',
        )

    def test_15_to_hexa(self):
        self.assertEqual(
            hexa(15),
            'F',
        )

    def test_16_to_hexa(self):
        self.assertEqual(
            hexa(16),
            '10',
        )

    def test_17_to_hexa(self):
        self.assertEqual(
            hexa(17),
            '11',
        )

    def test_4095_to_hexa(self):
        self.assertEqual(
            hexa(4095),
            'FFF',
        )

    def test_1234_to_hexa(self):
        self.assertEqual(
            hexa(1234),
            '4D2',
        )

    def test_234_to_hexa(self):
        self.assertEqual(
            hexa(234),
            'EA',
        )


if __name__ == '__main__':
    unittest.main()