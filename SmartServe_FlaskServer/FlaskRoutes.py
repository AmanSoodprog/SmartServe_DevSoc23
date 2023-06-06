from flask import Flask, request, jsonify
from Database import MongoP,MongoP1
from predict import retPred
import requests


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

@app.route('/bet1', methods=['POST'])
def received_array3():
    aProb=request.json['string']
  

    API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
    headers = {"Authorization": "Bearer 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"}


    with open('C:/Users/sooda/Desktop/Folders/Cprogfiles/.vscode/PYTHON/data.txt', 'r') as file:
        # Read the contents of the file
        contents = file.read()

    text = contents

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": {
            "question": aProb,
            "context": text
        },
    })
    value_string = output['answer']

    print(value_string)
    return value_string


if __name__ == '__main__':
    app.run(debug=True)
