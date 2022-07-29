# <u>F5 Certificate Expiry Query</u>
<br/>

## Pre-Requisite ##
```sh
pip install f5-sdk
```

## Usage ##
```sh
./f5_check_certificates.py -h --warning <number> --critical <number> --f5.ip <ip> --f5.user <username> --f5.password <password> --f5.port <port>
```

## Example ###
```sh

./f5_check_certificates.py --warning 45 --critical 30 --f5.ip 10.100.10.10 --f5.user admin --f5.password password --f5.port 8443

CRITICAL:  2 certificate(s) are going to expire in  30  days.
Certificate:  test_cert_a 2022-08-18 09:31:37
Certificate:  test_cert_f 2022-07-31 14:06:29
WARNING:  2 certificates are going to expire  45  days.
Certificate:  test_cert_d 2022-09-12 09:33:02
Certificate:  test_cert_e 2022-09-07 13:05:53
```


</br>

### <u>Supporting Documentation</u>
https://f5-sdk.readthedocs.io/en/latest/userguide/object_path.html (API may be deprecated)

</br>

### <u> From F5 CLI </u>

Query for SSL Certificates that are going to expire within a certain time frame. F5 Documentation provides the following done via tmos: https://support.f5.com/csp/article/K14318

```sh
# Checking for just those expiring soon
```
```
(tmos)# cd /; run /sys crypto check-cert
emailAddress=testuser@bigbusiness.org,CN=test_cert_a,OU=test_division,O=test,L=US,ST=FL,C=US in file /Common/test_cert_a will expire on Aug 18 13:31:37 2022 GMT

```sh
#Checking all certs in all partitions and all statuses
```
```
(tmos)# cd /; run /sys crypto check-cert verbose enabled
Jul 18 21:00:13 2027 GMT | emailAddress=support@f5.com,CN=support.f5.com,OU=Product Development,O=F5 Networks,L=Seattle,ST=Washington,C=US | /Common/f5-irule.crt: OK
Dec  7 17:55:54 2030 GMT | CN=Entrust Root Certification Authority - G2,OU=(c) 2009 Entrust, Inc. - for authorized use only,OU=See www.entrust.net/legal-terms,O=Entrust, Inc.,C=US | /Common/f5-ca-bundle.crt: OK
Jul 26 13:06:51 2032 GMT | emailAddress=root@localhost.localdomain,CN=localhost.localdomain,OU=IT,O=MyCompany,L=Seattle,ST=WA,C=US | /Common/default.crt: OK
Apr 18 05:52:37 2028 GMT | CN=CrossTrust OV CA4,O=CrossTrust,C=JP | /Common/ca-bundle.crt: OK
.
.
.
Dec  7 17:55:54 2030 GMT | CN=Entrust Root Certification Authority - G2,OU=(c) 2009 Entrust, Inc. - for authorized use only,OU=See www.entrust.net/legal-terms,O=Entrust, Inc.,C=US | /Common/ca-bundle.crt: OK
Feb 27 21:00:12 2043 GMT | CN=Microsoft ECC TS Root Certificate Authority 2018,O=Microsoft Corporation,L=Redmond,ST=Washington,C=US | /Common/ca-bundle.crt: OK
Dec 31 23:59:59 2029 GMT | CN=Starfield Services Root Certificate Authority,OU=http://certificates.starfieldtech.com/repository/,O=Starfield Technologies, Inc.,L=Scottsdale,ST=Arizona,C=US | /Common/ca-bundle.crt: OK
emailAddress=testuser@bigbusiness.org,CN=test_cert_a,OU=test_division,O=test,L=US,ST=FL,C=US in file /Common/test_cert_a will expire on Aug 18 13:31:37 2022 GMT
Jan 25 13:32:16 2023 GMT | CN=test_cert_b,OU=test_division,O=test,L=US,ST=FL,C=US | /Common/test_cert_b: OK
Jul 29 13:32:36 2023 GMT | emailAddress=testuser@bigbusiness.org,CN=test_cert_c,OU=test_division,O=test,L=US,ST=FL,C=US | /Common/test_cert_c: OK
Sep 12 13:33:02 2022 GMT | emailAddress=testuser@bigbusiness.org,CN=test_cert_d,OU=test_division,O=test,L=US,ST=FL,C=US | /Common/test_cert_d: OK
```