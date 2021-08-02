# Testing GET
curl -v  --request GET http://127.0.0.1:5000/route1

# Testing POST
curl -v --header "Content-Type: application/json" --request POST --data '{"hello":"world","message":"This is my JSON message"}' http://127.0.0.1:5000/route2

# Testing GET + key/value
curl -v --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/route3?user=alice

# Testing GET + key/value
curl -v --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/route3?key=value

# Testing PUT 
curl -v --header "Content-Type: application/json" --request PUT http://127.0.0.1:5000/route4/bob


####################################Start to test REST_API.py####################################
'''
# Testing route: sample-registration in REST_API
curl -v --header "Content-Type: application/json" --request POST --data '{"sample_type":"blood","sample_ID":"blo789","loc":"f2","status":"ok","Q":-5,"unit":"ml","custodian":"mary"}' http://127.0.0.1:5000/sample-log

# Testing route: sample-search in REST_API
curl -v --header "Content-Type: application/json" --request POST --data '{"sample_type":"blood","sample_ID":"blo789","loc":"","status":"","Q":"","unit":"","custodian":""}' http://127.0.0.1:5000/sample-search

# Testing route: all-logs in REST_API
curl -v --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/all-logs

# Testing route: all-samples in REST_API
curl -v --header "Content-Type: application/json" --request GET http://127.0.0.1:5000/all-samples

# Testing route: check in backup-api
curl -v --header "Content-Type: application/json" --request POST --data '{"sample_type":"","sample_ID":"blo789","loc":"","status":"","Q":"","unit":"","custodian":""}' http://127.0.0.1:5000/check

'''