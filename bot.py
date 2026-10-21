import os
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🔐 MELSTROY VPN\n\n"
        "Добро пожаловать!\n"
        "Выбери действие:\n\n"
        "💳 Тарифы — скоро\n"
        "👤 Мой аккаунт — скоро\n"
        "🆘 Поддержка — скоро"
    )

async def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN в настройках Render")
    bot = Bot(token=TOKEN)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
