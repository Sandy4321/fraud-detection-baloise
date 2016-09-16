import BaseHTTPServer
from data.data_model import DamageCase
#from detection.rules import RuleDetection

class DamageHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.getheader('content-length', -1))
        if content_len < 0:
            self.send_error(500, "Content length could not be read")
        elif self.path == "/newdamagecase":
            form_data = self.rfile.read(content_len)

            # Generate DamageCase object
            damage_case = DamageCase()
            damage_case.generateFromFormData(form_data)

            self.response_default(form_data)
            # Detect if some rule applies
            #rule_detector = RuleDetection()
            # (fraud, reason) = rule_detector.isFraud(damage_case)
            # if fraud:

            # else:
        elif self.path == "/":
            self.do_GET()
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)




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

    def response_default(self, data):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(data)