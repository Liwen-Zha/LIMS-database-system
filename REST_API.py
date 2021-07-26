from flask import Flask, jsonify, request
from flask_cors import CORS
from py2neo import *
import json
import backend as be

app = Flask(__name__)
CORS(app)

NEO4j_URL= "http://localhost:7474"
NEO4j_USERNAME = "neo4j"
NEO4j_PASSWORD = "database_1"
graph = Graph(NEO4j_URL, auth=(NEO4j_USERNAME, NEO4j_PASSWORD))

@app.route('/')
def home():
    return '<h1>Start Page</h1>'

# Register sample
@app.route('/sample-registration', methods = ["POST"])
def register_sample():
    #data_json = request.data
    #values = json.loads(data_json)
    values = request.get_json()
    new_sample = be.insert(values['sample_type'], values['sample_ID'], values['loc'], values['status'],
                           values['Q'], values['unit'], values['custodian'])
    '''new_sample = be.insert(request.json['sample_type'], request.json['sample_ID'], request.json['loc'],
                           request.json['status'], request.json['Q'], request.json['unit'],
                           request.json['custodian'])'''
    if new_sample:
        return 'Successfully added {} to the database.'.format(values['sample_ID'])
    else:
        return jsonify({"errorMsg": "Failed add sample"}), 400

# Search sample
@app.route('/sample-search', methods = ["POST"])
def search_sample():
    values = request.get_json()
    searched_sample = be.search_improved(values['sample_type'], values['sample_ID'], values['loc'],
                                         values['status'],values['Q'], values['unit'],
                                         values['custodian'])
    if searched_sample:
        return 'Successfully searched {} in the database.'.format(values['sample_ID'])
    else:
        return jsonify({"errorMsg": "Failed search sample"}), 400

# View all sample logs
@app.route('/all-logs', methods = ["GET"])
def view_logs():
    all_logs = be.view_all

    if all_logs:
        return 'Successfully view the logbook of the database.'
    else:
        return jsonify({"errorMsg": "Failed view the logbook"}), 400

# View all samples
@app.route('/all-samples', methods = ["GET"])
def view_samples():
    all_samples = be.view_samples

    if all_samples:
        return 'Successfully view all samples in the database.'
    else:
        return jsonify({"errorMsg": "Failed view all samples"}), 400

# Check certain sample/freezer/custodian
@app.route('/database-check', methods = ["POST"])
def check_db():
    values = request.get_json()
    checked_data = be.search_improved(values['sample_type'], values['sample_ID'], values['loc'],
                                       values['status'],values['custodian'])
    if checked_data:
        return 'Successfully checked status.'
    else:
        return jsonify({"errorMsg": "Failed check status"}), 400


if __name__ == '__main__':
    app.run()





