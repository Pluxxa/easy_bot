import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from config import TOKEN
from keyboards import main_menu_keyboard, links_keyboard, dynamic_keyboard, options_keyboard

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    user = message.from_user
    await message.answer(f'Привет, {user.first_name}! Выберите опцию:', reply_markup=main_menu_keyboard())

@dp.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.answer('Список команд:\n/start - начать\n/help - помощь\n/links - ссылки\n/dynamic - динамическая клавиатура')

@dp.message(Command(commands=['links']))
async def links(message: Message):
    await message.answer("Выберите категорию:", reply_markup=links_keyboard())

@dp.message(Command(commands=['dynamic']))
async def dynamic(message: Message):
    await message.answer("Выберите опцию:", reply_markup=dynamic_keyboard())

@dp.callback_query(F.data == "show_more")
async def show_more(callback_query: CallbackQuery):
    await bot.edit_message_reply_markup(chat_id=str(callback_query.message.chat.id),
                                        message_id=callback_query.message.message_id,
                                        reply_markup=options_keyboard())

@dp.callback_query(F.data == "option1")
async def option1(callback_query: CallbackQuery):
    await bot.send_message(chat_id=str(callback_query.message.chat.id), text="Вы выбрали Опцию 1")

@dp.callback_query(F.data == "option2")
async def option2(callback_query: CallbackQuery):
    await bot.send_message(chat_id=str(callback_query.message.chat.id), text="Вы выбрали Опцию 2")

@dp.message(F.text == "Привет")
async def hello(message: Message):
    user = message.from_user
    await message.answer(f"Привет, {user.first_name}!")

@dp.message(F.text == "Пока")
async def goodbye(message: Message):
    user = message.from_user
    await message.answer(f"До свидания, {user.first_name}!")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
