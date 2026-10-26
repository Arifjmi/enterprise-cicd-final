import unittest

from app.app import add, get_app_version


class TestApplication(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_app_version(self):
        self.assertEqual(get_app_version(), "1.0.0")


if __name__ == "__main__":
    unittest.main()
