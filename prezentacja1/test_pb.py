def test_lookup_by_name():
    phonebook = Phonebook()
    phonebook.add("Rossmann", "123456789")
    assert "123456789" == phonebook.lookup("Bob")