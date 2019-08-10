# Я не сразу понял задание, по этому сделал сначала через логичный метод, а потом сделал как по условию задания
# Рабочая версия программы через метод friends.getMutual


import requests

token = '1fd1d088b6559c699dfa4caf04cf57f0c45e169ea4577673eb1dc3dd248fcfa38489bddad0499de2c1bb5'



class Friends:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_params(self):
        return {
            'access_token': self.token,
            'v': '5.101'
        }

    def request(self, method, params):
        response = requests.get(
            'https://api.vk.com/method/' + method,
            params=params
        )
        return response

    def get_mutual_friends(self, target, source):
        params = self.get_params()
        params['target_uid'] = target.user_id
        params['source_uid'] = source.user_id
        response = self.request(
            'friends.getMutual',
            params=params
        )
        return response.json()['response']

    def get_user_url(self):
        user_id = self.user_id
        return ('https://vk.com/id' + user_id)


user1 = Friends(token, '10886452')
user2 = Friends(token, '8711769')
print(user1.get_mutual_friends(user1, user2))
print(user1.get_user_url())



# Рабочая версия программы через метот friends.get



class User:
    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_params(self):
        return {
            'access_token': self.token,
            'v': '5.52',
            'user_id': self.user_id
        }

    def request(self, method, params):
        response = requests.get(
            'https://api.vk.com/method/' + method,
            params=params
        )
        return response

    def get_friends(self):
        params = self.get_params()
        response = self.request(
            'friends.get',
            params=params
        )
        return set(response.json()['response']['items'])

    def get_user_url(self):
        user_id = self.user_id
        return ('https://vk.com/id' + user_id)


user3 = User(token, '10886452')
user4 = User(token, '8711769')
user3_friends = user1.get_friends()
user4_friends = user2.get_friends()
print(user3_friends & user4_friends)
print(user3.get_user_url())
