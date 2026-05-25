from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🎵 Популярное"),
                KeyboardButton(text="🎲 Случайный"),
                KeyboardButton(text="ℹ️ О себе"),
            ]
        ],
        resize_keyboard=True,
    )
