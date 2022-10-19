#!/bin/bash

crl_URL="$(openssl asn1parse -in $1 | grep -A 1 'X509v3 CRL Distribution Points' | tail -1 | cut -d: -f 4 | cut -b21- | perl -ne 's/(..)/print chr(hex($1))/ge; END {print "\n"}')"
echo "$crl_URL"
wget -P /etc/pki/crls/ "$crl_URL"

openssl crl -in /etc/pki/crls/ "$crl_URL" -inform DER -text -noout
