# Macaddresscli
A Simple Python script to check vendor of a Mac Address.

## Prerequisites

- Signup and get a API Key from https://macaddress.io/

- Needs Python 3

- Requests, argparse and re modules needs to be installed.

## Usage:

- once your clone this script change/add shebang for your python env.
- Update your API Key as key variable on the script.

Then run the Script with a valid Mac Address:
```javascript
./macaddrcli.py "443839ffef57"
```
Output (vendor name):
```javascript
Cumulus Networks, Inc
```
- You can use "XX:XX:XX:XX:XX:XX" OR  "XX-XX-XX-XX-XX-XX" OR "XXXXXXXXXXXX" for Mac Address format.


If you provide a invalid Mac Address the Output will show:
```javascript
Invalid MAC Address
```
If your API is invalid or empty the Output will show:
```javascript
Access restricted. Enter the correct API key.
```

## Security
This script has a API Key that can be visible in plain text. To avoid this we can export the key as a ENV Varible, this script is only meant to be used
as a personal script on a user device.
