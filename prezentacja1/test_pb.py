class PhoneBook():
    def __init__(self) -> None:
        self.numbers = {}
    
    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]


def test_lookup_by_name():
    phonebook = PhoneBook()
    phonebook.add("Rossmann", "123456789")
    assert "123456789" == phonebook.lookup("Rossmann")