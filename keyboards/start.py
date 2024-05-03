'''обработчик кнопок'''
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

back_kb = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Назад', callback_data='back')]])
'''кнопка назад'''
next_btn = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Вперед', callback_data='next')]])
