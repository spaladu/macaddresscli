#!/usr/bin/python3
# include shebang based on your python3 env or run> python3 filename.py --agrs MACADDRESS format while running the code.
import requests
import re
import argparse

# API KEY
key = "ENTER YOUR API KEY HERE"

'''Below function checks the argument MACADDRESS to be valid and returns a boolean. It will accept and verifies all the below MACADDRESS formats:
XX: XX: XX: XX: XX: XX OR  XX-XX-XX-XX-XX-XX OR XXXXXXXXXXXX'''

def macaddress_check(mac_address):
    check_bool = re.match(
        "^([0-9A-Fa-f]{2}[:.-]?){5}([0-9A-Fa-f]{2})$", mac_address.strip())
    return check_bool

#main function
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("mac_address", type=str, help="ENTER VALID MAC ADDRESS")
    #positional argument for mac_address
    args = parser.parse_args()
    mac_address = args.mac_address

    while macaddress_check(mac_address):
        #this while conditional only runs if the mac address is verified and returns true.
        response = requests.get(
            "https://api.macaddress.io/v1?apiKey="+key+"&output=vendor&search="+mac_address)
        print(response.text)
        break
    else:
        print("Invalid MAC Address")



if __name__ == "__main__":
    main()
