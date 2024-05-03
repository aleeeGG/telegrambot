from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

next_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад', callback_data='back')]])

back_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Вперед', callback_data='next')]])