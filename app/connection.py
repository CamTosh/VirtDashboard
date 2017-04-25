import json
import code 

class Connection(object):

	def __init__(self):
		f = open("conf.json")
		self.f = json.loads(f.read())
		f.close()

	def login(self, username, password):
		f = self.f['dashboard']

		if username == f['username'] and password == f['password']:
			return self.error(1, "You are connected")
		else:
			return self.error(0, "Username or password ar inccorect")


	def error(self, code, message):
		d = {}
		d['code'] = code
		d['message'] = message

		return d