from data.data_models import *
#from detection.rules import RuleDetection
#from detection.learn import LearnDetection as LearnDetection
from detection.learn import FakeLearnDetection as LearnDetection

#from data.data_access import DbData as Data
from data.data_access import LocalData as Data

#Handle "/"
def handle_root(request, content_len=0, type="GET"):
    index_file = open("../frontend/index.html")
    request.send_response(200)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(index_file.read())
    index_file.close()


# Handle "/newdamagecase"
def handle_newdamagecase(request, content_len=0, type="GET"):
    # Generate a new damage case
    form_data = request.rfile.read(content_len)

    # Generate DamageCase object
    damage_case = DamageCase()
    damage_case.generateFromFormData(form_data)

    request.DBG_response_default(form_data)
    # Detect if some rule applies
    # rule_detector = RuleDetection()
    # (fraud, reason) = rule_detector.isFraud(damage_case)
    # if fraud:

    # Detect if ML algo tells us something
    # ml_detector = LearnDetector()
    # (fraud, prob) = ml_detector.isFraud(damage_case)
    return NotImplemented


# Handle "/enterpono"
def handle_enterpono(request, content_len=0, type="GET"):
    return NotImplemented


# Handle "/personinfo"
def handle_personinfo(request, content_len=0, type="GET"):
    #Get pono from url
    #Case distinciton, get info from Data object
    return NotImplemented


# Handle all other cases
def handle_404(request):
    request.send_error(404, 'File Not Found: %s' % request.path)

