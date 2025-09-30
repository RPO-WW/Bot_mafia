import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Токен бота (замените на свой!)
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Привет!")

# Обработчик всех текстовых сообщений (эхо)
@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

# Основная функция запуска
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
