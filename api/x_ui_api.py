import json
from typing import Any, NoReturn, Union
from urllib.parse import urljoin

import requests
from decouple import config

from app.utlis import try_json_load


class XUiApi:
    domain = config("DOMAIN_VPN")
    scemas = config("SCHEMA_VPN")
    port = config("PORT_VPN")
    base_url = f"{scemas}://{domain}:{port}"
    secret_path = config("SECRET_PATH_VPN")
    username = config("USERNAME_VPN")
    password = config("PASSWORD_VPN")
    main_inbound_id = config("MAIN_INBOUND_ID")

    def __init__(self):
        self.session = requests.Session()

    def request(self, url: str, method: str = "GET", **kwargs) -> Union[Any, NoReturn]:
        max_attempts, attempts = 3, 0
        while attempts < max_attempts:
            try:
                response = self.session.request(method, url, **kwargs)
                response.raise_for_status()
                result = response.json()
            except Exception:
                attempts += 1
                self.login()
            else:
                if not result["success"]:
                    raise Exception("Request failed")
                return result

    def login(self) -> Union[None, NoReturn]:
        url = urljoin(self.base_url, f"{self.secret_path}/login")
        payload = {
            "username": self.username,
            "password": self.password,
        }
        self.request(url, "POST", json=payload)

    def get_inboud(self) -> Union[dict, NoReturn]:
        url = urljoin(
            self.base_url,
            f"{self.secret_path}/panel/api/inbounds/get/{self.main_inbound_id}",
        )
        headers = {"Accept": "application/json"}
        result = self.request(url, headers=headers)
        return {k: try_json_load(v) for k, v in result["obj"].items()}

    def add_client_to_inbound(
        self, tg_id: Union[int, str], email: str
    ) -> Union[dict, NoReturn]:
        url = urljoin(self.base_url, f"{self.secret_path}/panel/api/inbounds/addClient")
        headers = {"Accept": "application/json"}
        payload = {
            "id": self.main_inbound_id,
            "settings": json.dumps(
                {
                    "clients": [
                        {
                            "id": str(tg_id),
                            "flow": "xtls-rprx-vision",
                            "email": email,
                            "limitIp": 0,
                            "totalGB": 0,
                            "expiryTime": 0,
                            "enable": True,
                            "tgId": str(tg_id),
                            "subId": "",
                            "reset": 0,
                        }
                    ]
                }
            ),
        }
        return self.request(url, "POST", headers=headers, data=payload)

    def del_client(self, client_id: str) -> Union[dict, NoReturn]:
        url = urljoin(
            self.base_url,
            f"{self.secret_path}/panel/api/inbounds/{self.main_inbound_id}/delClient/{client_id}",
        )
        payload = {}
        headers = {"Accept": "application/json"}
        result = self.request(url, "POST", headers=headers, data=payload)
        return result


X_UI_API = XUiApi()


if __name__ == "__main__":
    X_UI_API.login()
    X_UI_API.del_client()
