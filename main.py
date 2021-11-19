from logging import debug
from flask import Flask, request
from flask_restful import Api,Resource,request
from methodHandler import getMethod
from flask_cors import CORS

app= Flask(__name__)
api=Api(app)
CORS(app)

class CallNumericalAnalisisMethods(Resource):
    def get(self):
        return {"data":"Hello World"}

    def post(self):
        methodKey=request.json['key']
        parameters=request.json['parameters']
        return getMethod(methodKey,parameters)





api.add_resource(CallNumericalAnalisisMethods,"/callMethod")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
    #app.run(debug=True)
