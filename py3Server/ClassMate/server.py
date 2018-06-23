#
#
#
#Gillian Bryson
#University of Victoria
#V00880054
#Feb 1st 2018
#
#
#

#--IMPORTS--#
import time
import http.server
import sys
import socketserver


#HOST_NAME=134.87.138.158
PORT=8000
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("",PORT),Handler)

print("serving at port ",PORT)

httpd.serve_forever()

"""
def run(myServer=HTTPServer, handler_class=BaseHTTPequestHandler):
	server_address = ('',8000)
	httpd = server_class(server_address, handler_class);
	httpd.serve_forever()
"""

do_get()






