import json
import code 

class Connection(object):

	def __init__(self):
		f = open("conf.json")
		self.f = json.loads(f.read())
		f.close()

	def login(self, username, password):

		if username == self.f['username'] and password == self.f['password']:
			return self.error(1, "You are connected")
		else:
			return self.error(0, "Username or password ar inccorect")


	def error(self, code, message):
		d = {}
		d['code'] = code
		d['message'] = message

		return d