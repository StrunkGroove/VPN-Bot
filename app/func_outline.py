from os import getenv
from urllib.parse import urljoin

import aiohttp
from aiohttp import TCPConnector


class OutlineServerErrorException(Exception):
    pass


class OutlineManager:
    def __init__(self) -> None:
        self.api_url = getenv("API_URL_VPN")
        self.secret_string = getenv("SECRET_VPN_STRING")

    async def get_keys(self, timeout: int = None):
        url = urljoin(self.api_url, f"/{self.secret_string}/access-keys/")
        async with aiohttp.ClientSession(connector=TCPConnector(ssl=False)) as session:
            async with session.get(url, timeout=timeout) as response:
                if response.status == 200:
                    data = await response.json()
                    if "accessKeys" in data:
                        return data