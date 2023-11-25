from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram import types

button = [
    [types.KeyboardButton(text="location", request_location=True)],
    [types.KeyboardButton(text="contact", request_contact=True)],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)

builder_one = ReplyKeyboardBuilder()
for i in range(1, 20):
    builder_one.add(types.KeyboardButton(text=str(i)))
builder_one.adjust(4)
