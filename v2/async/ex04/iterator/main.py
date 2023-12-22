import asyncio
from dataclasses import dataclass

@dataclass
class AsyncTimer:

    count: int = 5

    def __aiter__(self):
        self.current = 0
        return self

    async def __anext__(self):
        if self.current < self.count:
            self.current += 1
            await asyncio.sleep(1)
            return self.current
        else:
            raise StopAsyncIteration

async def main() -> int:
    async for number in AsyncTimer(5):
        print(number)

asyncio.run(main())
