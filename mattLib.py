#!/usr/bin/env python3
#Library of Functions created by Matt Faulkner, a python beginner.
#
#
import os
import subprocess
import timedate
import getpass

def main():
	#
#
def linuxPing():
	hostname = input("Target")
	sendPing = os.system("ping -c 1 " + hostname)
	if sendPing == 0:
		print(hostname + " is up.")
	else:
		print(hostname + " is down.")
#
def getCreds():
	username = input("Username: ")
	password1 = getpass()
	print("Please enter your password one more time to prevent lockouts...")
	password2 = getpass()
	if password1 != password2:
		print("Passwords did not match. Exiting...")
		raise SystemExit
		