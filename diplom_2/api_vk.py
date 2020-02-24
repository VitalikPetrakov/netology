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


# token = '92b1998dbc5c585641036729b8b95b726b078143cdb772982146e5b2e2c205882f02c66e01c55cdd47229'
