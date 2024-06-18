# import ocrspace
# api = ocrspace.API(api_key="K83740406288957")
# res = api.ocr_url('https://api.telegram.org/file/bot6089866995:AAF7TMleVNJABOu_dAwgsS2Pq_zx4-aTd8g/photos/file_0.jpg')

# import requests

# payload = {'url': "https://api.telegram.org/file/bot6089866995:AAF7TMleVNJABOu_dAwgsS2Pq_zx4-aTd8g/photos/file_0.jpg",
#                'isOverlayRequired': False,
#                'apikey': "K83740406288957",
#                'language': "eng",
#                }
# r = requests.post('https://api.ocr.space/parse/image',
#                     data=payload,
#                     )
# print(r.content.decode())

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
OCR_SPACE_KEY = os.getenv("OCR_SPACE_KEY")


def ocr_space_file(filename, overlay=False, api_key=OCR_SPACE_KEY, language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()

def detect_text(file):
    res = ocr_space_file(filename=file)
    json_info = json.loads(res)
    text = json_info['ParsedResults'][0]['ParsedText']
    return text
