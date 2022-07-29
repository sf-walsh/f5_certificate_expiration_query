#!/usr/bin/env python3

# pip install f5-sdk
# https://f5-sdk.readthedocs.io/en/latest/userguide/object_path.html

import os
import sys
from datetime import datetime

import jsonargparse
from f5.bigip import ManagementRoot

NOW = datetime.now()
CRITICAL = []
WARNING = []
EXPIRED = []

def check_cert(cert, warning, critical):
    expiration_time = datetime.fromtimestamp(cert.expirationDate)
    delta = expiration_time - NOW
    if delta.days >= 0 and delta.days <= critical:
        CRITICAL.append(cert)
    if delta.days >= critical and delta.days <= warning:
        WARNING.append(cert)
    elif delta.days <= 0:
        EXPIRED.append(cert)

def connect(args):
    client = ManagementRoot(args.f5.ip, args.f5.user, args.f5.password, port=args.f5.port)
    certs = client.tm.sys.file.ssl_certs.get_collection()
    for cert in certs:
        check_cert(cert, args.warning, args.critical)

    if len(CRITICAL):
        print(f'CRITICAL: ', len(CRITICAL), 'certificate(s) are going to expire in ',args.critical,'days.')
        for crit in CRITICAL:
            print(f'Certificate: ',crit.name, datetime.fromtimestamp(int(crit.expirationDate)))
    if len(WARNING):
        print(f'WARNING: ', len(WARNING), 'certificates are going to expire ',args.warning,'days.')
        for warn in WARNING:
            print(f'Certificate: ',warn.name, datetime.fromtimestamp(int(warn.expirationDate)))
    if len(EXPIRED):
        print(f'EXPIRED: ', len(EXPIRED), 'certificates are expired ')
        for expire in EXPIRED:
            print(f'Certificate: ',expire.name, datetime.fromtimestamp(int(expire.expirationDate)))
    if not any((WARNING, CRITICAL, EXPIRED)):
        print('OK!')
        sys.exit(0)
    sys.exit(0)

def main():
    parser = jsonargparse.ArgumentParser(
        description="Monitor SSL certificates expiration registered in a F5 server.",
        default_env=True,
    )
    parser.add_argument(
        "-w",
        "--warning",
        help="number of days to raise a warning",
        type=int,
        required=True,
    )
    parser.add_argument(
        "-c",
        "--critical",
        help="number of days to raise a critical",
        type=int,
        required=True,
    )
    parser.add_argument(
        "--f5.ip",
         help="F5 IP or hostname to connect to",
         required=True,
    )
    parser.add_argument(
        "--f5.user",
        help="F5 user to access Big IP API",
        required=True,
    )
    parser.add_argument(
        "--f5.password",
        help="F5 password to access Big IP API",
        required=True,
    )
    parser.add_argument(
        "--f5.port",
        help="F5 port to connect to the Big API",
        required=True
    )
    args = parser.parse_args()
    
    return connect(args)

if __name__ == "__main__":
    main()