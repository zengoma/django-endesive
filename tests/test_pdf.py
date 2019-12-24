#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-endesive
------------

Tests for `django-endesive` pdf module.
"""
import os
from django.test import TestCase, override_settings
from tests.utils.create_test_certs import CreateTestCerts
from django_endesive import pdf
from django.conf import settings
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
        self.doc.output(self.temp_dir + 'pdf.pdf', "F")

        # Create test certificates
        test_certs = CreateTestCerts()
        test_certs.CA()
        test_certs.USERs()

        # Temp Files
        self.pdf_bytes = open(self.temp_dir + 'pdf.pdf', 'rb').read()
        self.cert_file = self.temp_dir + 'demo2_user1.p12'
        self.ca_file = self.temp_dir + 'demo2_ca.crt.pem'
        self.trusted_cert_pems = (open(self.ca_file, 'rt').read(),)

    @override_settings(DJANGO_ENDESIVE={})
    def test_pdf_sign_no_cert(self):
        data = pdf.sign(pdf_bytes=self.pdf_bytes)
        with self.assertRaises(AssertionError):
            verify(data, self.trusted_cert_pems)

    def test_pdf_sign(self):
        data = pdf.sign(pdf_bytes=self.pdf_bytes)

        (hashok, signatureok, certok) = verify(data, self.trusted_cert_pems)

        self.assertTrue(signatureok, 'There is an error with the signature')
        self.assertTrue(hashok, 'There is an error with the hash')
        self.assertTrue(certok, 'There is an error with the certificate')

    def test_pdf_sign_invalid_date(self):
        data = pdf.sign(pdf_bytes=self.pdf_bytes, sign_date='Not a date')
        (hashok, signatureok, certok) = verify(data, self.trusted_cert_pems)

        self.assertTrue(signatureok, 'There is an error with the signature')
        self.assertTrue(hashok, 'There is an error with the hash')
        self.assertTrue(certok, 'There is an error with the certificate')

    @override_settings()
    def test_get_settings(self):
        del settings.DJANGO_ENDESIVE
        self.assertEqual(pdf.get_settings(), {})

    def tearDown(self):
        os.remove(self.temp_dir + 'pdf.pdf')
