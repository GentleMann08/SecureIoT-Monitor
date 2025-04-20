from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.menu import Menu
from database.db import add_user

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: Message, bot: Bot, state: FSMContext):
    chat = message.chat.id

    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    add_user(first_name, last_name, username)

    keyboard = await Menu.start()
    last_messafe = await bot.send_message(
        chat_id=chat, 
        text="Добро пожаловать в IoT Security Monitor!",
        reply_markup=keyboard
        )
    
    await state.update_data(last_message_id=last_messafe.message_id)