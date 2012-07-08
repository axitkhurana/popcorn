# -*- coding: utf-8 -*-
# Copyright (c) 2012 Ionuț Arțăriși <iartarisi@suse.cz>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from sqlalchemy import Column, String

from popcorn.database import Base


class Vendor(Base):
    __tablename__ = 'vendors'
    vendor_name = Column(String(20), primary_key=True)
    vendor_url = Column(String(100), unique=True, nullable=False)

    def __init__(self, vendor_url):
        self.vendor_url = vendor_url
         # FIXME get better information on the vendor from the RPM
        self.vendor_name = vendor_url[:20]

    def __repr__(self):
        return '<Vendor %s>' % self.vendor_name

    @property
    def _flat_attrs(self):
        return {
            'vendor_name': self.vendor_name,
            'vendor_url': self.vendor_url
        }

    @property
    def serialize(self):
        return dict(**self._flat_attrs)
