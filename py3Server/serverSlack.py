#
#
# Gillian Bryson
# V00880054
# Feb 5th 2017
# Code assisted by example code written by Bill Bird (assistant teaching professor UVic)
# Code assisted by example from https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
#
#

import http.server

class slackHandler(http.server.BaseHTTPRequestHandler):
	def respond(self):
		self.send_response(200)
		self.send_header('content-type', 'text/plain')
		self.end_headers()

	def do_GET(self):
		self.respond()
		print("GET request found");
		response_text = 'Hello World'
		self.wfile.write(bytes(response_text,'UTF-8'))
	def do_POST(self):
		print("POST request found")
		content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
		post_data = self.rfile.read(content_length) # <--- Gets the data itself
		logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
		str(self.path), str(self.headers), post_data.decode('utf-8'))

		self.respond()
		self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))



server = http.server.HTTPServer (('134.87.136.87',8888), slackHandler)

server.serve_forever();
