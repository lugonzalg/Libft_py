async def aio_get(
        client: aiohttp.ClientSession, 
        url: str, 
        headers: dict, 
        params: dict = None
        ) -> object:
    
    try:
        aio_res = await client.get(url, headers=headers, params=params)
        return aio_res
    except aiohttp.HTTPClientError as err:
        logger.logger.error(f"Error: client side error {err}")
    except aiohttp.HTTPServerError as err:
        logger.logger.error(f"Error: server side error {err}")
    except asyncio.TimeoutError as err:
        logger.logger.error(f"Error: timeout {err}")
