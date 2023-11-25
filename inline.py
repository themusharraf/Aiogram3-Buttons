from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

builder = InlineKeyboardBuilder()
builder.row(types.InlineKeyboardButton(
    text="GitHub", url="https://github.com/themusharraf")
)
builder.row(types.InlineKeyboardButton(
    text="Aiogram Documentation",
    url="https://docs.aiogram.dev/en/latest/")
)

builder_shop = InlineKeyboardBuilder()
builder_shop.row(types.InlineKeyboardButton(
    text="Python", url="https://www.python.org/")
)

builder_random = InlineKeyboardBuilder()
builder_random.add(types.InlineKeyboardButton(
    text="Knopkani bosing",
    callback_data="random_son")
)
