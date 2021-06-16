#import flask
from flask import Flask , request, json,jsonify
import requests
import pickle
import numpy as np

app = Flask(__name__)
loaded_model = pickle.load(open("titanic.sav", "rb"))

@app.route("/", methods = ["POST"])
def titanic_predict():
    user_input = request.json
    print(user_input)
    input_list = [user_input["PassengerId"], user_input["Pclass"], user_input["Age"], user_input["SibSp"], user_input["Fare"], user_input["male"], user_input["Q"], user_input["S"]]

    prediction = loaded_model.predict([input_list])
    confidence = loaded_model.predict_proba([input_list])
    response = {}
    response["prediction"] = int(prediction[0])
    response["confidence"] = str(round(np.amax(confidence[0]) *100,2))
    return jsonify(response)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = "5000")