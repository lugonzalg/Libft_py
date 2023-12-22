import asyncio

async def main() -> int:

    while True:

        print("Hey!")
        await asyncio.sleep(1)

    return 0

if __name__ == "__main__":
    asyncio.run(main())
