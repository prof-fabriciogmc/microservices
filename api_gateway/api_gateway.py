from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from urllib import parse, request as req


app = Flask(__name__)
CORS(app)


# This simulates service data that should come from database or
# configuration file.
sum_service_config = {'route':'/cripto', 'address':'localhost', 'port':5001}
mult_service_config = {'route':'/lower_case', 'address':'localhost', 'port':5000}


service_registry = [sum_service_config, mult_service_config]

@app.route('/api_gateway/<operation>')
def api_gateway(operation):
    for service_config in service_registry:
        if service_config['route'] == ('/'+operation):
            parameters = { 'str_input': request.args.get('str_input')}
            url = 'http://' + service_config['address'] +':' + str(service_config['port']) + service_config['route']
            url_request = req.urlopen(url+'?'+parse.urlencode(parameters))
            result = url_request.read()
            return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)

