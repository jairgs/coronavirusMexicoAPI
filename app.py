from flask import Flask, request
from flask_restful import Resource, Api
import pandas as pd

df=pd.read_csv('https://raw.githubusercontent.com/jairgs/Covid19MexicoDatos/master/allData.csv')
df['Fecha Actualizacion']=df['Fecha Actualizacion'].str.replace('/', '-')

app = Flask(__name__)
api = Api(app)

class TodoSimple(Resource):
    def get(self, fecha):
        print(fecha)
        return df[df['Fecha Actualizacion']==fecha].to_json()

api.add_resource(TodoSimple, '/date/<string:fecha>')

if __name__ == '__main__':
    app.run(debug=False)