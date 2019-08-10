import requests

token = 'c366a788656c4b60af958454729a7208170446e980ff2f67fda296ff3032018eae89a595b9be85e88a34b'


# response = requests.get(
#     'https://api.vk.com/method/friends.getMutual',
#     params={
#         'target_uid': '10886452',
#         'source_uid': '8711769',
#         'access_token': token,
#         'v': '5.101'
#     }
# )
#
# print(response.text)



# class Friends:
#
#     def __init__(self, token, user_id):
#         self.token = token
#         self.user_id = user_id
#
#     def get_params(self):
#         return {
#             'access_token': self.token,
#             'v': '5.101'
#         }
#
#     def request(self, method, params):
#         response = requests.get(
#             'https://api.vk.com/method/' + method,
#             params=params
#         )
#         return response
#
#     def get_mutual_friends(self, target, source):
#         params = self.get_params()
#         params['target_uid'] = target.user_id
#         params['source_uid'] = source.user_id
#         response = self.request(
#             'friends.getMutual',
#             params=params
#         )
#         return response.json()['response']
#
#     def get_user_url(self):
#         user_id = self.user_id
#         return ('https://vk.com/id' + user_id)
#
#     def __and__(self, other_user):
#         # id_other_user = other_user.user_id
#         params = self.get_params()
#         params['target_uid'] = other_user.user_id
#         params['source_uid'] = self.user_id
#         response = self.request(
#             'friends.getMutual',
#             params=params
#         )
#         return response.json()['response']
#
#
# user1 = Friends(token, '10886452')
# user2 = Friends(token, '8711769')
# print(user1.get_mutual_friends(user1, user2))
# print(user1.get_user_url())
# print(user1 & user2)


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
user3_friends = user1.get_friends()
user4_friends = user2.get_friends()
print(user2 & user1)
print(user2)