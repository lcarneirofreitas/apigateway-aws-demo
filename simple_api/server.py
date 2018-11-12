#!/usr/bin/env python
# coding=utf-8
from flask import Flask, jsonify
from flask import request
import socket

app = Flask(__name__)

@app.route('/actions/healthcheck', methods=['GET'])
def get_actions():
    return jsonify({
                    'environment': socket.gethostname(),
                    'path': '/actions'
                  })

@app.route('/queues/healthcheck', methods=['GET'])
def get_queues():
    return jsonify({
                    'environment': socket.gethostname(),
                    'path': '/queues'
                  })

@app.route('/peers', methods=['GET'])
def get_peers_list():
    return jsonify({
                    'Cidao': '05011961651310',
                    'Larigo': '05011961651311',
                    'Igordao': '05011961651312',
                    'Eurico': '05011961651313',
                    '1/2 vida': '05011961651314',
                    'Louis1': '05011961651315',
                    'Louis2': '05011961651312',
                    'Jaime': '05011961651316'
                  })

@app.route('/peers/healthcheck', methods=['GET'])
def get_peers():
    return jsonify({
                    'environment': socket.gethostname(),
                    'path': '/peers'
                  })

@app.route('/calls/healthcheck', methods=['GET'])
def get_calls():
    return jsonify({
                    'environment': socket.gethostname(),
                    'path': '/calls'
                  })

@app.route('/recording/healthcheck', methods=['GET'])
def get_recording():
    return jsonify({
                    'environment': socket.gethostname(),
                    'path': '/recording'
                  })

@app.route('/bulk-recording/healthcheck', methods=['GET'])
def get_bulk():
    return jsonify({
                    'environment': socket.gethostname(),
                    'path': '/bulk-recording'
                  })

@app.route('/ddrs/healthcheck', methods=['GET'])
def get_ddrs():
    return jsonify({
                    'environment': socket.gethostname(),
                    'path': '/ddrs'
                  })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

