#coding=utf-8
from aip import AipOcr

config = {
    'appId': '15368290',
    'apiKey': 'T1K5tKlwPmGXPWMlpRscuwzG',
    'secretKey': 'bGqHyrvaCleLsOBnvGlefW1vlAUu0Udz'
}

client = AipOcr(**config)

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    image = get_file_content(image_path)
    result = client.basicGeneral(image)

    if 'words_result' in result:
        return '\n'.join([w['words'] for w in result['words_result']])


if __name__ == '__main__':
    print(img_to_str("/Users/kang/Desktop/phone0/3.png"))