
from model.contact import Contact
from random import randrange
def test_edit_first_contact(app):
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

    contact = Contact(firstname="Lena123456", lastname="Anisimova12", address="Цветочная, 29", email="1234",
                      homepage="1234", bday="2", bmonth="May", byear="1992")
    app.contact.contact_change_by_index(index, contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
