import asyncio

async def async_timer(count: int) -> int:

    for i in range(1, count + 1):
        await asyncio.sleep(1)
        yield 1

async def main() -> int:
    async for number in async_timer(5):
        print(number)

asyncio.run(main())
