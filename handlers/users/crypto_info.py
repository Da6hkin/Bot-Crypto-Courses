import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import API_KEY
from keyboards.inline import back_keyboard, check_keyboard, main_keyboard
from loader import dp, db
from states import CryptoPrice
from data import config
from utils.db_api import postgre_sql


@dp.callback_query_handler(state=CryptoPrice.InputName)
async def save_name(call: types.CallbackQuery, state=FSMContext):
    await call.answer()
    if call.data in config.CALLBACK_DATA:
        await state.update_data({"name": call.data})
        await call.message.answer("Выберите опцию:", reply_markup=check_keyboard)
        await CryptoPrice.InputOption.set()


@dp.callback_query_handler(state=CryptoPrice.InputOption)
async def save_name(call: types.CallbackQuery, state=FSMContext):
    await call.answer()
    data = await state.get_data()
    name = data.get("name")
    if call.data == "now":
        price = await get_price(name)
        await call.message.answer(f"Цена {name} сейчас {price} долларов!", reply_markup=back_keyboard)
        await CryptoPrice.DataOption.set()
    elif call.data == "interval":
        dates = await db.select_dates_by_name(name)
        await call.message.answer(f"Доступные даты:{dates}")
        await  CryptoPrice.DataOption.set()


@dp.callback_query_handler(state=CryptoPrice.DataOption)
async def save_name(call: types.CallbackQuery, state=FSMContext):
    await call.answer()

    if call.data == "back":
        data = await state.finish()
        await call.message.answer(f"Посмотрите курсы доступных Криптовалют!", reply_markup=main_keyboard)
        await CryptoPrice.InputName.set()

    else:
        date = call.data
        data = await state.get_data()
        name = data.get("name")
        price = await db.select_price_by_coin_name(name, date)
        await call.message.answer(f"Цена за {date} равна {price}", reply_markup=main_keyboard)
        await CryptoPrice.InputName.set()


headers = {'X-CoinAPI-Key': API_KEY}


async def get_price(name):
    url = f'https://rest.coinapi.io/v1/exchangerate/{name}/USD'
    async with aiohttp.ClientSession() as session:
        session.headers.update(headers)
        async with session.get(url) as resp:
            json_response = await resp.json()
            print(json_response["rate"])
            return json_response["rate"]
