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
        return jsonify({'errorMsg': "Fail to add sample!"}), 400


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
            searchwho = each[0]
            searchtype = searched_sample_info[i]['type'][1:-1]
            searchsample = each[2]
            searchstatus = searched_sample_info[i]['status'][1:-1]
            searchwhere = each[4]
            searchQvar = searched_sample_info[i]['Qvar']
            searchQvar_unit = searched_sample_info[i]['Qvar_unit'][1:-1]
            searchQnow = searched_sample_info[i]['Qnow']
            searchQnow_unit = searched_sample_info[i]['Qnow_unit'][1:-1]
            searchtime = each[6]

            searchResult = {
                "custodian": searchwho,
                "type": searchtype,
                "status": searchstatus,
                "id": searchsample,
                "loc": searchwhere,
                "Qvar": searchQvar,
                "Qvar_unit": searchQvar_unit,
                "Qnow": searchQnow,
                "Qnow_unit": searchQnow_unit,
                "time": searchtime
            }
            print(searchResult)
            searchResults.append(searchResult)
            i=i+1

        #print(searchResults)
        #print(jsonify(searchResults))
        return jsonify({'Status': '200 OK', 'Method': request.method, 'Data': searchResults})
        #return jsonify(searchResults)

    else:
        return jsonify({"errorMsg": "Fail to search the log(s)!"}), 400

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
            allLogs_who = each[0]
            allLogs_sample = each[2]
            allLogs_where = each[4]
            allLogs_type = all_logs_info[i]['type']
            allLogs_Qvar = all_logs_info[i]['Qvar']
            allLogs_Qvar_unit = all_logs_info[i]['Qvar_unit']
            allLogs_Qnow = all_logs_info[i]['Qnow']
            allLogs_Qnow_unit = all_logs_info[i]['Qnow_unit']
            allLogs_status = all_logs_info[i]['status']
            allLogs_time = each[6]

            logResult = {
                'custodian': allLogs_who,
                'type': allLogs_type,
                'id': allLogs_sample,
                'loc': allLogs_where,
                'Qvar': allLogs_Qvar,
                'Qvar_unit': allLogs_Qvar_unit,
                'Qnow': allLogs_Qnow,
                'Qnow_unit': allLogs_Qnow_unit,
                'time': allLogs_time,
                'status': allLogs_status
            }
            print(logResult)
            logResults.append(logResult)
            i = i + 1

        return jsonify({'Status': '200 OK', 'Method': request.method, 'Data': logResults}), 200

    else:
        return jsonify({"errorMsg": "Fail to view all logs!"}), 400

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
            print(each)

            allSamples_type = each[0]
            allSamples_ID = each[1]
            allSamples_Qnow = each[2]
            allSamples_Qnow_unit = each[3]
            allSamples_where = each[4]
            allSamples_status = each[5]
            allSamples_custodian = each[6]

            sampleResult = {
                'type': allSamples_type,
                'id': allSamples_ID,
                'Qnow': allSamples_Qnow,
                'Qnow_unit': allSamples_Qnow_unit,
                'loc': allSamples_where,
                'status': allSamples_status,
                'latest_custodian': allSamples_custodian
            }

            sampleResults.append(sampleResult)


        return jsonify({'Status': '200 OK', 'Method': request.method,'Data': sampleResults}),200

    else:
        return jsonify({"errorMsg": "Fail to view all samples!"}), 400

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
                               dict_value['status'], dict_value['custodian'])[0]

    if checked_data:
        checkResults = []
        for each in checked_data:
            print(each)
            checktype = each[1]
            checkID = each[3]
            checkQnow = each[5]
            checkQnow_unit = each[7]
            checkwhere = each[9]
            checkstatus = each[11]
            checkcustodian = each[13]

            checkResult = {
                'type': checktype,
                'id': checkID,
                'Qnow': checkQnow,
                'Qnow_unit': checkQnow_unit,
                'loc': checkwhere,
                'status': checkstatus,
                'latest_custodian': checkcustodian,
            }
            checkResults.append(checkResult)

        return jsonify({'Status': '200 OK', 'Method': request.method, 'Data': checkResults}),200

    else:

        return jsonify({"errorMsg": "Fail to check status!"}), 400



