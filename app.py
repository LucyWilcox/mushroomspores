import os
from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
import psycopg2
import config as config

app = Flask(__name__)
# app.config(os.environ['DATABASE_URL'])
# app.config.from_pyfile('config.py')


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/todo/api/v1.0/currid', methods=['GET'])
def get_id():
	# database_URI = config.DATABASE_URI
	database_URI = os.environ['DATABASE_URI']
	conn = psycopg2.connect(database_URI)
	curr = conn.cursor()
	curr.execute("SELECT * FROM CurrentId;")
	curr_id = curr.fetchone()[1]
	print curr_id
	conn.commit()
	curr.close()
	conn.close()
	return jsonify({'currid': curr_id}), 200

@app.route('/todo/api/v1.0/currid', methods=['POST'])
def post_id():
	# database_URI = config.DATABASE_URI
	database_URI = os.environ['DATABASE_URI']
	if not request.json:
		print "could not find request.json"
	if not 'newid' in request.json:
		print "no newid in request.json"
	print "okay this should work now"
	print request.json
	conn = psycopg2.connect(database_URI)
	curr = conn.cursor()
	curr_id = request.json['newid']
	print curr_id
	sql = "UPDATE CurrentId SET curr_id = %s WHERE id = 1" %(curr_id)
	print sql
	curr.execute(sql)
	conn.commit()
	curr.close()
	conn.close()
	return jsonify({'currid': curr_id}), 201

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)