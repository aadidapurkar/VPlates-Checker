import requests
from datetime import datetime

from itertools import product
from string import ascii_lowercase
keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 3)]
availPlates = []

def check(platename):
    end_no = round(datetime.timestamp(datetime.now()))
    r = str(requests.get("https://vplates.com.au/vplatesapi/checkcombo?vehicleType=car&combination="+ platename + "&_=" + str(end_no)).content)
    if "true" in r:
        availPlates.append(platename)
        print(availPlates)
    else:
        print("plate not available. moving on to next plate")

for i in keywords:
    check(i)
