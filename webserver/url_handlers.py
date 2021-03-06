from string import split
from string import replace
from detection.rules import RuleDetection
#from detection.learn import LearnDetection as LearnDetection
from detection.learn import FakeLearn as LearnDetection
from frontend.personinfo_builder import PersonInfoBuilder

#from data.data_access import DbData as Data
from data.data_access import StaticLocalData as Data

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
        Data.damage_cases[damage_no] = parsed_data
        Data.customers[int(parsed_data["police"])]["damage_cases"].append(damage_no)
        for param in parsed_data:
            string = parsed_data[param]
            parsed_data[param] = replace(string, "+", " ")
        #parsed_data.pop("damage_no")

        rule_detector = RuleDetection()
        (parsed_data["rule_fraud"], parsed_data["rule_reason"]) = rule_detector.isFraud(damage_no)

        ml_detector = LearnDetection()
        parsed_data["ml_prob"] = ml_detector.isFraud(damage_no)
        if parsed_data["ml_prob"] > 0.50:
            parsed_data["ml_fraud"] = True
        else:
            parsed_data["ml_fraud"] = False

        Data.damage_cases[damage_no] = parsed_data

        #Again easiest is just to redirect to localhost/personinfo/pono
        request.send_response(301)
        request.send_header('Location', 'http://localhost:5000/personinfo/' + str(parsed_data["police"]))
        request.end_headers()
    else:
        html_file = open("../frontend/newdamagecase.html")
        request.send_response(200)
        request.send_header('Content-Type', 'text/html')
        request.end_headers()
        request.wfile.write(html_file.read())
    return NotImplemented


# Handle "/enterpono"
def handle_enterpono(request, content_len=0, type="GET"):
    if type == "POST":
        form_data = request.rfile.read(content_len)
        parsed_data = read_form_data(form_data)
        if int(parsed_data["police"]) not in Data.customers:
            handle_404(request)
            return
        #Just read pono from parsed_data and then call handle_personinfo
        #Even simpler would be just redirect to personinfo/pono
        request.send_response(301)
        request.send_header('Location', 'http://localhost:5000/personinfo/' + str(parsed_data["police"]))
        request.end_headers()
    else:
        html_file = open("../frontend/enterpono.html")
        request.send_response(200)
        request.send_header('Content-Type', 'text/html')
        request.end_headers()
        request.wfile.write(html_file.read())

# Handle "/personinfo"
def handle_personinfo(request, content_len=0, type="GET"):
    if type == "POST":
        pass
    else:
        # PoNo should be in URL
        # Build table with function and inject to html file maybe
        # To make it easy create two files: top.html and bottom.html
        # Create table using some function as string
        # Return top.html + tables + bottom.html
        person_info = PersonInfoBuilder()
        police = request.path.rsplit('/', 1)[-1]
        person_info.buildPersonInfo(police)
        request.send_response(200)
        request.send_header('Content-Type', 'text/html')
        request.end_headers()
        request.wfile.write(person_info.toString())

# Handle all other cases
def handle_404(request):
    request.send_error(404, 'File Not Found: %s' % request.path)

#Function to parse POST data to key value pair of form-field-name and form-field-value
def read_form_data(data):
    features = split(data, "&")
    dict = {}
    for feature in features:
        key_and_value = split(feature, "=")
        dict[key_and_value[0]] = key_and_value[1]
    return dict

