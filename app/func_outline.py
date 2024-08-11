from os import getenv
from typing import Union
from urllib.parse import urljoin
from os import getenv

import aiohttp
from aiohttp import TCPConnector


def bytes_to_gb(integer: int) -> float:
    return round(integer / (1024 ** 3), 3)


class TestLimit:
    name = "5 Gb"
    value = 1_073_741_824 * 5


class OutlineServerException(Exception):
    pass


class OutlineManager:
    not_foud = "Not found"

    def __init__(self) -> None:
        self.api_url = getenv("API_URL_VPN")
        self.secret_string = getenv("SECRET_VPN_STRING")

    async def get_data(
        self, url: str, method = "get", **kwargs
    ) -> Union[dict, str]:
        async with aiohttp.ClientSession(
            connector=TCPConnector(ssl=False)
        ) as session:
            async with session.request(
                method, url, **kwargs
            ) as response:
                if response.status == 404:
                    return self.not_foud
                if response.status >= 200 and response.status < 300:
                    return await response.json()
                raise OutlineServerException()

    async def get_keys(self, timeout: int = None) -> Union[dict, str]:
        url = urljoin(self.api_url, f"/{self.secret_string}/access-keys/")
        result = await self.get_data(url, timeout=timeout)
        return result

    async def get_key(self, key_id: str, timeout: int = None) -> Union[dict, str]:
        url = urljoin(self.api_url, f"/{self.secret_string}/access-keys/{key_id}")
        result = await self.get_data(url, timeout=timeout)
        return result

    async def create_key(
        self, key_id: int, timeout: int = None, **kwargs
    ):
        """
        - kwargs (dict):
            - name (str)
            - method (str)
            - password (str)
            - port (int)
            - limit (dict): Ожидает словарь вида {"bytes": <bytes>}.
        """
        payload = {**kwargs}
        url = urljoin(self.api_url, f"/{self.secret_string}/access-keys/{key_id}",)
        result = await self.get_data(url, "put", timeout=timeout, json=payload)
        return result

    async def get_transferred_data(self, timeout: int = None) -> dict:
        url = urljoin(self.api_url, f"/{self.secret_string}/metrics/transfer",)
        result = await self.get_data(url, timeout=timeout)
        return result

    async def get_transferred_data_per_user(
        self, key_id: int, timeout: int = None
    ) -> float:
        key_id = str(key_id)
        result = await self.get_transferred_data(timeout)
        if transferred_data := result["bytesTransferredByUserId"].get(key_id):
            return bytes_to_gb(transferred_data)
        return 0