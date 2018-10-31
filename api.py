import os
import requests
from flask import Flask
from flask_restplus import Api, Resource
from meetup.meetup import Meetup

app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/eventos')
class EventosGeral(Resource):
    def get(self):
        eventos = Meetup()
        return eventos.eventos_all()

@api.route('/api/v1/eventos/<string:meetup>')
class Eventos(Resource):
    def get(self, meetup):
        eventos = Meetup()
        return eventos.eventos_meetup(meetup)



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port , debug=True)