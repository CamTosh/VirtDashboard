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


	def run(self, action, data):
		r = requests.post(self.addr + action, data=data)
		req = json.loads(r.text)

		return req

	def loadServers(self):
		return self.run("listvm", "null")


	def loadServer(self, name):
		return self.run("getvm", name)


	def create(self, vm):
		d = {}

		d['name'] 	= vm['name']
		d['backend'] = vm['backend']
		
		for k,v in vm['parameters']:
			d[k] = v

		self.run("create", json.dumps(d))


	# VM Actions

	def start(self, name):
		return self.run("startvm", name)

	def stop(self, name):
		return self.run("stopvm", name)

	def delete(self, name):
		return self.run("delvm", name)

	def status(self, name):
		return self.run("statusvm", name)
