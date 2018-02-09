#
#
#
#
# B. Bird - 02/01/2018

import http.server


class MyHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self):
		print("Got a request")
		self.send_response(200)
		self.send_header('Content-type', 'text/plain')
		self.end_headers()
		response_text = 'Hi\n'
		response_text += 'asdfasdfasfdasdf\nasdfasdf'
		self.wfile.write(bytes(response_text,'UTF-8'))
		for h in self.headers:
			print("Header %s: %s"%(h,self.headers.get(h)))

server = http.server.HTTPServer( ('127.0.0.1',8888), MyHandler)

server.serve_forever()
