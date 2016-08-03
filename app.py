import os
from flask import Flask, jsonify, request

app = Flask(__name__)

currid = [{ 'currid': 1 }]

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/todo/api/v1.0/currid', methods=['GET'])
def get_id():
	return jsonify({'currid': currid})

@app.route('/todo/api/v1.0/currid', methods=['POST'])
def post_id():
	if not request.json:
		print "could not find request.json"
	if not 'newid' in request.json:
		print "Jimmy is so terrible he scared newid out of request.json"
	print "okay this should work now"
	print request.json
	currid[0]['currid'] = request.json['newid']
	print currid
	return jsonify({'currid': currid}), 201

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
