import vk
import vk_advanced_api


def make_session():
    login = input('Loggin: ')
    password = input('Password: ')
    vk_id = '7071031'
    session = vk.AuthSession(app_id=vk_id, user_login=login, user_password=password)
    return session


vkapi = vk.API(make_session())


api = vk_advanced_api.VKAPI(login='vitalik.petrakov@mail.ru', password='Vpi65852341', app_id='7071031')
print(api.access_token)

