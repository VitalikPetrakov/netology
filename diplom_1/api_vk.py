from urllib.parse import urlencode


app_id = 7071031
auth_url = 'https://oauth.vk.com/authorize'
auth_data = {
    'client_id': app_id,
    'display': 'page',
    'scope': 'friends, status, groups',
    'response_type': 'token',
}


print('?'.join((auth_url, urlencode(auth_data))))

token = '9d5bb410e187ed413b6752d1f2719c073b0b79ef92b3ce4445bda3c2419b64d34aa70b068b8c641ed45b4'