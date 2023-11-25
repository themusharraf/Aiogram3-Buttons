import asyncio
import logging
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from keyboards import keyboard, builder_one
from config import token
from random import randint
from inline import builder, builder_random

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
    await message.answer(
        "date choice:",
        reply_markup=builder_one.as_markup(resize_keyboard=True),
    )


@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    await message.answer(
        "Knopkani bosing, 1 dan 10 gacha bo'lgan botni o'rnating",
        reply_markup=builder_random.as_markup()
    )


@dp.callback_query(F.data == "random_son")
async def send_random_son(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
