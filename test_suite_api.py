import requests
import pytest
import json
from requests.auth import HTTPBasicAuth

main_url = "http://qhost:1050/"
login_url = "api/account/login"


class APICore(object):

    def __init__(self, url, username, password):
        self._session = self.login(url, username, password)

    def login(self, url, username, password):
        payload = {"userName": username, "password": password}
        session = requests.session()
        session.post(url="{0}{1}".format(main_url, url), json=payload)
        return session

    def get_cashrequisition_document(self, id):
        _url = '{0}api/bank/documents/cashrequisition/{1}'.format(main_url, id)
        r = self._session.get(url=_url)
        print(r.text)


api = APICore(login_url, "Пользователь 1", "111")
api.get_cashrequisition_document(390)

def test_is_document_open():
    assert api.get_cashrequisition_document(390) != None
