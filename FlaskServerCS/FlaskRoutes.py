from flask import Flask, request, jsonify
from Database import MongoP,MongoP1
from predict import retPred

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_array():
    received_array = request.json['array']  
    return (retPred(received_array))

@app.route('/dbd', methods=['POST'])
def received_array1():
    received_array = request.json['array']
    MongoP(received_array)
    response="1"
    return response

if __name__ == '__main__':
    app.run(debug=True)
