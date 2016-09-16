import BaseHTTPServer

class DamageHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_error(500)

    def do_GET(self):
        if self.path == "/":
            index_file = open("../frontend/index.html")
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(index_file.read())
            index_file.close()
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)
