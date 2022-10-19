from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.x509 import ocsp
from cryptography.x509.ocsp import OCSPResponseStatus
from cryptography.x509.oid import ExtensionOID, AuthorityInformationAccessOID
import sys

def get_crl_server(cert):    
    certifocate = x509.load_pem_x509_certificate(open(cert, 'rb').read(), default_backend())
    aia = certifocate.extensions.get_extension_for_oid(ExtensionOID.CRL_DISTRIBUTION_POINTS).value
    crls = [ia for ia in aia if ia.access_method == CRLEntryExtensionOID.]
    if not crls:
        raise Exception(f'no ocsp server entry in AIA')
    return crls[0].access_location.value         

print(get_crl_server(sys.argv[1]))