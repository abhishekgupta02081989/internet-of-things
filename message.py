import requests

import time

from twilio.rest import TwilioRestClient 

for i in range(0,100):
	req = requests.get('https://data.sparkfun.com/output/aGOE6rY5mxcxX1GNnOKq.json?')
	if req.status_code != 200:
		continue
	data = req.json()
	#print data
	print data[i]['light']
	print data[i]['user']
	if(data[i]['user']=="agupta12/skottur" and data[i]['temperature'] <10):
		ACCOUNT_SID = "AC9fdb651e85c60e40622cc5a41eeb61ec" 
		AUTH_TOKEN = "0d4cd7b95d6c688d5d02bbc665a654ad" 
 
		client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
		client.messages.create(
		to="3308120800", 
		from_="+13305765860", 
		body="It's cold outside !!!!",  
		)
