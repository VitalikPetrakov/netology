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

token = ''