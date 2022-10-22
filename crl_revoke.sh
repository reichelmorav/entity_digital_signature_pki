#!/bin/bash

openssl ca -config /etc/pki/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -revoke $1
rm /etc/pki/crls/ca_intermediate_entities_issuing.crl
openssl ca -engine pkcs11 -keyform engine -keyfile 02 -gencrl -crldays 30 -cert /etc/pki/ca/issuing_ca/certs/ca_intermediate_issuing.cert.pem -out crl/ca_intermediate_entities_issuing.crl
