#!/bin/bash
cert_serial="$(openssl x509 -noout -serial -in /etc/pki/entities_issued/facultaddeartes/facultaddeartes.pem | cut -d'=' -f2)"
echo "$cert_serial"
crl_URL="$(openssl asn1parse -in $1 | grep -A 1 'X509v3 CRL Distribution Points' | tail -1 | cut -d: -f 4 | cut -b21- | perl -ne 's/(..)/print chr(hex($1))/ge; END {print "\n"}')"
echo "$crl_URL"
wget -P /etc/pki/crls/ "$crl_URL"

openssl crl -in /etc/pki/crls/ca_intermediate_entities_issuing.crl -outform DER -out /etc/pki/crls/issuing.crl

openssl crl -in /etc/pki/crls/issuing.crl -inform DER -text -noout | grep "$cert_serial"


