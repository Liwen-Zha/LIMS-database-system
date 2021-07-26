from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Start Page</h1>'

@app.route('/ttt', methods=['POST'])
def create_task():
    if not request.json:
        print('Failed')
        #abort(400)
    '''task = {
        'sample_ID': request.json['sample_ID'],
        'description': request.json.get('description', ""),
        'done': True
    }'''
    return jsonify({'task':True}), 201

@app.route('/ttt', methods=['GET'])
def get_task():
    return '<h1>ttt page</h1>'

if __name__ == '__main__':
    app.run()
