openssl ts -query -data $1 -no_nonce -sha512 -cert -out $2

curl -H "Content-Type: application/timestamp-query" --data-binary '@'$2'' https://freetsa.org/tsr > $3