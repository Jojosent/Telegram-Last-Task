from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Coose one", reply_markup=menu)

@dp.message_handler(Text(equals=["12","34","56"]))
async def get_food(message:Message):
    await message.answer(f"Coosen {message.text}. Thanks",
                           reply_markup=ReplyKeyboardRemove())