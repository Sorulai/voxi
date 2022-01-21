import json

import requests
from voximplant.apiclient import VoximplantAPI, VoximplantException


# aid = 4250226
# api_key = 'a1733d9a-40d3-40ff-b7a5-259175811e84'
# url = 'https://api.voximplant.com/platform_api/CreateKey/'
#
# params = {
#     'account_id': aid,
#     'api_key': api_key
# }
# r = requests.get(url, params=params)
# print(r.json().get('result'))

def decorator(func):
    def wrapper(*args, **kwargs):
        page = {
            "account_email": "sorulaijuli@gmail.com",
            "account_id": 4250226,
            "key_id": "799bcefc-51fc-47ba-8420-bbbb578cd76d",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCeT+fTeIHmhLQ+\nIuIpMRWcrGrffIXcl9mJd5gCSu4jtMVTLddJNwIsNQE8HgExocBb5WKd2OfjvTwq\ndgIzz4e3scrNHD/rmyyhJF/M5FThLAaNkIBqsJUANQgzUXbQJUpfMkAdymff2PVJ\nIdNj00/PTLWCPAv5XY/JMs/i+o4v6M3sJ05B73deM2Ylc/tIKpYTrqTVvJMMN19T\nW9hrtxg1MSBDDxpcs5AdgVu/a7/yvqNkJXGr0rTgAq+HkwfAJuYMSRCVORLRwkJq\nIM8pNPP9ZWfy5MQiUUyam+UgatsCnVIVhs3ewlQHigqiyl12Vec7X4yZsZ0ebuWp\nuWViatznAgMBAAECggEAdm9nCtC7tb4PrfCg65oaBgUDS0C4UGiVyP7cjNKLx9Ck\nUu8XgWGS0Ymx68yyrfPJmbZJCbfM+5aFnWp9iU83xFhRVRNOSq/jOoag2QL08SPj\nnyK8v5RtVCNYiDPoxB0xv3gzeVYEUfXYwyZ4I9Vhfr9vhwfvGVZCjI3j8nXpy7KU\nhWX5y73XODd2P0WIWTz+/TmMhLrzFpXcB/Ja2ILmluRbMIfRAhkWkihoAbIorc84\nScVpQGQFuseBa/9LdT58SRRiJoo+tBFdjD5cENV2fRie8Y4O8m3xJQ07OczyCAoT\nD4BfnWplRbnLcR8myGuxcdfKFeMgqoMnDDi++57GwQKBgQD96RgPPfEkPeXsAb9+\nkfJPfQ2NL56WaxHgf5sJMCsLnhtPnW7WW9sqP+t3OWQd1P/P3HEg3u+5NtEFGIHT\nkqF5XKUEpQLUrXVkFAE2Y8/K76nHSa/ZAlfvD5FXLLgWEm4L436ICxCzErzXMCJU\nQD4cc6N4tD21jHYjkeYrOECWhwKBgQCfnWrNaOzNSSa8tAk+LneEIcLW8aBnFfcR\nmLPMgfrXbqP6Rx0LOJVPVCc2u+SV1JVs4J8DH2N4esDvR9XIK5xGnoAsppqPap3S\ntd0Nurr065bxGyyXye+6mqq63Gz3HFjB+I7f5q3G553/putkfSNWWxosRX/RIWjj\n2PM5Dky+oQKBgQCRxVWrwnsDvImYsfQ3fSCo4/l4ugMJBlVQFtJyNvYviEjTr2Wn\nqTqtCd9sJkXFHrjyo/NK1NK5+a+MhmJajg8oNrkCbp2ubhs8JoP/rtPoBSnqoPJU\n2xSSydQ+QQ06lsAZETVec0PWGwbRX/AFgJBoEzehn5Dh/s8AYs3KuFPUVwKBgD1e\nmyfrRdEQZTJ8zmj4GL/W80ENmizIhzxeyBLDjxyxz551JTehQ9dCdelXiOYK3IEG\nRF1A/k/ecrwNlKboDaghXQrN6/NkfNX9UsbqmuN8iYaeeiDKZcALo8VA5yyD26SI\n2vY/jWVCvL8FANCcRK/5SzDmb+SKwfeI/MtdMijBAoGAFo2zmbNhTTEUomiCX5xf\nU/O4vqANJpKExdvJFlrKaqBz20X2UjXj1K2CJVi/7qrEtEC4F19XVhiBX/cExKcs\ncqdN1X2XNDsSEKGjLCj/P1ba178FMoVxK9jqRxzcquUxZZnX23nCAfjt30/WxB2d\napcOl8g/lNYUZbX5RtMscTU=\n-----END PRIVATE KEY-----\n"

        }
        with open('app/templates/cres.json', 'w', encoding='utf-8') as f:
            json.dump(page, f)
        func()
        with open('app/templates/cres.json', 'w', encoding='utf-8') as f:
            json.dump("", f)
    return wrapper


@decorator
def create_voxi():
    api = VoximplantAPI('app/templates/cres.json')

    USER_NAME = "78ddd98"
    USER_DISPLAY_NAME = "GordonFrehgheman"
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



create_voxi()