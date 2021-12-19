#!/usr/bin/env python3
#Library of Functions created by Matt Faulkner, a python beginner.
#
#
import os #linuxPing() 

def main():
	#
#
def caseConverter():
	xblankspacex = "*************************"
	ogInput = input("String to Convert: ")
	ccSelect = input("Convert to Upper or Lower? ")
	if ccSelect.lower() == 'u' or "upper":
		print(ogInput.upper())
		#
	elif ccSelect.lower() == 'l' or 'lower':
		print(ogInput.lower())
#
def linuxPing():
	hostname = input("Target")
	sendPing = os.system("ping -c 1 " + hostname)
	if sendPing == 0:
		print(hostname + " is up.")
	else:
		print(hostname + " is down.")
#
def windowPing():
	#
#