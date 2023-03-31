#!/usr/bin/env python

import subprocess
from optparse import OptionParser
import re

# Function to get user inputs
def get_inputs():
    parser = OptionParser()
    parser.add_option("--i", "--interface", dest="interface", help="add your mac address")
    parser.add_option("--mac", "--macaddress", dest="new_mac", help="add your new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error('[-] enter a valid interface, use --help for more info')
        # code for interface error
    elif not options.new_mac:
        parser.error('[-] enter valid mac address , use --help for more info')
    return options
    # or we can us return function this way!
    # change_mac(options.interface, options.new_mac)

# function to change the mac address
def change_mac(interface, new_mac):
    # subprocess.call("ifconfig", shell=True)
    print("[+] Changing the " + interface + " to the mac address " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# funnction to return value stored in ether that is the mac address, using regex
def current_mac(interface):
    result_mac = subprocess.check_output(['ifconfig', interface])
    # print(result_mac)
    resulting_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(result_mac))

    if resulting_mac:
        return resulting_mac.group(0)
    else:
        print("[-] Sorry no Mac Address found.")


# options= get_inputs()

options = get_inputs()  # function to get user inputs and stored in options variable , options holds value of mac as well as interface
returned_mac = current_mac(options.interface) # retured_mac has the current mac address value
print("Current Mac = " + str(returned_mac))
change_mac(options.interface, options.new_mac)
returned_mac = current_mac(options.interface)  # returned_mac is overwritten with new mac address from user
if options.new_mac == returned_mac:
    print("[+] Mac changed successfully to " + options.new_mac)
else:
    print("[-] Mac address did not change.")
