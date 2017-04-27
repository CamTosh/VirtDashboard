import json
import requests

class API(object):

	def __init__(self):
		f = open("conf.json")
		j = json.loads(f.read())
		f.close()

		self.addr = j['api']


	def getAddress(self):
		return self.addr


	def loadServers(self):
		r = requests.post(self.addr + "listvm", data="null")
		req = json.loads(r.text)

		return req


	def loadServer(self, name):
		r = requests.post(self.addr + "getvm", data=name)
		req = json.loads(r.text)

		return req


	# VM Actions

	def start(self, name):
		r = requests.post(self.addr + "startvm", data=name)

	def stop(self, name):
		r = requests.post(self.addr + "stopvm", data=name)

	def delete(self, name):
		r = requests.post(self.addr + "delvm", data=name)