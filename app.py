from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
import json
import socket
import os
import time
import logging
import ConfigParser
from connectivity.TestLogging import TestLogging
from threading import Thread
import socket
import math
from operator import xor

app = Flask(__name__)
api = Api(app)
cwd = os.environ["TEST_HOME"]
cwd_new = cwd.replace("\\", "/")
config = ConfigParser.ConfigParser()
test_path = cwd_new + '/config/' + 'Test_data.cfg'
config.read(test_path)


class TestApplication(Resource):
    def post(self):
        try:
            json_data = request.get_json(force=True)
            A = json_data['A']
            B = json_data['B']
            log_obj = TestLogging(cwd_new)
            logger = log_obj.logger
            logger.info(json_data)
            logger.info("Done")
            output = int(A)+int(B)
            return output
        except Exception as e:
            log_obj = TestLogging(cwd_new)
            logger = log_obj.logger
            logger.error('No data found')
            logger.error('error %s',e)
            return "Fail"
        finally:
            log_obj.logger.handlers[0].close()

api.add_resource(TestApplication, '/iparse')

if __name__ == '__main__':
    #app.run(host=socket.gethostbyname(socket.gethostname()), port=8019, debug=True)
    app.run()
