import unittest


class PhoneBookTest(unittest.TestCase):
    def setUp(self):
        self.phonebook = PhoneBook()

    def tearDown(self):
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Rossman", "123456789")
        number = self.phonebook.lookup("Rossman")
        self.assertEqual("123456789", number)

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")