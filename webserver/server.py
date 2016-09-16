import BaseHTTPServer
from data.data_model import DamageCase

class DamageHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', -1))
        if content_len < 0:
            self.send_error(500, "Content length could not be read")
        else:
            form_data = self.rfile.read(content_len)
            damage_case = DamageCase()
            damage_case.generateFromFormData(form_data)
            


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
