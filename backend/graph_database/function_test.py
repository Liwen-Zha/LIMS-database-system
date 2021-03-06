import model

'''
  function_test.py:
  This file is to test and verify that each of the functions in the backend.py and tools.py 
  can work correctly. 
'''

if __name__ == "__main__":
    # 1. Change the value of the following variables to get different test results
    sample_type = 'test1'
    sample_ID = 't002'
    loc = 'test_f1'
    status = 'ok'
    Q = 20
    unit = 'ml'
    custodian = 'tester'


    # 2. Use hash mark (#) or triple quotes (''') to comment the following test cases
    print('Test result of get_time():')
    test_time = model.get_time()
    if test_time:
        print(test_time)
    else:
        print('no test_time')

    print('\nTest result of insert():')
    if model.insert(sample_type, sample_ID, loc, status, Q, unit, custodian, test_time):
        print('Insert Done')
    else:
        print('Insert Failed')

    print('\nTest result of search():')
    test_search = model.search(sample_type, sample_ID, loc, status, Q, unit, custodian)
    if test_search:
        print(test_search)
    else:
        print('no test_search')

    print('\nTest result of view_logs():')
    test_view_logs = model.view_logs()[0]
    if test_view_logs:
        for each in test_view_logs:
            print(each)
    else:
        print('no test_view_logs')

    print('\nTest result of view_samples():')
    test_view_samples = model.view_samples()[0]
    if test_view_samples:
        for each in test_view_samples:
            print(each)
    else:
        print('no test_view_samples')

    print('\nTest result of check():')
    test_check = model.check(sample_type, sample_ID, loc, status, custodian)[0]
    if test_check:
        print(test_check)
    else:
        print('no test_result')

    print('\nTest result of search_improved():')
    test_search_improved = model.search_improved(sample_type, sample_ID, loc, status, Q,
                                                 unit, custodian)[0]
    if test_search_improved:
        print(test_search_improved)
    else:
        print('no test_search_improved')


