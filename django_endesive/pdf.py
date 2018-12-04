from OpenSSL.crypto import load_pkcs12
from endesive import pdf
from django.utils import timezone
from datetime import datetime
from django_endesive.apps import DjangoEndesiveConfig
from django.conf import settings

def get_settings():
    try:
        return settings.DJANGO_ENDESIVE
    except AttributeError:
        print("WARNING: YOU HAVE NOT DECLARED 'DJANGO_ENDESIVE' IN YOUR SETTINGS FILE")
        return {}

def pdf_time(pdf_date=timezone.now()):
    """Convert datetime bytes for 'singingdate'

    :param pdf_date: Datetime object
    :return: bytes A bytestring date
    """
    if not isinstance(pdf_date, datetime):
        pdf_date = timezone.now()

    pdf_date = pdf_date.strftime("%Y%m%d%H%M%S%z")
    pdf_date = "{}{}{}{}".format(pdf_date[:-2], '\'',pdf_date[-2:], '\'' )
    return bytes(pdf_date, 'utf-8')

def sign(pdf_file, sign_date=timezone.now()):
    cert_path = get_settings().get('PDF_CERTIFICATE_PATH', None)
    password =  get_settings().get('PDF_CERTIFICATE_PASSWORD', '')
    location =  bytes(get_settings().get('PDF_ATTRIBUTES', {}).get('LOCATION', ''), 'utf-8')
    contact =  bytes(get_settings().get('PDF_ATTRIBUTES', {}).get('CONTACT', ''), 'utf-8')
    reason =  bytes(get_settings().get('PDF_ATTRIBUTES', {}).get('REASON', ''), 'utf-8')

    if cert_path:
        dct = {
            b'sigflags': 3,
            b'contact': contact,
            b'location': location,
            b'signingdate': pdf_time(sign_date),
            b'reason': reason,
        }
        p12 = load_pkcs12(open(cert_path, 'rb').read(), password)
        datau = open(pdf_file, 'rb').read()
        datas = pdf.cms.sign(datau, dct,
            p12.get_privatekey().to_cryptography_key(),
            p12.get_certificate().to_cryptography(),
            [],
            'sha256'
        )
        with open(pdf_file, 'wb') as fp:
            fp.write(datau)
            fp.write(datas)
