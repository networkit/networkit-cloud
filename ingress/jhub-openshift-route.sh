#!/bin/bash

if [ "$#" -ne 4 ]; then
    echo "Illegal number of parameters"
    echo "This script sets a public URL for the service."
    echo "Should be called like 'jhub-openshift-route.sh <URL-SUBPATH> <CERT-FILE> <KEY-FOR-CERT> <CA-CERT-FILE>"
fi

oc create route edge --service=jhub-service --cert=$2 --key=$3 --ca-cert=$4 --path=$1
kubectl annotate route jhub-service --overwrite haproxy.router.openshift.io/hsts_header="max-age=31536000;includeSubDomains;preload"
