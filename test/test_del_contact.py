from random import randrange
from model.contact import Contact

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="Lena",
                                        lastname="Anisimova",
                                        address="Цветочная, 29",
                                        email="1234",
                                        homepage="1234",
                                        bday="2",
                                        bmonth="May",
                                        byear="1992"))

    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    # assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)