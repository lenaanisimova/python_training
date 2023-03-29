# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact

def test_add_contact(app):
    app.contact.add_contact(Contact(firstname="Lena",
                                    middlename="Anisimova",
                                    address="Цветочная, 29",
                                    email="1234",
                                    homepage="1234",
                                    bday="2",
                                    bmonth="May",
                                    byear="1992"))

def test_add_empty_contact(app):
    app.contact.add_contact(Contact(firstname="", middlename="", address="", email="", homepage="", bday="", bmonth="-", byear=""))





