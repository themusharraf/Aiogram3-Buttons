import asyncio
import logging

from aiogram.utils.keyboard import ReplyKeyboardBuilder

from config import token
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from keyboards import keyboard
from inline import builder

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
    await message.answer("inline button!", reply_markup=builder.as_markup())


@dp.message(Command("rep"))
async def reply_builder(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 20):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(4)
    await message.answer(
        "date choice:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
