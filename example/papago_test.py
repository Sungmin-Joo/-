# -*- coding: utf-8 -*-
import requests

header = {
    'X-Naver-Client-Id' : '--------------------',
    'X-Naver-Client-Secret' : '----------'
}

datas = {
    "source" : "ko",
    "target" : "en",
    "text" : "딸기"
}
url = 'https://openapi.naver.com/v1/language/translate'

response=requests.post(url = url, headers=header, data=datas).json()
print(response['message']['result']['translatedText'])