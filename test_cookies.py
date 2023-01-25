from urllib import request
import json
from threading import Thread, Lock
import random
import string
import time
import requests
import http.cookiejar


# printing lowercase
letters = string.ascii_lowercase

PORT=10000
PROXY_USER = 'spcmp28zj1' 
PROXY_PASS = '123123123'
PROXY_URL_BASE = 'http://'+PROXY_USER+':'+PROXY_PASS+'@gb.smartproxy.com:PORT'

attackList = [
'https://www.business2community.com',
# 'https://x-bitcoin-club.com'
]

def checkIp(proxies):
	ipUrl='https://api.ipify.org'
	print(requests.get(ipUrl, proxies=proxies).content)
	# input()


def checkmyHeaders():
	url='http://myhttpheader.com/'
	data = {"cmd": "request.get",
			"url": url,
			}
	resStr = requests.post(flareSolverUrl, json=data).content
	print(resStr)
	input()

	print(requests.get('http://myhttpheader.com/').content)
	input()

def changeProxies():
	PORT=random.randrange(30001,32048)
	PROXY_URL = PROXY_URL_BASE.replace('PORT',str(PORT))

	proxies = {
   'http': PROXY_URL,
   'https': PROXY_URL,
	}

	return PROXY_URL, proxies

def my_handler(request, exception):
    print(f"exception thrown by grequests: \n{exception}")
    return request

cookies={'asdasd':'123123123'}
print(requests.get('http://httpbin.org/cookies', cookies=cookies).content)
input()
		