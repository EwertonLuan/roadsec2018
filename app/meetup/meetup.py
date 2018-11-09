import requests
from urllib import parse

class Meetup(object):
    def eventos_by_meetup(self, meetup, access_token):
        data = []
        url = 'https://api.meetup.com/' + meetup + '/events?&status=upcoming'

        headers = {
            'Authorization': 'Bearer' + access_token,
            'sign': 'True',
        }
        response = requests.get(url, headers=headers)
        events_response = response.json()
        count = len(events_response)
        if count > 0: # 0 = Sem eventos
            for event in events_response:
                data_events = {}
                group = event['group']['name']
                name = event['name']
                address_1 = event['venue']['address_1']
                city = event['venue']['city']
                data_events['organizador'] = group
                data_events['nome'] = name
                data_events['endereco'] = address_1
                data_events['cidade'] = city
                data.append(data_events)
        return data



    def eventos_all(self, access_token):
        eventos = []
        meetups = ['PHPSP-Santos', 'MovimentoBaixadaNerd', 'QA-Caiçara', 'dotnet-Sao-Paulo']
        for meetup in meetups:
            result = self.eventos_by_meetup(meetup, access_token)
            for evento in result:
                eventos.append(evento)
        return eventos

    def eventos_meetup(self, meetup, access_token):
        print("start")
        eventos = []
        result = self.eventos_by_meetup(meetup, access_token)
        for evento in result:
            eventos.append(evento)
        return eventos

    def authorize_access(self):

        params = {'response_type':'code',
                    'client_id':'lklk38nu460hho48rr9sisa9qg',
                    'redirect_uri':'http://localhost:5000/login'}

        url = 'https://secure.meetup.com/oauth2/authorize'

        params = parse.urlencode(params)

        url_autorization = url+'?'+params

        return url_autorization

    def get_acees_token(self, code):

        r = requests.post('https://secure.meetup.com/oauth2/access',
                        data={'client_id':'lklk38nu460hho48rr9sisa9qg',
                            'client_secret':'f0662cchdctub86gg5qrpi6geo',
                            'grant_type': 'authorization_code',
                            'redirect_uri': 'http://localhost:5000/login',
                            'code': code
                            })
        # print(r.json())
        return r.json()

    
        


