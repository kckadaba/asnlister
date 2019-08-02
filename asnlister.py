#!/usr/bin/env python
#Author Neat

import urllib2
from bs4 import BeautifulSoup

bgp_he = "http://bgp.he.net/search?search[search]=$1&commit=Search"

print "[+] This program lists out ASN's of Respective country. [+]\n"
abbre = raw_input("Enter the abbreviation of country: ")

url = bgp_he + abbre

def soup_call():
	try:
		request = urllib2.Request(url, headers={'User-Agent':'Mozilla/5.0'})
		html = urllib2.urlopen(request)
		soup = BeautifulSoup(html,'html.parser')
		for a in soup.find_all('a',title=True):
			print "Allocated ASNs: ", a['title']

#	print (soup.prettify())
	except:
		print "\nSomething went wrong! Maybe You should check out abbreviation for the respective country!"

def main():
	soup_call()

if __name__ == '__main__':
	main()

