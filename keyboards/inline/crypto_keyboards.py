from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="BTC", callback_data="BTC"),
    ],
    [
        InlineKeyboardButton(text="ETH", callback_data="ETH"),
    ],
    [
        InlineKeyboardButton(text="SOL", callback_data="SOL"),
    ],
    [
        InlineKeyboardButton(text="BNB", callback_data="BNB"),
    ],
    [
        InlineKeyboardButton(text="ADA", callback_data="ADA"),
    ],
    [
        InlineKeyboardButton(text="XRP", callback_data="XRP"),
    ],
    [
        InlineKeyboardButton(text="DOT", callback_data="DOT"),
    ],
    [
        InlineKeyboardButton(text="MATIC", callback_data="MATIC"),
    ]
])


check_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="За промежуток", callback_data="interval"),
    ],
    [
        InlineKeyboardButton(text="Нынешний курс", callback_data="now"),
    ]
])

back_keyboard = InlineKeyboardMarkup(inline_keyboard=[

    [
        InlineKeyboardButton(text="Назад", callback_data="back"),
    ]
])


