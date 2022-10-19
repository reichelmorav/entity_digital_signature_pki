from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.x509 import ocsp
from cryptography.x509.ocsp import OCSPResponseStatus
from cryptography.x509.oid import ExtensionOID, AuthorityInformationAccessOID
import sys

def get_ocsp_server(cert):    
    cert2 = x509.load_pem_x509_certificate(open(cert, 'rb').read(), default_backend())
    aia = cert2.extensions.get_extension_for_oid(ExtensionOID.CRL_DISTRIBUTION_POINTS).value
    print(aia[1])     

get_ocsp_server(sys.argv[1])