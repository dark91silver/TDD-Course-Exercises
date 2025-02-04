import unittest
from src.cart import add_product, remove_product, total_cart, deploy_cart
from src.errors import ProductNotFoundException

class Test(unittest.TestCase):
    def add_new_ok(self):
        prodotto = {"id":1, "nome":"libro", "prezzo":55.0, "quantità":1}
        test_value = [prodotto]
        self.assertEqual(add_product(prodotto), test_value)
    def check_total_ok(self):
        test_value = 55.0
        self.assertEqual(total_cart(), test_value)
    def add_another_ok(self):
        prodotto = {"id":1, "nome":"libro", "prezzo":55.0, "quantità":1}
        test_value = [{"id":1, "nome":"libro", "prezzo":110.0, "quantità":2}]
        self.assertEqual(add_product(prodotto), test_value)
    def check_discount_ok(self):
        test_value = 99.0
        self.assertEqual(total_cart(), test_value)
    def remove_one_ok(self):
        prod_id = 1
        test_value = [{"id":1, "nome":"libro", "prezzo":55.0, "quantità":1}]
        self.assertEqual(remove_product(prod_id), test_value)
    def remove_last_ok(self):
        prod_id = 1
        self.assertEqual(remove_product(prod_id), [])
    def remove_not_existent(self):
        prod_id = 5
        self.assertRaises(remove_product(prod_id), ProductNotFoundException)


class DeployTest(unittest.TestCase):
    def deploy_ok(self):
        prodotto = {"id":1, "nome":"libro", "prezzo":55.0, "quantità":1}
        prodotto_2 = {"id":1, "nome":"film", "prezzo":30.0, "quantità":1}
        add_product(prodotto)
        add_product(prodotto_2)
        self.assertEqual(deploy_cart(), {"totale":0.0, "prodotti":[]})