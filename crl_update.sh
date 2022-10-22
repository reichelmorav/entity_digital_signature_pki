#!/usr/bin/sudo bash

crl_date="$(openssl crl -in /etc/pki/ca/issuing_ca/crl/ca_intermediate_entities_issuing.crl -noout -nextupdate | cut -d'=' -f2)"
crl_date_f="$(date -d "$crl_date" -u)"
echo "$crl_date_f"

actual_date="$(date +"%a %b %d %H:%M:%S %p %Z %Y" -u)"
echo "$actual_date"

if [[ "$crl_date_f" < "$actual_date" ]]
then 
    echo "fecha menor"
    #rm /etc/pki/ca/issuing_ca/crl/ca_intermediate_entities_issuing.crl
    #openssl ca -engine pkcs11 -keyform engine -keyfile 02 -gencrl -crldays 30 -cert /etc/pki/ca/issuing_ca/certs/ca_intermediate_issuing.cert.pem -out /etc/pki/ca/issuing_ca/crl/ca_intermediate_entities_issuing.crl
else 
    echo "fecha mayor"
fi