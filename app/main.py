from flask import Flask, url_for, redirect, render_template, request, session
from flask_restplus import Api, Resource
from app.meetup.meetup import Meetup


# pylint: disable=C0103
app = Flask(__name__)
app.secret_key = 'development'
api = Api(app)

@app.route('/home')
def index():
    if 'meetup_token' in session:
        
        print(session.get('meetup_token'))
    return render_template('index.html')


@api.route('/login')
class GetCode(Resource):

    def get(self):
        
        if 'code' in request.args:
            code = request.args
            token = Meetup.get_acees_token(self, code=code['code'])
            # print(token['access_token'])
            session['meetup_token'] = token['access_token']
            return token

        else:
            erro = {'erro':'Do not have token'}
            return erro

@api.route('/api/v1/eventos/')
class EventosGeral(Resource):
    def get(self):
        access_token = session.get('meetup_token')
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
        return redirect(url_autorization)

# if __name__ == '__main__':
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='127.0.0.1', port=port , debug=True)
