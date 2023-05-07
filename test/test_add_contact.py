# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact
import random
import string

def random_string(prefix,maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digits(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_ascii_letters(prefix, maxlen):
    symbols = string.ascii_letters
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(maxlen_1, maxlen_2, maxlen_3):
    prefix = string.ascii_letters + string.digits + "-" + "." + "_"
    domen = string.ascii_lowercase
    email = "".join([random.choice(prefix) for i in range(random.randrange(maxlen_1))]) + "@" + \
            "".join([random.choice(domen) for i in range(random.randrange(maxlen_2))]) + "." +\
            "".join([random.choice(domen) for i in range(random.randrange(maxlen_3))])
    return email
def random_dbirth():
    day = random.randint(1, 28)
    return str(day)

def random_dmonth():
    return random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"])
def random_dyear():
    year = random.randint(1899, 2023)
    return str(year)

testdata = [
    Contact(firstname=random_ascii_letters("firstname", 10), lastname=random_ascii_letters("lastname", 10),
                address=random_string("address", 10), homephone=random_digits(5), mobilephone=random_digits(5),
                workphone=random_digits(10), email=random_email(5, 9, 6), bday=random_dbirth(),
                bmonth=random_dmonth(), byear=random_dyear())
        for i in range(5)
]
@pytest.mark.parametrize("contact",testdata,ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)







