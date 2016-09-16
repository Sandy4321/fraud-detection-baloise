import BaseHTTPServer
from url_handlers import *

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', -1))

        if content_len < 0:
            self.send_error(500, "Content length could not be read")
            return

        #Determine which handler to call
        if self.path == "/":
            handle_root(self)
        elif self.path == "/newdamagecase":
            handle_newdamagecase(self, content_len, "POST")
        elif self.path == "/enterpono":
            handle_enterpono(self, content_len, "POST")
        elif self.path == "/personinfo":
            handle_personinfo(self, content_len, "POST")
        else:
            handle_404(self)

    def do_GET(self):

        #Determine which handler to call
        if self.path == "/":
            handle_root(self)
        elif self.path == "/newdamagecase":
            handle_newdamagecase(self)
        elif self.path == "/enterpono":
            handle_enterpono(self)
        elif self.path == "/personinfo":
            handle_personinfo(self)
        else:
            handle_404(self)

    #Default response sending input back for debug
    def DBG_response_default(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(data)