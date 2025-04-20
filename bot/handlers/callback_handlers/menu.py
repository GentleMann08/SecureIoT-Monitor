from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.menu import Menu

menu_router = Router()

text = '''
Выберите опцию
'''

@menu_router.callback_query(F.data == 'menu')
async def menu(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_message_id = data.get("last_message_id")

    keyboard = await Menu.menu()
    last_messafe = await callback_query.message.edit_text(
        text=text,
        reply_markup=keyboard
        )
    
    await state.update_data(last_message_id=last_messafe.message_id)


@menu_router.callback_query(F.data == 'join')
async def join(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_message_id = data.get("last_message_id")

    keyboard = await Menu.to_start()
    last_messafe = await callback_query.message.edit_text(
        text= '❗ Запись на тестирование приостановлена',
        reply_markup=keyboard
        )
    
    await state.update_data(last_message_id=last_messafe.message_id)