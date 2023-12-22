import asyncio
import httpx

async def timer(client: httpx.AsyncClient, url: str, id: int):
    while True:

        res = await client.get(url)
        print(res.status_code)
        await asyncio.sleep(1)

async def main() -> int:
    url = "https://petstore.swagger.io/v2/store/inventory"
    async with httpx.AsyncClient() as client:
        tasks = [ timer(client, url, i) for i in range(10)]
        await asyncio.gather(*tasks)

    return 0

if __name__ == "__main__":
    asyncio.run(main())
