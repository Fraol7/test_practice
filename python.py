import unittest
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total(self):
        return self.price * self.quantity
class TestProduct(unittest.TestCase):
    def test_calculate_total(self):
        product = Product('Widget', 10, 2)
        total = product.calculate_total()
        self.assertEqual(total, 20)
    def test_calculate_total_with_zero_quantity(self):
        product = Product('Widget', 10, 0)
        total = product.calculate_total()
        self.assertEqual(total, 0)
    def test_calculate_total_with_zero_price(self):
        product = Product('Widget', 0, 2)
        total = product.calculate_total()
        self.assertEqual(total, 0)
    def test_calculate_total_with_negative_price(self):
        product = Product('Widget', -10, 2)
        total = product.calculate_total()
        self.assertEqual(total, -20)
    def test_calculate_total_with_negative_quantity(self):
        product = Product('Widget', 10, -2)
        total = product.calculate_total()
        self.assertEqual(total, -20)
if __name__ == '__main__':
    unittest.main()
    