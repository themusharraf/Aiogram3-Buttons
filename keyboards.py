from aiogram import types

button = [
    [types.KeyboardButton(text="location", request_location=True)],
    [types.KeyboardButton(text="contact", request_contact=True)],
]
keyboard = types.ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)
