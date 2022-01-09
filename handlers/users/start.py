from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline import main_keyboard
from loader import dp
from states import CryptoPrice


@dp.message_handler(CommandStart, state="*")
async def bot_start(message: types.Message, state=FSMContext):
    await state.finish()
    await message.answer(f"Приветсвую, {message.from_user.full_name}!\nВ данном боте ты можешь посмотреть нынешний курс "
                         f"самых популярных криптовалют в данный момент.\n"
                         f"Также есть у нас есть информация о прошедших днях", reply_markup=main_keyboard)
    await CryptoPrice.InputName.set()
