from flask import Flask, render_template, request, session, redirect, url_for
from app.connection import Connection
from app.api import API
from uuid import uuid4

app = Flask(__name__)
app.secret_key = uuid4().bytes


@app.route('/')
def index():

	if session:

		return render_template('index.html')
	else:
		return render_template('login.html')


@app.route('/vm/<string:vm_name>')
def getVM(vm_name):

	if session:

		a = API()
		server = a.loadServer(vm_name)
		
		return render_template('vm.html', srv=server)
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


@app.route('/logout', methods=['POST'])
def logout():
	session['username'] = None
	

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=6969, debug=True)