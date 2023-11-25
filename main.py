import asyncio
import logging

from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import token
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("buttons"))
async def buttons(message: types.Message):
    ...


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
