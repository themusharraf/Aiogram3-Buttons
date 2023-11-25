import asyncio
import logging
from config import token
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from keyboards import keyboard

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("buttons"))
async def buttons(message: types.Message):
    await message.answer("location or contact", reply_markup=keyboard)


@dp.message(Command("in_url"))
async def button(message: types.Message):
    await message.answer("inline button!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
