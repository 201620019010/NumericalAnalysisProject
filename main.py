from logging import debug
from flask import Flask, request
from flask_restful import Api,Resource,request
from methodHandler import getMethod

app= Flask(__name__)
api=Api(app)

class CallNumericalAnalisisMethods(Resource):
    def get(self):
        return {"data":"Hello World"}

    def post(self):
        methodKey=request.json['key']
        parameters=request.json['parameters']
        return getMethod(methodKey,parameters)




api.add_resource(CallNumericalAnalisisMethods,"/callMethod")

if __name__ == "__main__":
    app.run(debug=True)