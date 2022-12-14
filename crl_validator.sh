#!/bin/bash
if [ -z $1 ]
then 
    echo "Debe especificar la ruta del certificado"; 
else 
   rm /etc/pki/crls/ca_intermediate_entities_issuing.crl /etc/pki/crls/issuing.crl
    cert_serial="$(openssl x509 -noout -serial -in $1 | cut -d'=' -f2)"
    crl_URL="$(openssl asn1parse -in $1 | grep -A 1 'X509v3 CRL Distribution Points' | tail -1 | cut -d: -f 4 | cut -b21- | perl -ne 's/(..)/print chr(hex($1))/ge; END {print "\n"}')"
    wget -P /etc/pki/crls/ "$crl_URL" --no-check-certificate -q

    openssl crl -in /etc/pki/crls/ca_intermediate_entities_issuing.crl -outform DER -out /etc/pki/crls/issuing.crl

    status="$(openssl crl -in /etc/pki/crls/issuing.crl -inform DER -text -noout | grep "$cert_serial")"

    if [ -z "$status" ]; then echo "Good"; else echo "Revoked"; fi
fi
