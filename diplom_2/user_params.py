# from diplom_2.my_requests import get_users_params
import diplom_2.my_requests
import datetime
from pprint import pprint


# from diplom_2.Vkinder import token


def user_params(token):
    users_params = {}
    response_get_users_params = diplom_2.my_requests.get_users_params(10886452, token)
    list_user_params = response_get_users_params.json()['response']
    users_params['years'] = int(str(datetime.datetime.now())[:4]) - int((list_user_params[0]['bdate'][-4:]))
    users_params['sex'] = list_user_params[0]['sex']
    users_params['city'] = list_user_params[0]['city']['id']
    pprint(list_user_params)
    return users_params
