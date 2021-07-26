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
