import asyncio
import time
import threading

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/sync/{id}")
def sync_get(id : int):
    print(f"Потоков sync {threading.active_count()}")
    print(f"Запуск sync функции {id} в {time.time():.2f}")
    time.sleep(3)
    print(f"Закончил sync функции {id} в {time.time():.2f}")

@app.get("/async/{id}")
async def async_get(id : int):
    print(f"Потоков async {threading.active_count()}")
    print(f"Запуск async функции {id} в {time.time():.2f}")
    await asyncio.sleep(3)
    print(f"Закончил async функции {id} в {time.time():.2f}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)