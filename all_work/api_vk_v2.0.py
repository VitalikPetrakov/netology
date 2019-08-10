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

    def __and__(self, other_user):
        other_user_friends = other_user.get_friends()
        user_friends = self.get_friends()
        mutal_user_list = other_user_friends & user_friends
        return mutal_user_list

    def __str__(self):
        return self.get_user_url()

user1 = User(token, '10886452')
user2 = User(token, '8711769')
print(user2 & user1)
print(user2)
