from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Привет")],
            [KeyboardButton(text="Пока")]
        ],
        resize_keyboard=True
    )
    return keyboard

def links_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Новости", url="https://news.yandex.ru")],
            [InlineKeyboardButton(text="Музыка", url="https://music.yandex.ru")],
            [InlineKeyboardButton(text="Видео", url="https://youtube.com")]
        ]
    )
    return keyboard

def dynamic_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Показать больше", callback_data="show_more")]
        ]
    )
    return keyboard

def options_keyboard():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Опция 1", callback_data="option1")],
            [InlineKeyboardButton(text="Опция 2", callback_data="option2")]
        ]
    )
    return keyboard
