from flask import Flask, url_for, redirect, render_template, request, session
from flask_restplus import Api, Resource
from app.meetup.meetup import Meetup
from flask_cors import CORS, cross_origin


# pylint: disable=C0103
app = Flask(__name__)
app.secret_key = 'development'
CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


@app.route('/home')
def index():
    return render_template('index.html')


@api.route('/login')
class GetCode(Resource):
    def get(self):
        if 'code' in request.args:
            code = request.args
            token = Meetup.get_acees_token(self, code=code['code'])
            session['meetup_token'] = token['access_token']
            return redirect(url_for('index'))
        else:
            erro = {'erro':'Do not have token'}
            return erro
@api.route('/logoff')
class Logoff(Resource):
    def get(self):
        session.pop('meetup_token')
        return redirect(url_for('index'))


@api.route('/api/v1/eventos/')
class EventosGeral(Resource):
    def get(self, access_token):
        # access_token = session.get('meetup_token')
        eventos = Meetup().eventos_all(access_token=access_token)
        return eventos

@api.route('/api/v1/eventos/<string:meetup>')
class Eventos(Resource):
    def get(self, meetup):
        access_token = session.get('meetup_token')
        eventos = Meetup()
        return eventos.eventos_meetup(meetup, access_token=access_token)

@api.route('/login/authoraze')
class Login(Resource):
    def get(self):
        url_autorization = Meetup.authorize_access(self)
        return url_autorization

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='127.0.0.1', port=port , debug=True)
