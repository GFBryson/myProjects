#
#
# Gillian Bryson
# V00880054
# Feb 5th 2017
#
#

import http.server

class slackHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		print("GET request found");
		response_text = 'Hello World'
		self.wfile.write(bytes(response_text,'UTF-8'))

server = http.server.HTTPServer (('127.0.0.1',8888), slackHandler)

server.serve_forever();
