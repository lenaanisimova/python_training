# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Lena",
                                    lastname="Anisimova",
                                    address="Цветочная, 29",
                                    email="1234",
                                    homepage="1234",
                                    bday="2",
                                    bmonth="May",
                                    byear="1992")
    app.contact.add_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_add_empty_contact(app):
#   old_contacts = app.contact.get_contact_list()
#   contact = Contact(firstname="", lastname="", address="", email="", homepage="", bday="", bmonth="-", byear="")
#   app.contact.add_contact(contact)
#   new_contacts = app.contact.get_contact_list()
#   assert len(old_contacts) + 1 == len(new_contacts)
#   old_contacts.append(contact)
#   assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





