from aiogram.dispatcher.filters.state import StatesGroup, State


class CryptoPrice(StatesGroup):
    InputName = State()
    InputOption = State()
    DataOption = State()
    PriceByDate = State()
