# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
import random
import string

def random_string(maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email():
    domen = [".ru", ".org", ".com"]
    return random_string(10) + "@" + random_string(10) + random.choice(domen)
def random_dbirth():
    day = random.randint(1, 28)
    return str(day)

def random_dmonth():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"])
def random_dyear():
    year = random.randint(1899, 2023)
    return str(year)

testdata = [Contact(firstname=random_string(10), lastname=random_string(10),
                address=random_string(10), homephone=random_digits(5), mobilephone=random_digits(5),
                workphone=random_digits(10), email=random_email(), bday=random_dbirth(),
                bmonth=random_dmonth(), byear=random_dyear())
        for i in range(5)
]
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







