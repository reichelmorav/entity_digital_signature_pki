#!/bin/bash

ocsp_url="$(openssl x509 -noout -ocsp_uri -in $1)"

openssl ocsp -CAfile /etc/pki/ca/issuing_ca/certs/ca_chain_issuing.cert.pem -url "$ocsp_url" -port 8080 -issuer /etc/pki/ca/issuing_ca/certs/ca_intermediate_issuing.cert.pem -cert $1
