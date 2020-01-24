import requests


API_KEY = 'trnsl.1.1.20190714T173604Z.9b4e91eef1a8c4bb.58074b97e1b246001f37cc401bc3a872057ade11'

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'



def read_file(file_in):
    with open(file_in, 'rt', encoding='utf-8') as file_in:
        text_for_transl = file_in.readlines()
    return text_for_transl


def get_response(text_in, from_lang, to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': text_in,
        'lang': to_lang.format(from_lang),
    }
    response = requests.get(URL, params=params)
    return response


def get_text_from_response(response):
    json_ = response.json()
    transl_text = ''.join(json_['text'])
    return transl_text


def write_file(file_out, transl_text):
    with open(file_out, 'wt', encoding='utf-8') as file_out:
        file_out.write(transl_text + '\n')


if __name__ == '__main__':
    text = read_file('DE.txt')
    text = ''.join(text)
    response = get_response(text, 'de')
    print(response)
    write_file('de1.txt', get_text_from_response(response))