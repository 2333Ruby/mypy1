import asyncio
import time


async def play():
    print("enter play")
    for _ in range(5):
        sleep_coro = asyncio.sleep(1)
        await asyncio.create_task(sleep_coro)
        # time.sleep(1)  # 线程被占用，线程阻塞
        # 所有可能让线程等待的IO调用都应该使用其异步版本，否则会降低程序的吞吐量
        for _ in range(1000):
            pass


async def main():
    print("enter main")
    start = time.time()
    task = []
    for _ in range(10):
        play_coro = play()
        task.append(asyncio.create_task(play_coro))
    for t in task:
        await t
    print(f"total time: {time.time() - start} seconds")


main_coro = main()
asyncio.run(main_coro)
