import requests
import json
import serial
import time

#url = 'http://gabriuuuus.com'
card = 1234567
amount = float(input())
print amount
concept = 'Cocacola'
time.sleep (5)
print "charging " +str(amount) + " to the card number " + str(card)
time.sleep(1)
print "please wait"
time.sleep(1)
print "please wait"
time.sleep(5)
#payload = {'card': card , 'amount': amount , 'concept': concept }
#r2 = requests.post(url, data=payload)
print "Payment accepted"
