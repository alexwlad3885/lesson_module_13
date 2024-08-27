# - * - coding: utf - 8 - * -
"""Домашнее задание по теме 'Асинхронность на практике'"""
import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    inverse_prop_power = 1 / power
    for ball_number in range(1, 6):
        await asyncio.sleep(inverse_prop_power)
        print(f'Силач {name} поднял {ball_number}')
        if ball_number == 5:
            print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Pasha', 3))
    task_2 = asyncio.create_task(start_strongman('Denis', 4))
    task_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())
