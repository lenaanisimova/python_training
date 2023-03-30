
from model.contact import Contact
def test_delete_first_contact(app):
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
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts