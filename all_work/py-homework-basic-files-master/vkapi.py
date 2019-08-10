import requests

token = '8408db2847b42ce25554ffc3dbde01fc205fa008b88e34b6e25a31953d7976e297672b9b3176d9830a8b6'


class User:
    def __init__(self, token):
        self.token = token

    def get_params(self):
        return {
            'access_token': self.token,
            'v': '5.52'
        }

    def request(self, method, params):
        response = requests.get(
            'https://api.vk.com/method/' + method,
            params=params
        )
        return response

    def get_status(self):
        params = self.get_params()
        response = self.request(
            'status.get',
            params=params
        )
        return response.json()['response']

    def set_status(self, text):
        params = self.get_params()
        params['text'] = text
        response = self.request(
            'status.set',
            params=params
        )
        return response.json()['response']


Vitalik = User(token)
status = Vitalik.get_status()
print(status)

