from string import split
from detection.rules import RuleDetection
#from detection.learn import LearnDetection as LearnDetection
from detection.fake_learn import FakeLearn as LearnDetection

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
    if type == "POST":
        # Generate a new damage case
        form_data = request.rfile.read(content_len)
        parsed_data = read_form_data(form_data)
        damage_no = int(parsed_data["damage_no"])
        parsed_data.pop("damage_no")

        rule_detector = RuleDetection()
        (parsed_data["rule_fraud"], parsed_data["rule_reason"]) = rule_detector.isFraud(damage_no)

        ml_detector = LearnDetection()
        (parsed_data["ml_fraud"], parsed_data["ml_prob"]) = ml_detector.isFraud(damage_no)

        Data.damage_cases[damage_no] = parsed_data

        #TODO: Return to Person Page
    else:
        #TODO: Return Form to input data
        pass
    return NotImplemented


# Handle "/enterpono"
def handle_enterpono(request, content_len=0, type="GET"):
    if type == "POST":
        form_data = request.rfile.read(content_len)
        parsed_data = read_form_data(form_data)


# Handle "/personinfo"
def handle_personinfo(request, content_len=0, type="GET"):
    return NotImplemented


# Handle all other cases
def handle_404(request):
    request.send_error(404, 'File Not Found: %s' % request.path)

def read_form_data(data):
    features = split(data, "&")
    dict = {}
    for feature in features:
        key_and_value = split(feature, "=")
        dict[key_and_value[0]] = key_and_value[1]
    return dict

