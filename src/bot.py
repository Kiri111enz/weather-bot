from aiogram import Bot, Dispatcher, Router
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
import aiogram.utils.markdown as md
from aiogram.types import Message

_router = Router()


class States(StatesGroup):
    location = State()
    period = State()


@_router.message(CommandStart())
async def _start_handler(message: Message, state: FSMContext) -> None:
    await state.set_data({'period': 1})
    await state.set_state(States.location)
    await message.answer(f'Привет, {md.bold(message.from_user.full_name)}\\! Твоя локация?')


@_router.message(Command('location'))
async def _location_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(States.location)
    await message.answer('Твоя локация?')


@_router.message(States.location)
async def _location_state_handler(message: Message, state: FSMContext) -> None:
    await state.update_data(location=message.text)
    await state.set_state()
    await message.answer('Готово\\! Можешь узнавать погоду\\.')


@_router.message(Command('period'))
async def _period_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(States.period)
    await message.answer('На какое количество дней ты хочешь узнавать погоду?')


@_router.message(States.period)
async def _period_state_handler(message: Message, state: FSMContext) -> None:
    try:
        period = int(message.text)
        if period < 1 or period > 30:
            await message.answer('Введи число от 1 до 30\\.')
            return
    except ValueError:
        await message.answer('Попробуй ввести число заново\\.')
        return

    await state.update_data(period=period)
    await state.set_state()
    await message.answer('Период успешно установлен\\.')


@_router.message(Command('weather'))
async def _weather_handler(message: Message, state: FSMContext) -> None:
    data = await state.get_data()
    print(data)
    await message.answer(f'Сегодня в городе {data["location"]} 0 градусов\\.')


@_router.message(Command('clothes'))
async def _clothes_handler(message: Message) -> None:
    await message.answer('Сегодня лучше надеть шубу\\.')


async def start(bot_token: str) -> None:
    bot = Bot(token=bot_token, parse_mode='MarkdownV2')
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(_router)

    await dp.start_polling(bot)
