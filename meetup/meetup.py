import requests

class Meetup(object):
    def eventos_by_meetup(self,meetup):
        data = []
        url = 'https://api.meetup.com/' + meetup + '/events?&status=upcoming'
        access_token = '{3f3c377256781b4a2d852d4f7e1017}'
        headers = {
            'Authorization': 'Bearer' + access_token,
            'sign': 'True',
        }
        response = requests.get(url,headers=headers)
        events = response.json()
        if len(events) > 0: # 0 = Sem eventos
            for event in events:
                dict = {}
                group = event['group']['name']
                name = event['name']
                address_1 = event['venue']['address_1']
                city = event['venue']['city']
                dict['organizador'] = group
                dict['nome'] = name
                dict['endereco'] = address_1
                dict['cidade'] = city
                data.append(dict)
        return data

    def eventos_all(self):
        eventos = []
        meetups = ['PHPSP-Santos', 'MovimentoBaixadaNerd','QA-Caiçara','dotnet-Sao-Paulo']
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



#for meetup in meetups:
#    print(eventos.eventosByMeetup(meetup))
