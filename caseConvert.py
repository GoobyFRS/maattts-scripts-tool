#!/usr/bin/env python3
#Library of Functions created by Matt Faulkner, a python beginner.
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
def main():
        caseConverter()
main()
