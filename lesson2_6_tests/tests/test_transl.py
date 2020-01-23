import unittest
import requests
import transl
from unittest.mock import patch

text_DE = str()
text_ES = ''
text_FR = ''


def setUpModule():
    with open('../text/DE.txt', 'r', encoding='utf-8') as out_DE:
        text_DE.join(out_DE)


print(text_DE)

setUpModule()
print(text_DE)