#!/usr/bin/python

from peewee import *

db = MySQLDatabase('Repo', user='root', passwd='')


class Repo(Model):
	repoID = IntegerField()
	repoName = CharField()
	repoURL = CharField()
	repoAPI = CharField()
	
	class Meta:
		database = db

	
def insertRepo(repoid, name, url):
	Repo.create(repoID=repoid, repoName=name, repoURL=url)
		
def insertApi(repoid, api):
	Repo.update(repoAPI=api).where(Repo.repoID==repoid).execute()
	
def checkLastID():
	return Repo.select(fn.Max(Repo.repoID)).get().repoID
	
def getUrlByID(repoid):
	return Repo.get(Repo.repoID == repoid).repoURL