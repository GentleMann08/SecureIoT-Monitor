from aiogram import Bot, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.menu import Menu
from datetime import datetime

example_router = Router()

text = f"""
<b>❗ Остановлена попытка отправки данных во внешнюю среду со стороны устройства!</b>

Устройство: <b>192.168.1.50</b>
Тип активности: <b>Попытка подключения к неизвестному серверу</b>
Время обнаружения: <b>{datetime.now().strftime("%d.%m.%y")} {datetime.now().strftime("%H:%M")}</b>

Детали:
- <b>IP-адрес назначения:</b> 93.184.216.34
- <b>Тип данных:</b> Конфиденциальная информация
- <b>Статус:</b> Попытка блокирована
"""

@example_router.message(Command("example"))
async def start_handler(message: Message, bot: Bot, state: FSMContext):
    chat = message.chat.id

    keyboard = await Menu.example_reaction()
    last_messafe = await bot.send_message(
        chat_id=chat, 
        text=text,
        reply_markup=keyboard
        )
    
    await state.update_data(last_message_id=last_messafe.message_id)