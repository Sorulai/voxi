import requests
from voximplant.apiclient import VoximplantAPI, VoximplantException

aid = 4250226
api_key = 'a1733d9a-40d3-40ff-b7a5-259175811e84'
url = 'https://api.voximplant.com/platform_api/CreateKey/'

params = {
    'account_id': aid,
    'api_key': api_key
}
r = requests.get(url, params=params)
print(r.json())

api = VoximplantAPI("credentials.json")

USER_NAME = "student1"
USER_DISPLAY_NAME = "GordonFreeman"
USER_PASSWORD = "1234567"
APPLICATION_ID = 10569334

try:
    res = api.add_user(USER_NAME,
                       USER_DISPLAY_NAME,
                       USER_PASSWORD,
                       application_id=APPLICATION_ID)

    print(res)
except VoximplantException as e:
    print("Error: {}".format(e.message))
