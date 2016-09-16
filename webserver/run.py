from webserver.server import RequestHandler
import BaseHTTPServer

HOST_NAME = "127.0.0.1"
PORT_NUMBER = 5000

server_class = BaseHTTPServer.HTTPServer
server = server_class((HOST_NAME, PORT_NUMBER), RequestHandler)
server.serve_forever()