import json
import os

class Dashboard(object):

	def __init__(self):
		f = open("conf.json")
		j = json.loads(f.read())
		self.j = j['dashboard']
		f.close()


	def loadImgs(self):
		path = self.j['iso_path']
		res = os.listdir(path)

		d = {}
		d['path'] = path
		d['img'] = res

		return d