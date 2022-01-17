from voximplant.apiclient import VoximplantAPI, VoximplantException

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
