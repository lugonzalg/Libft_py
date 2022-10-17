import requests
import asyncio

from dataclasses import dataclass

@dataclass
class Proxy:

    def simple_get(self, url: str, verify: bool = True) -> dict:
        #self.logger.info(url)
        res = requests.get(url, verify=verify)
        if res.status_code != 200:
            self.logger.error(f"URL -> {url}")
        return res

    async def async_get(self, url: str, verify: bool = True) -> dict:
        res = await asyncio.to_thread(self.simple_get, url, verify)
        return res.json()

