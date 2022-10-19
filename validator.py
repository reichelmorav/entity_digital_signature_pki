import sys
from certvalidator import CertificateValidator, ValidationContext

with open(sys.argv[1], 'rb') as f:
    end_entity_cert = f.read()
    print(end_entity_cert)

context = ValidationContext(allow_fetching=True)
validator = CertificateValidator(end_entity_cert, validation_context=context)
validator.validate_usage("digital_signature")

