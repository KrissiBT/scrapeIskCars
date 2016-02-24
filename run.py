import json
import requests


preurl = "http://apis.is/car?number="
url = "http://apis.is/car?number=zz690"
upl = requests.get(url).json()

abc = "abcdefghijklmnopqrstuvwxyz"
char1 = "a"
char2 = "b"
platechars = "something"

numberplatecount = 0


print upl["results"][0]["color"]
print upl["results"][0]["factoryNumber"]
print upl["results"][0]["nextCheck"]
print upl["results"][0]["number"]
print upl["results"][0]["pollution"]
print upl["results"][0]["registeredAt"]
print upl["results"][0]["registryNumber"]
print upl["results"][0]["status"]
print upl["results"][0]["subType"]
print upl["results"][0]["type"]
print upl["results"][0]["weight"]


text_file = open("Output.txt", "w")

for x in range(100,101):
	url = preurl + 'aa' + str(x)



	try:
		upl = requests.get(url).json()
		print upl["results"][0]["type"]
		text_file.write(upl["results"][0]["type"])
		print upl["results"][0]["number"]
		print upl["results"][0]["status"]
		print upl["results"][0]["weight"]
		
		print("---------------------------------")
	except Exception:
		print "error printing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


for x in range(0,26):
	char1 = abc[x]
	for b in range(0,26):
		char2 = abc[b]
		platechars = char1 + char2
		for c in range(1,1000):
			url = preurl + platechars + '{0:0>3}'.format(c)
			
			numberplatecount += 1

			try:
				pass
				print("---------------------------------")
				upl = requests.get(url).json()
				print upl["results"][0]["type"]
				
				print upl["results"][0]["number"]
				print upl["results"][0]["status"]
				print upl["results"][0]["weight"]
		
				print("--------------------------------- \n")
			except Exception:
				print "error printing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print numberplatecount