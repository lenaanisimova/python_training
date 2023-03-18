# -*- coding: utf-8 -*-

import pytest
from model.contact import Contact

def test_add_contact(app):
    app.contact.add_contact(Contact(firstname="Lena",
                            middlename="Anisimova",
                                    nickname="lenaanisimova",
                                      title="1234",
                                      company="lenvendo",
                                      address="Цветочная, 29",
                                      home="1234",
                                      mobile="79111111111",
                                      work="1234",
                                      fax="1234",
                                      email="1234",
                                      email2="1234",
                                      email3="1234",
                                      homepage="1234",
                                      bday="2",
                                      bmonth="May",
                                      byear="1992",
                                      aday="13",
                                      amonth="November",
                                      ayear="1993"))

def test_add_empty_contact(app):
    app.contact.add_contact(Contact(firstname="", middlename="", nickname="", title="", company="", address="", home="",
                         mobile="", work="", fax="", email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="",
                         amonth="-", ayear=""))





