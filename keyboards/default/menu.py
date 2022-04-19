from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="12")
        ],
        [
            KeyboardButton(text="34"),
            KeyboardButton(text="56")
        ],
    ],
    resize_keyboard=True
)