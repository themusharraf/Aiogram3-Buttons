import asyncio
import logging
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config import token
from random import randint
from keyboards import keyboard, builder_one, keyboard_shop
from inline import builder, builder_random, builder_shop, redmi_shop, apple_shop

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("buttons"))
async def buttons(message: types.Message):
    await message.answer("location or contact", reply_markup=keyboard)


@dp.message(Command("inl"))
async def button(message: types.Message):
    await message.answer_photo(photo="https://images.app.goo.gl/j9DisEm4jsxcMw7V7", caption="inline button!",
                               reply_markup=builder.as_markup())


@dp.message(Command("rep"))
async def reply_builder(message: types.Message):
    await message.answer(
        "date choice:",
        reply_markup=builder_one.as_markup(resize_keyboard=True),
    )

    @dp.message(F.text == "2")
    async def reply(message: types.Message):
        await message.answer(" 2- raqam")


@dp.message(Command("shop"))
async def shop(message: types.Message):
    await message.answer_photo(photo="https://images.app.goo.gl/j9DisEm4jsxcMw7V7", caption="choices list",
                               reply_markup=builder_shop.as_markup())


@dp.message(Command("shop_list"))
async def shop_list(message: types.Message):
    await message.answer(
        "shop choice:", reply_markup=keyboard_shop)

    @dp.message(F.text == "Apple")
    async def reply(message: types.Message):
        await message.answer_photo(photo="", caption="Apple mobile", reply_markup=apple_shop.as_markup())

    @dp.message(F.text == "Redmi")
    async def reply1(message: types.Message):
        await message.answer_photo(photo="", caption="Redmi mobile", reply_markup=redmi_shop.as_markup())


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
