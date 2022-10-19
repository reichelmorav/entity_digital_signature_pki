#!/bin/bash

crl_URL= "$(openssl asn1parse -in $1 | 
grep -A 1 'X509v3 CRL Distribution Points' | tail -1 | cut -d: -f 4 | cut -b21)"

echo crl_URL
