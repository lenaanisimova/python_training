
from model.contact import Contact
def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="Lena",
                                        middlename="Anisimova",
                                        address="Цветочная, 29",
                                        email="1234",
                                        homepage="1234",
                                        bday="2",
                                        bmonth="May",
                                        byear="1992"))
    app.contact.edit_first_contact((Contact(firstname="Lena",
                                            middlename="Anisimova",
                                            address="Цветочная, 29",
                                            email="1234",
                                            homepage="1234",
                                            bday="2",
                                            bmonth="May",
                                            byear="1992",)))