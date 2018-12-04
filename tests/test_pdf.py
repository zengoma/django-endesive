#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-endesive
------------

Tests for `django-endesive` pdf module.
"""

from django.test import TestCase
from tests.utils.create_test_certs import CreateTestCerts
from django_endesive import pdf
from tests import settings
from endesive.pdf import fpdf, verify

TEMP_ROOT = settings.TEMP_ROOT


class TestDjangoEndesive(TestCase):


    def setUp(self):
        self.temp_dir = TEMP_ROOT

        # Create a pdf file for testing
        self.doc = fpdf.FPDF()
        self.doc.add_page()
        self.doc.set_font('helvetica', '', 13.0)
        self.doc.cell(w=75.0, h=22.0, align='C',
                      txt='Hello, world page=1.', border=0, ln=0)
        self.doc.output(self.temp_dir+'pdf.pdf', "F")

        # Create test certificates
        test_certs = CreateTestCerts()
        test_certs.CA()
        test_certs.USERs()

        # Temp Files
        self.pdf_file = self.temp_dir+'pdf.pdf'
        self.cert_file = self.temp_dir+'demo2_user1.p12'
        self.ca_file = self.temp_dir+'demo2_ca.crt.pem'

    def test_pdf_sign(self):

        trusted_cert_pems = (open(self.ca_file, 'rt').read(),)

        pdf.sign(pdf_file=self.pdf_file)

        data = open(self.pdf_file, 'rb').read()
        (hashok, signatureok, certok) = verify(data, trusted_cert_pems)

        self.assertTrue(signatureok, 'There is an error with the signature')
        self.assertTrue(hashok, 'There is an error with the hash')
        self.assertTrue(certok, 'There is an error with the certificate')


    def tearDown(self):
        # Delete temp files?
        pass
