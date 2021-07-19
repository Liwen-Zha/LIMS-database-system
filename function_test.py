import backend
import tools

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
    Q = 10
    unit = 'ml'
    custodian = 'tester'

    # 2. Use hash mark (#) or triple quotes (''') to comment the following test cases
    print('Test result of get_time():')
    test_time = backend.get_time()
    print(test_time)

    print('Test result of insert():')
    if backend.insert(sample_type, sample_ID, loc, status, Q, unit, custodian, test_time):
        print('Done')
    else:
        print('Failed')

    print('Test result of search():')
    test_search = backend.search(sample_type, sample_ID, loc, status, Q, unit, custodian)
    print(test_search)

    print('Test result of view_logs():')
    test_view_logs = backend.view_logs()
    print(test_view_logs)

    print('Test result of view_samples():')
    test_view_samples = backend.view_samples()
    print(test_view_samples)

    print('Test result of check():')
    test_check = backend.check(sample_type, sample_ID, loc, status, custodian)
    print(test_check)

    print('Test result of search_improved():')
    test_search_improved = backend.search_improved(sample_type, sample_ID, loc, status, Q, unit, custodian)
    print(test_search_improved)


