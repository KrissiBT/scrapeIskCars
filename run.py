import json
import requests


preurl = "http://apis.is/car?number="
url = "http://apis.is/car?number=zz690"
upl = requests.get(url).json()



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




for x in range(100,200):
	url = preurl + 'aa' + str(x)


	try:
		upl = requests.get(url).json()
		print upl["results"][0]["type"]
		print upl["results"][0]["number"]
		print upl["results"][0]["status"]
		print upl["results"][0]["weight"]
		
		print("---------------------------------")
	except Exception:
		print "error printing !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"