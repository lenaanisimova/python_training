
from model.contact import Contact
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
    contact = Contact(firstname="Lena123456", lastname="Anisimova12", address="Цветочная, 29", email="1234",
                      homepage="1234", bday="2", bmonth="May", byear="1992")
    app.contact.edit_first_contact(contact)
    contact.id = old_contacts[0].id
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
