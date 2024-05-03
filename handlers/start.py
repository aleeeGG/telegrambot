from aiogram import Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
from keyboards.start import next_kb, back_kb



router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    from main import bot
    await bot.set_my_commands([
        BotCommand(command='start', description='Запуск бота'),
        BotCommand(command='anketa', description='Справка'),
        BotCommand(command='delete', description='Отчислиться')
    ])

    await msg.answer(text="Страница 1", reply_markup=next_kb)

@router.callback_query(F.data == 'next')
async def next_handler(callback_query: CallbackQuery):
    next_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад', callback_data='back')]])
    await callback_query.message.edit_text('Страница 2', reply_markup=back_kb)

@router.callback_query(F.data == 'back')
async def back_handler(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await callback_query.message.answer(
        text="Страница 1",
        reply_markup=back_kb)
