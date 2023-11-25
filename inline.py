from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

builder = InlineKeyboardBuilder()
builder.row(types.InlineKeyboardButton(
    text="GitHub", url="https://github.com/themusharraf")
)
builder.row(types.InlineKeyboardButton(
    text="Aiogram Documentation",
    url="tg://@all_nc")
)
