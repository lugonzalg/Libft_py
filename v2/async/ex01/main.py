import asyncio

async def timer(id: int):
    while True:

        print(f"My id is: {id}")
        await asyncio.sleep(1)

async def main() -> int:
    tasks = [ timer(i) for i in range(10)]
    await asyncio.gather(*tasks)

    return 0

if __name__ == "__main__":
    asyncio.run(main())
