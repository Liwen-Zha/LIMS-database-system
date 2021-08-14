from flask import render_template, jsonify, request
from flask import Blueprint

from backend.graph_database import model


main = Blueprint('main', __name__, template_folder='templates', static_folder='static', static_url_path="/static")

@main.route('/')
def show_home():
    return render_template('index.html')

@main.route('/log', methods=['POST'])
def log_sample():
    '''
    Log sample transaction
    '''

    # Here dict_value is 'dict'; json_value is 'flask.wrappers.Response'
    dict_value = request.get_json()

    new_sample = model.insert(dict_value['sample_type'], dict_value['sample_ID'], dict_value['loc'],
                              dict_value['status'], dict_value['Q'], dict_value['unit'],
                              dict_value['custodian'])

    if new_sample:
        sampleInfo = {
            'type': dict_value['sample_type'],
            'id': dict_value['sample_ID'],
            'loc': dict_value['loc'],
            'status': dict_value['status'],
            'Qvar': dict_value['Q'],
            'Qvar_unit': dict_value['unit'],
            'custodian': dict_value['custodian']
        }
        print(sampleInfo)
        return jsonify({'Status': '200 OK', 'Method': request.method, 'Data': sampleInfo})
    else:
        print("sample log failed")
        return jsonify({"errorMsg": "Failed add sample"}), 400


@main.route('/search', methods = ["POST"])
def search_sample():
    '''
    Search sample records
    '''
    dict_value = request.get_json()
    searched_sample = model.search_improved(dict_value['sample_type'], dict_value['sample_ID'],
                                            dict_value['loc'], dict_value['status'],
                                            dict_value['Q'], dict_value['unit'],
                                            dict_value['custodian'])[0]
    searched_sample_info = model.search_improved(dict_value['sample_type'], dict_value['sample_ID'],
                                            dict_value['loc'], dict_value['status'],
                                            dict_value['Q'], dict_value['unit'],
                                            dict_value['custodian'])[1]
    if searched_sample:
        i = 0
        searchResults = []
        for each in searched_sample:
            who = each[0]
            thistype = searched_sample_info[i]['type']
            thissample = each[2]
            where = each[4]
            thisQvar = searched_sample_info[i]['Qvar']
            thisQvar_unit = searched_sample_info[i]['Qvar_unit']
            thisQnow = searched_sample_info[i]['Qnow']
            thisQnow_unit = searched_sample_info[i]['Qnow_unit']
            thistime = each[6]

            searchResult = {
                "custodian": who,
                "type": type,
                "id": thissample,
                "loc": where,
                "Qvar": thisQvar,
                "Qvar_unit": thisQvar_unit,
                "Qnow": thisQnow,
                "Qnow_unit": thisQnow_unit,
                "time": thistime
            }
            print(searchResult)
            searchResults.append(searchResult)
            i=i+1

        print(searchResults)
        print(jsonify(searchResults))
        return jsonify(searchResults)

    else:
        return jsonify({"errorMsg": "Failed search sample"}), 400

@main.route('/view-logs', methods = ["GET"])
def view_logs():
    '''
    View all sample records
    i.e., view all transactions stored in the database
    '''
    all_logs = model.view_logs()[0]
    all_logs_info = model.view_logs()[1]

    if all_logs:
        i=0
        logResults = []
        for each in all_logs:
            who = each[0]
            sample = each[2]
            where = each[4]
            Qvar = all_logs_info[i]['Qvar']
            Qvar_unit = all_logs_info[i]['Qvar_unit']
            Qnow = all_logs_info[i]['Qnow']
            Qnow_unit = all_logs_info[i]['Qnow_unit']
            time = each[6]

            logResult = {
                'custodian': who,
                'id': sample,
                'loc': where,
                'Qvar': Qvar,
                'Qvar_unit': Qvar_unit,
                'Qnow': Qnow,
                'Qnow_unit': Qnow_unit,
                'time': time
            }

            logResults.append(logResult)
            i = i + 1

        return jsonify({'Status': '200 OK', 'Method': request.method, 'Data': logResults}), 200

    else:
        return jsonify({"errorMsg": "Failed view the logbook"}), 400

@main.route('/view-samples', methods = ["GET"])
def view_samples():
    '''
    View all samples
    i.e., view all samples' latest profile
    '''
    all_samples = model.view_samples()[1]
    if all_samples:
        sampleResults = []
        for each in all_samples:
            type = each[0]
            ID = each[1]
            Qnow = each[2]
            Qnow_unit = each[3]
            where = each[4]
            status = each[5]
            custodian = each[6]

            sampleResult = {
                'type': type,
                'id': ID,
                'Qnow': Qnow,
                'Qnow_unit': Qnow_unit,
                'loc': where,
                'status': status,
                'latest_custodian': custodian
            }

            sampleResults.append(sampleResult)
            print(each)

        return jsonify({'Status': '200 OK', 'Method': request.method,'Data': sampleResults}),200

    else:
        return jsonify({"errorMsg": "Failed view all samples"}), 400

@main.route('/check', methods = ["POST"])
def check_db():
    '''
    Check the current status of certain sample/freezer/custodian
    i.e., check the latest profile of certain sample;
          check the content in certain freezer;
          check the sample(s) operated by certain custodian
    '''
    dict_value = request.get_json()


    checked_data = model.check(dict_value['sample_type'], dict_value['sample_ID'], dict_value['loc'],
                               dict_value['status'], dict_value['custodian'])[1]
    if checked_data:
        checkResults = []
        for each in checked_data:
            type = each[0]
            ID = each[1]
            Qnow = each[2]
            Qnow_unit = each[3]
            where = each[4]
            status = each[5]
            custodian = each[6]

            checkResult = {
                'type': type,
                'id': ID,
                'Qnow': Qnow,
                'Qnow_unit': Qnow_unit,
                'loc': where,
                'status': status,
                'latest_custodian': custodian,
            }
            checkResults.append(checkResult)
            print(each)

        return jsonify({'Status': '200 OK', 'Method': request.method, 'Data': checkResults}),200

    else:

        return jsonify({"errorMsg": "Failed check status"}), 400



