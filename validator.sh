#!/bin/bash

cert_serial = openssl x509 -noout -serial -in $1 | cut -d'=' -f2 | sed 's/../&:/g;s/:$//'
echo "$cert_serial"
crl_URL="$(openssl asn1parse -in $1 | grep -A 1 'X509v3 CRL Distribution Points' | tail -1 | cut -d: -f 4 | cut -b21- | perl -ne 's/(..)/print chr(hex($1))/ge; END {print "\n"}')"
echo "$crl_URL"
wget -P /etc/pki/crls/ "$crl_URL"

openssl crl -in /etc/pki/crls/ca_intermediate_entities_issuing.crl -outform DER -out /etc/pki/crls/issuing.crl

#openssl crl -in ssca-sha2-g6.crl -inform DER -text -noout | grep YOUR_SERIAL_NUMBER


