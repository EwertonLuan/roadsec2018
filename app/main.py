import os
import requests
from flask import Flask
from flask_restplus import Api, Resource
from meetup.meetup import Meetup
import jwt

# pylint: disable=C0103
app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/token/<string:email>')
class TokenJwt(Resource):
    def get(self, email):
        token = Meetup().token_jwt(email)
        return token

@api.route('/api/v1/eventos/')
class EventosGeral(Resource):
    def get(self):
        eventos = Meetup().eventos_all()
        return eventos

@api.route('/api/v1/eventos/<string:meetup>')
class Eventos(Resource):
    def get(self, meetup):
        eventos = Meetup()
        return eventos.eventos_meetup(meetup)

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='127.0.0.1', port=port, debug=True)
