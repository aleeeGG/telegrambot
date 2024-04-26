from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Вперед', callback_data='next')]])

next_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад', callback_data='back')]])