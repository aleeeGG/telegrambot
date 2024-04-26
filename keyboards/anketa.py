from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

cancel_kb = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text = 'Отмена', callback_data='cancel_anketa')]])


cancel_back_kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Назад', callback_data='back_anketa'),
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]])

cancel_back_gender_kb = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Назад', callback_data='back_anketa'),
    InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')],
    [InlineKeyboardButton(text='мужской', callback_data='gender_male'),
    InlineKeyboardButton(text='женский', callback_data='gender_female')]])