
from aiogram import Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from states.anketa import Anketa
from keyboards.anketa import cancel_kb, cancel_back_kb, cancel_back_gender_kb #Про это спросить было import keyboards.anketa as kb_anketa

router = Router()

@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    await state.set_state(Anketa.name)
    await msg.answer('Введите Ваше имя', reply_markup=cancel_kb)

@router.callback_query(F.data == 'cancel_anketa')
async def next_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer('регистрация отменена')


@router.message(Anketa.name)
async def set_name_by_anketa_hander(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    await msg.answer("Введите ваш возраст", reply_markup=cancel_back_kb)


@router.callback_query(F.data == 'set_name_anketa')
async def set_name_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    await anketa_handler(callback_query.message, state)


@router.message(Anketa.age)
async def set_name_by_anketa_hander(msg: Message, state: FSMContext):
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('Вы неверно ввели возраст!')
        await msg.answer("Введите ваш возраст", reply_markup=cancel_back_kb)
        return
    
    await state.set_state(Anketa.gender)
    await msg.answer('Введите Ваш пол', reply_markup=cancel_back_gender_kb)


@router.callback_query(F.data.startswitch('gender_') and Anketa.gender)
async def anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    gender = {'gender_male':'Мужской', 'gender_female':'Женский'}[callback_query.data]
    await state.update_data(gender=gender)
    await callback_query.message.answer(str(await state.get_data()))
    await state.clear()

@router.message(Anketa.gender)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    await msg.answer('Нужно выбрать кнопкой')

@router.callback_query(F.data == 'set_age_anketa')
async def set_age_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Anketa.age)
    await callback_query.message.answer('Введите Ваш возраст', reply_markup=cancel_back_kb)

@router.callback_query(F.data == 'back_anketa')
async def set_age_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state == Anketa.gender:
        await state.set_state(Anketa.age)
        await callback_query.message.answer('Введите ваш возраст', reply_markup=cancel_back_kb)

    elif current_state == Anketa.age:
        await state.set_state(Anketa.name)
        await callback_query.message.answer('Введите вашe имя', reply_markup=cancel_kb)


@router.message(Anketa.gender)
async def set_age_by_anketa_hander(msg: Message, state: FSMContext):
    await state.update_data(gender=msg.text)
    await msg.answer(str(await state.get_data()))
    await state.clear()

