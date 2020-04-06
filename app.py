from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd
import os

df=pd.read_csv('https://raw.githubusercontent.com/jairgs/Covid19MexicoDatos/master/allData.csv')
df['Fecha Actualizacion']=df['Fecha Actualizacion'].str.replace('/', '-')

app = Flask(__name__)
api = Api(app)

class getAll(Resource):
    def get(self):
        return df.to_json()

api.add_resource(getAll, '/')

class getDate(Resource):
    def get(self, date):
        return df[df['Fecha Actualizacion']==date].to_json()

api.add_resource(getDate, '/date/<string:date>')

class getState(Resource):
    def get(self, state):
        return df[df['Estado']==str(state)].to_json()

api.add_resource(getState, '/state/<string:state>')

class getDateTotal(Resource):
    def get(self, date):
        return df[df['Fecha Actualizacion']==date].groupby('Estado').size().to_json()

api.add_resource(getDateTotal, '/date/<string:date>/agg')

class getStateTotal(Resource):
    def get(self, state):
        return df[df['Estado']==state].groupby('Fecha Actualizacion').size().to_json()

api.add_resource(getStateTotal, '/state/<string:state>/agg')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=False, port=port)