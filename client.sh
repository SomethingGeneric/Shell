#!/bin/bash

if [[ "$1" == "" ]]; then
    printf "Recieve port: "
    read PORT
else
    PORT=$1
fi

echo "Listening for connections on port ${PORT}"

echo "Press ctrl+c to exit"

while true; do
echo "Waiting for connection"
ncat -l -p ${PORT}
echo "Connection closed."
done
