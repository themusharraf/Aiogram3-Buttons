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

apple_shop = InlineKeyboardBuilder()
apple_shop.row(types.InlineKeyboardButton(
    text="Apple 14", url="https://www.apple.com/uz/iphone-14-pro/specs/")
)
redmi_shop = InlineKeyboardBuilder()
redmi_shop.row(types.InlineKeyboardButton(
    text="Redmi 12", url="https://mi-store.uz/shop/redmi-note-12-pro-plus-5g")
)

builder_random = InlineKeyboardBuilder()
builder_random.add(types.InlineKeyboardButton(
    text="Knopkani bosing",
    callback_data="random_son")
)
