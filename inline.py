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

builder_random = InlineKeyboardBuilder()
builder_random.add(types.InlineKeyboardButton(
    text="Knopkani bosing",
    callback_data="random_son")
)
