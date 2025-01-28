import unittest
from datetime import datetime

import fatture
import errors

fattura_mock = {
    "id": 1234,
    "emitted": datetime.utcnow(),
    "recipient": "pippo industries s.r.l.",
    "fiscal_code": "ppp123h501o",
    "vat": "1234567",
    "payment_4": 0.0,
    "payment_10": 0.0,
    "payment_22": 1000.0 
}

fattura_mock_result = {
    "id": 1234,
    "emitted": datetime.utcnow(),
    "recipient": "pippo industries s.r.l.",
    "fiscal_code": "ppp123h501o",
    "vat": "1234567",
    "payment_4": 0.0,
    "payment_10": 0.0,
    "payment_22": 1000.0,
    "tax_4": 0.0,
    "tax_10": 0.0,
    "tax_22": 220.0,
    "total": 1220.0 
}

class TestCreate(unittest.TestCase):
    def ok(self):
        self.assertTrue(fatture.create(fattura_mock))
    def missing_input(self):
        self.assertRaises(fatture.create(None), errors.MissingInputExceptionException)
    def missing_id(self):
        test_value = {
            "emitted": datetime.utcnow(),
            "recipient": "pippo industries s.r.l.",
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": 1000.0 
        }
        self.assertRaises(fatture.create(test_value), errors.MissingIdException)
    def missing_mandatory_field(self):
        test_value = {
            "id": 1234,
            "emitted": datetime.utcnow(),
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": 1000.0 
        }
        self.assertRaises(fatture.create(test_value), errors.MissingIdException)
    def wrong_date(self):
        test_value = {
            "id": 1234,
            "emitted": "pippo",
            "recipient": "pippo industries s.r.l.",
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": 1000.0 
        }
        self.assertRaises(fatture.create(test_value), errors.WrongDateFormatException)
    def wrong_payment(self):
        test_value = {
            "id": 1234,
            "emitted": datetime.utcnow(),
            "recipient": "pippo industries s.r.l.",
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": "pippo"
        }
        self.assertRaises(fatture.create(test_value), errors.WrongPaymentFormatException)
    def negative_payment(self):
        test_value = {
            "id": 1234,
            "emitted": datetime.utcnow(),
            "recipient": "pippo industries s.r.l.",
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": -1000.0 
        }
        self.assertRaises(fatture.create(test_value), errors.NegativePaymentException)
    def big_payment(self):
        test_value = {
            "id": 1234,
            "emitted": datetime.utcnow(),
            "recipient": "pippo industries s.r.l.",
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 99999999999.0,
            "payment_10": 99999999999.0,
            "payment_22": 999999999999.0 
        }
        self.assertTrue(fatture.create(test_value))
    def small_payment(self):
        test_value = {
            "id": 1234,
            "emitted": datetime.utcnow(),
            "recipient": "pippo industries s.r.l.",
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 0.00000000000001,
            "payment_10": 0.00000000000001,
            "payment_22": 0.00000000000001
        }
        self.assertTrue(fatture.create(test_value))


class TestUpdate(unittest.TestCase):
    def ok(self):
        self.assertTrue(fatture.update(fattura_mock))
    def missing_input(self):
        self.assertRaises(fatture.create(None), errors.MissingInputExceptionException)
    def missing_id(self):
        test_value = {
            "emitted": datetime.utcnow(),
            "recipient": "pippo industries s.r.l.",
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": 1000.0 
        }
        self.assertRaises(fatture.update(test_value), errors.MissingIdException)
    def unknown_id(self):
        test_value = {
            "id": 1235,
            "emitted": datetime.utcnow(),
            "recipient": "pippo industries s.r.l.",
            "fiscal_code": "ppp123h501o",
            "vat": "1234567",
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": 1000.0 
        }
        self.assertRaises(fatture.update(test_value), errors.MissingIdException)
    def wrong_date(self):
        test_value = {
            "id": 1234,
            "emitted": "pippo"
        }
        self.assertRaises(fatture.update(test_value), errors.WrongDateFormatException)
    def wrong_payment(self):
        test_value = {
            "id": 1234,
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": "pippo"
        }
        self.assertRaises(fatture.update(test_value), errors.WrongPaymentFormatException)
    def negative_payment(self):
        test_value = {
            "id": 1234,
            "payment_4": 0.0,
            "payment_10": 0.0,
            "payment_22": -1000.0 
        }
        self.assertRaises(fatture.update(test_value), errors.NegativePaymentException)
    def big_payment(self):
        test_value = {
            "id": 1234,
            "payment_4": 99999999999.0,
            "payment_10": 99999999999.0,
            "payment_22": 999999999999.0 
        }
        self.assertTrue(fatture.update(test_value))
    def small_payment(self):
        test_value = {
            "id": 1234,
            "payment_4": 0.00000000000001,
            "payment_10": 0.00000000000001,
            "payment_22": 0.00000000000001
        }
        self.assertTrue(fatture.update(test_value))


class TestDelete(unittest.TestCase):
    def ok(self):
        self.assertTrue(fatture.delete(fattura_mock.get("id")))
    def missing_id(self):
        self.assertRaises(fatture.delete(None), errors.MissingIdException)
    def unknown_id(self):
        self.assertRaises(fatture.delete(1235), errors.MissingIdException)

class TestRead(unittest.TestCase):
    def ok(self):
        self.assertEqual(fatture.read(fattura_mock.get("id")), fattura_mock_result)
    def missing_id(self):
        self.assertRaises(fatture.read(None), errors.MissingIdException)
    def unknown_id(self):
        self.assertRaises(fatture.read(1235), errors.MissingIdException)