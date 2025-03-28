import asyncio
import time
import aiohttp

async def get_data(id : int, endpoint: str):

    url = f"http://127.0.0.1:8000/{endpoint}/{id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            ...

async def main():
    print(f"Запуск запроса в {time.time():.2f}")
    startTime = time.time()
    await asyncio.gather(
        *[get_data(id, "async") for id in range(500)]
    )
    endTime = time.time() - startTime
    print(f"Выполнил запрос за {endTime:.2f}")

if __name__ == "__main__":
    asyncio.run(main())