#!/usr/bin/sudo bash

openssl ca -config /etc/pki/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -revoke $1
rm /etc/pki/ca/issuing_ca/crl/ca_intermediate_entities_issuing.crl
openssl ca -config /etc/pki/ca/issuing_ca/openssl.cnf -engine pkcs11 -keyform engine -keyfile 02 -gencrl -crldays 30 -cert /etc/pki/ca/issuing_ca/certs/ca_intermediate_issuing.cert.pem -out /etc/pki/ca/issuing_ca/crl/ca_intermediate_entities_issuing.crl
