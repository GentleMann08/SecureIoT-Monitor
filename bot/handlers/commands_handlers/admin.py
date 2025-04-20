from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
from settings import Settings
from database.db import get_users
import csv
import os

admin_router = Router()

@admin_router.message(Command("users"))
async def example(message: Message, bot: Bot, state: FSMContext):
    chat = message.chat.id

    is_admin = message.from_user.username in Settings.admins

    if is_admin:
        data = []
        file_path = 'database/users.csv'
        directory = os.path.dirname(file_path)

        if not os.path.exists(directory):
            os.makedirs(directory)

        for user in get_users():
            first_name, last_name, username, created_at = user
            data.append([first_name, last_name, username, created_at])

        with open(file_path, 'w', newline='') as users:
            writer = csv.writer(users)
            writer.writerows(data)

        document = FSInputFile(file_path)
        last_message = await bot.send_document(
            chat_id=chat,
            document=document
        )

    else:
        last_message = await bot.send_message(
            chat_id=chat,
            text="Нет прав для выполнения команды!"
        )

    await state.update_data(last_message_id=last_message.message_id)
