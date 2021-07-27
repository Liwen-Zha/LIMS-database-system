from flask import Flask, jsonify, request
import backend

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Start Page</h1>'

@app.route('/sample-log', methods=['POST'])
def log_sample():
    '''
    Log sample transaction
    '''
    dict_value = request.get_json()
    json_value = jsonify(dict_value)
    new_sample = backend.insert(dict_value['sample_type'], dict_value['sample_ID'], dict_value['loc'],
                                dict_value['status'], dict_value['Q'], dict_value['unit'],
                                dict_value['custodian'])
    if new_sample:
        return 'Successfully added {} to the database.'.format(json_value)
    else:
        return jsonify({"errorMsg": "Failed add sample"}), 400

@app.route('/sample-search', methods = ["POST"])
def search_sample():
    '''
    Search sample records
    '''
    dict_value = request.get_json()
    searched_sample = backend.search_improved(dict_value['sample_type'], dict_value['sample_ID'],
                                              dict_value['loc'],dict_value['status'],
                                              dict_value['Q'], dict_value['unit'],
                                              dict_value['custodian'])
    if searched_sample:
        print(searched_sample)
        return 'Successfully searched {} in the database.'.format(dict_value['sample_ID'])
    else:
        return jsonify({"errorMsg": "Failed search sample"}), 400

@app.route('/all-logs', methods = ["GET"])
def view_logs():
    '''
    View all sample records
    i.e., view all transactions stored in the database
    '''
    all_logs = backend.view_logs()

    if all_logs:
        return 'Successfully view the logbook of the database.'
    else:
        return jsonify({"errorMsg": "Failed view the logbook"}), 400

@app.route('/all-samples', methods = ["GET"])
def view_samples():
    '''
    View all samples
    i.e., view all samples' latest profile
    '''
    all_samples = backend.view_samples()

    if all_samples:
        return 'Successfully view all samples in the database.'
    else:
        return jsonify({"errorMsg": "Failed view all samples"}), 400

@app.route('/check', methods = ["POST"])
def check_db():
    '''
    Check the current status of certain sample/freezer/custodian
    i.e., check the latest profile of certain sample;
          check the content in certain freezer;
          check the sample(s) operated by certain custodian
    '''
    dict_value = request.get_json()
    checked_data = backend.check(dict_value['sample_type'], dict_value['sample_ID'], dict_value['loc'],
                                 dict_value['status'], dict_value['custodian'])
    if checked_data:
        return 'Successfully checked status.'
    else:
        return jsonify({"errorMsg": "Failed check status"}), 400


if __name__ == '__main__':
    app.run()
