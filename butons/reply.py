from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


bosh_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Start⬅️'),
            KeyboardButton('Help📝')
        ]
    ],
    resize_keyboard=True
)
start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Start⬅️'),
            KeyboardButton('Help📝')
        ]
    ],
    resize_keyboard=True
)
menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Programming📋'),
            KeyboardButton('Books📚')
        ]
    ],
    resize_keyboard=True
)

quiz_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Testni boshlash👨🏽‍💻')
        ],
        [
            KeyboardButton('Orqaga⬅️'),
            KeyboardButton('Bosh Menu🏠')
        ]
    ],
    resize_keyboard=True
)


tug_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Testni yakunlash🏁')
        ],
        [
            KeyboardButton('Qayta boshlash🔄️')
        ],
        [
            KeyboardButton('Orqaga⬅️'),
            KeyboardButton('Bosh Menu🏠')
        ]
    ],
    resize_keyboard=True
)