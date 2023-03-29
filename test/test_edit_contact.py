
from model.contact import Contact
def test_edit_first_contact(app):
    app.contact.edit_first_contact((Contact(firstname="Lena",
                                            middlename="Anisimova",
                                            address="Цветочная, 29",
                                            email="1234",
                                            homepage="1234",
                                            bday="2",
                                            bmonth="May",
                                            byear="1992",)))