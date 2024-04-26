from aiogram import Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from states.anketa import Anketa
from keyboards.start import back_kb, next_kb #import keyboards.anketa as kb_anketa

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='anketa', description='Справка'),
        BotCommand(command='delete', description='Отчислиться')
    ])

    inline_markap = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Вперед', callback_data='next')]])
    await msg.answer(text="Страница 1", reply_markup=inline_markap)

@router.callback_query(F.data=='next')
async def next_handler(callback_query: CallbackQuery):
    next_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад', callback_data='back')]])
    await callback_query.message.edit_text('Страница 2', reply_markup=next_kb)

@router.callback_query(F.data == 'back')
async def back_handler(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer(
        text="Страница 1",
        reply_markup=back_kb)
