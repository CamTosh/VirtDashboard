# coding: utf-8

from flask import Flask, render_template, request, session, redirect, url_for
from app.connection import Connection
from app.api import API
from app.dashboard import Dashboard
from uuid import uuid4
import json


app = Flask(__name__)
app.secret_key = uuid4().bytes


@app.route('/')
def index():

	if session:
		a = API()
		servers = a.loadServers()

		return render_template('index.html', servers=servers)
	else:
		return render_template('login.html')

@app.route('/vm/<string:vm_name>')
def getVM(vm_name):

	if session:

		a = API()
		server = a.loadServer(vm_name)

		return render_template('vm.html', srv=server, ip=getHost())
	else:
		return render_template('login.html')

@app.route('/vm_action/<string:action>/<string:vm_name>', methods=['POST'])
def action(action, vm_name):

	if session:
		api = API()
		
		if action == "start":
			api.start(vm_name)
			
			return "start"

		elif action == "stop":
			api.stop(vm_name)
			
			return "stop"

		elif action == "delete":
			api.delete(vm_name)
			
			return "delete"

		else:
			return "error"
	else:
		return redirect(url_for('index'))

@app.route('/create')
def create():

	if session:
		d = Dashboard()
		imgs = d.loadImgs()
		
		return render_template('create.html', imgs=imgs)
	else:
		return render_template('login.html')


@app.route('/createvm', methods=['POST'])
def createVM():

	if session:
		
		params = request.form['vm[]']
		"""
		if vm['name'] and vm['backend']:
			a = API()
			a.create(vm)
			
			return redirect(url_for('index'))
		else:
			return redirect(url_for('create'))
		"""
	else:
		return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():

	if session:
		return redirect(url_for('index'))
	else:
		c = Connection()
		conn = c.login(request.form['username'], request.form['password'])

		if conn['code'] == 1:
			session['username'] = request.form['username']
			return redirect(url_for('index'))
		else:
			return render_template('error.html')


@app.route('/logout')
def logout():
	del session['username']
	
	return redirect(url_for('index'))


def getHost():
	f = open("conf.json")
	conf = json.loads(f.read())
	f.close()
	c = conf['dashboard']

	return c

if __name__ == '__main__':

	c = getHost()
	app.run(host=c['ip'], port=c['port'], debug=c['debug'])