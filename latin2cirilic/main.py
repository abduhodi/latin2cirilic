from transliterate import to_cyrillic, to_latin
import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '*'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Menga matn yuboring")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Lotin yozuvida matn yuborsangiz kiril yozuviga o`tkazib beraman\
                        \nKiril yozuvida matn yuborsangiz lotin yozuviga o`tkazib beraman")


@dp.message_handler()
async def changer(message: types.Message):
    msg = message.text
    if msg.isascii():
        msg = to_cyrillic(msg)
    else:
        msg = to_latin(msg)
    await message.reply(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
