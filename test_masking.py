import unittest
from faker import Faker

fake = Faker()

def digit_transform(value):
    digit_map = str.maketrans("0123456789", "9876543210")
    return value.translate(digit_map)

class TestMaskingLogic(unittest.TestCase):
    def test_fake_name(self):
        name = fake.name()
        self.assertIsInstance(name, str)
        self.assertGreater(len(name), 0)

    def test_email_from_name(self):
        name = "Rahul Singh"
        email = name.lower().replace(" ", ".") + "@gmail.com"
        self.assertEqual(email, "rahul.singh@gmail.com")

    def test_fake_phone(self):
        phone = fake.msisdn()[:10]
        self.assertEqual(len(phone), 10)
        self.assertTrue(phone.isdigit())

    def test_digit_transform(self):
        original = "0123456789"
        transformed = digit_transform(original)
        self.assertEqual(transformed, "9876543210")

if __name__ == "__main__":
    unittest.main()
