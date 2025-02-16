from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.menu import Menu

menu_router = Router()

text = '''
Выберите опцию
'''

@menu_router.callback_query(F.data == 'menu')
async def handle_bleu_check(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_message_id = data.get("last_message_id")

    if last_message_id:
        await callback_query.message.chat.delete_message(message_id=last_message_id)

    keyboard = await Menu.menu()
    last_messafe = await callback_query.message.answer(
        text=text,
        reply_markup=keyboard
        )
    
    await state.update_data(last_message_id=last_messafe.message_id)