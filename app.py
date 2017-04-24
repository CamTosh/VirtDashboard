from flask import Flask, render_template, request, session, redirect, url_for
from app.connection import Connection
from uuid import uuid4

app = Flask(__name__)
app.secret_key = uuid4().bytes



@app.route('/')
def index():
	if session:
		return render_template('index.html')
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
	session.pop('username', None)
	

if __name__ == '__main__':
	app.run(debug=True)