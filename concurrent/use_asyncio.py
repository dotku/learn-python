import asyncio

async def worker():
    print(f"Worker is starting.")
    await asyncio.sleep(2)
    print(f"Worker is done.")

async def main():
    await asyncio.gather(*(worker() for _ in range(5)))

asyncio.run(main())