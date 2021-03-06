#!/usr/bin/python

import json
import requests
import time
import database

'''
Github unsecured API crawler
@author Misha Frenkman
@version 0.1

'''


githubURL = "https://api.github.com/repositories?since="

def checkReset():
	url = "https://api.github.com/rate_limit"
	resetDate = requests.get(url).json()[u'rate'][u'reset']
	return int(round((resetDate - time.time()) / 60))+1
	
def crawler():
	startID = 0
	
	while True:	
		startID = database.checkLastID() or 0
		req = githubURL+str(startID)
		res = requests.get(req).json()
		
		#Check for the right Github response
		if type(res) is list:
			#Iterate Repos
			for repo in res:
				# Check for private
				if repo[u'private'] == False:
					#Insert Repo in Database
					database.insertRepo(repo[u'id'], repo[u'full_name'], repo[u'html_url'])
		else:
			print "Github kicked me out :( Rate limit reset in: %i minutes" % (checkReset())
			print "Timestamp: %s" % (time.strftime("%d.%m.%Y %H:%M:%S"))
			
			time.sleep(60*10)

crawler()
	