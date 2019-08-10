API_KEY = 'trnsl.1.1.20190714T173604Z.9b4e91eef1a8c4bb.58074b97e1b246001f37cc401bc3a872057ade11'

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def read_file(file_in):
    with open(file_in, 'rt', encoding='utf-8') as file_in:
        text_for_transl = file_in.readlines() #.strip()
        if text_for_transl:
            file_in.readline()
    return text_for_transl


def translate_it(file_in, file_out, to_lang, in_lang='ru'):

    params = {
        'key': API_KEY,
        'text': read_file(file_in),
        'lang': in_lang.format(to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    transl_text = ''.join(json_['text'])
    with open(file_out, 'wt', encoding='utf-8') as file_out:
        file_out.write(transl_text + '\n')


translate_it('DE.txt', 'de1.txt', 'de', 'en')
