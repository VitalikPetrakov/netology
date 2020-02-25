from urllib.parse import urlencode


def get_token_url():
    app_id = 7071031
    auth_url = 'https://oauth.vk.com/authorize'
    auth_data = {
        'client_id': app_id,
        'display': 'page',
        'scope': 'friends, status, groups, photos, audio',
        'response_type': 'token',
    }
    token_url = '?'.join((auth_url, urlencode(auth_data)))
    return token_url


print(get_token_url())


# token = '9536a934fa0dbfdeaed31db8a021e1bc8848c737fe945292f68cf7da903e8f65fa7010e2d4b80bb30e993'
