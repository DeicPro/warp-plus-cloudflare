import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import pathlib

script_version = '4.0.0'
script_title   = f"WARP-PLUS-CLOUDFLARE script By ALIILAPRO (version {script_version})"
os.system('title ' + script_title if os.name == 'nt' else 'PS1="\[\e]0;' + script_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')

print('      _______ _      __________________       _______ _______ _______ _______\n'
'     (  ___  | \     \__   __|__   __( \     (  ___  |  ____ |  ____ |  ___  )\n'
'     | (   ) | (        ) (     ) (  | (     | (   ) | (    )| (    )| (   ) |\n'
'     | (___) | |        | |     | |  | |     | (___) | (____)| (____)| |   | |\n'
'     |  ___  | |        | |     | |  | |     |  ___  |  _____)     __) |   | |\n'
'     | (   ) | |        | |     | |  | |     | (   ) | (     | (\ (  | |   | |\n'
'     | )   ( | (____/\__) (_____) (__| (____/\ )   ( | )     | ) \ \_| (___) |\n'
'     |/     \(_______|_______|_______(_______//     \|/      |/   \__(_______)\n')
print ("[+] ABOUT SCRIPT:")
print ("[-] With this script, you can getting unlimited GB on Warp+.")
print (f"[-] Version: {script_version}")
print ("--------")
print ("[+] THIS SCRIPT CODDED BY ALIILAPRO") 
print ("[-] SITE: aliilapro.github.io") 
print ("[-] TELEGRAM: aliilapro")
print ("--------")

def newID():
	while True:
		referrer  = input("[#] Enter the WARP+ ID:")
		user_input = input(f"[?] Your ID = ({referrer}) is it correct? (y/n):")
		if user_input == "y":
			save_id = input("[?] Do you want to save your ID? (y/n):")
			if save_id == "y":
			    with open("referrer.txt","w") as file:
				    file.write(referrer)
			    return referrer
			elif save_id == "n":
				return referrer
			else:
			    print(f"\"{save_id}\" is not a valid parameter.")
		elif user_input == "n":
			user_input = None
		else:
			print(f"\"{user_input}\" is not a valid parameter.")

def progressBar():
	animation     = ["[□□□□□□□□□□]","[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]"]
	progress_anim = 0
	save_anim     = animation[progress_anim % len(animation)]
	percent       = 0
	while True:
		for i in range(10):
			percent += 1
			sys.stdout.write(f"\r[+] Sending request...  " + save_anim + f" {percent}%")
			sys.stdout.flush()
			if result.is_alive():
				time.sleep(0.1)
			else:
				time.sleep(0.005)
		progress_anim += 1
		save_anim = animation[progress_anim % len(animation)]
		if percent == 100:
			sys.stdout.write("\r[+] Received response.  [■■■■■■■■■■] 100%")
			break

def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    

def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)

url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'

from threading import Thread

class sendRequest(Thread):
	def run(self):
		try:
			install_id  = genString(22)
			body        = {"key": "{}=".format(genString(43)),
					"install_id": install_id,
					"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
					"referrer": referrer,
					"warp_enabled": False,
					"tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
					"type": "Android",
					"locale": "zh-CN"}
			data        = json.dumps(body).encode('utf8')
			headers     = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'}
			req         = urllib.request.Request(url, data, headers)
			response    = urllib.request.urlopen(req)
			status_code = response.getcode()
			self.status = status_code
		except Exception as error:
			self.status = error

if pathlib.Path("referrer.txt").exists():
	while True:
		user_input = input("[?] Do you want to use saved WARP+ ID? (y/n):")
		if user_input == "y":
			with open("referrer.txt","r") as file:
				referrer = file.read().strip()
			break
		elif user_input == "n":
			referrer = newID()
			break
		else:
			print(f"\"{user_input}\" is not a valid parameter.")
else:
	referrer = newID()

g = 0
b = 0
while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print("")
	print(f"                  {script_title}")
	print("")
	result = sendRequest()
	result.start()
	print(f"[-] WORK ON ID: {referrer}")
	progressBar()
	if result.status == 200:
		g += 1
		print(f"\n[#] Total: {g} Good {b} Bad")
		print("")
		print(f"[:)] {g} GB has been successfully added to your account.")
		for i in range(18,0,-1):
			sys.stdout.write(f"\r[*] After {i} seconds, a new request will be sent.")
			sys.stdout.flush()
			time.sleep(1)
	else:
		b += 1
		print(f"\n[#] Total: {g} Good {b} Bad")
		print("")
		print("[:(] Error when connecting to server: " + str(result.status))
		for i in range(18,0,-1):
			sys.stdout.write(f"\r[*] Retrying again in {i} seconds...")
			sys.stdout.flush()
			time.sleep(1)
