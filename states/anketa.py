"""состояния"""
from aiogram.fsm.state import State, StatesGroup

class Anketa(StatesGroup):
    '''класс с состояиями'''
    name = State()
    age = State()
    gender = State()
