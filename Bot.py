import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = os.getenv("8608795268:AAGw_ODCYK7-2rQEL6koyMppNUYuuk26ybs")  # Токен из секретов GitHub
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(msg: types.Message):
    await msg.answer("Я AuraXers, ебаный бот! Че надо?")

@dp.message()
async def reply_all(msg: types.Message):
    replies = ["Да пошёл ты!", "Окей, лох.", "Конечно, пидор."]
    await msg.answer(replies[__import__('random').randint(0,2)])

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
