import requests
import jwt

class Meetup(object):
    def token_jwt(self, email):
        key = 'secret'
        jwt_data = {'email':email}
        encoded = jwt.encode(jwt_data, key, algorithm='HS256')
        token_string = encoded.decode('utf-8')
        resp = {
                'success': 'true',
                'token': token_string
                }
        return resp

    def eventos_by_meetup(self, meetup):
        data = []
        url = 'https://api.meetup.com/' + meetup + '/events?&status=upcoming'
        access_token = '{3f3c377256781b4a2d852d4f7e1017}'
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

    def eventos_all(self):
        eventos = []
        meetups = ['PHPSP-Santos', 'MovimentoBaixadaNerd', 'QA-Caiçara', 'dotnet-Sao-Paulo']
        for meetup in meetups:
            result = self.eventos_by_meetup(meetup)
            for evento in result:
                eventos.append(evento)
        return eventos

    def eventos_meetup(self, meetup):
        eventos = []
        result = self.eventos_by_meetup(meetup)
        for evento in result:
            eventos.append(evento)
        return eventos
