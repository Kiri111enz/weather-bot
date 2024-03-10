from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import aiogram.utils.markdown as md
from env import config

_dp = Dispatcher()


@_dp.message(CommandStart())
async def _start_handler(message: Message) -> None:
    await message.answer(f'Привет, {md.bold(message.from_user.full_name)}\!', parse_mode='MarkdownV2')


@_dp.message()
async def _echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Неплохая попытка!')


async def start() -> None:
    bot = Bot(token=config.BOT_TOKEN)
    await _dp.start_polling(bot)
