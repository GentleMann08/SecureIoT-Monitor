from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.menu import Menu

system_router = Router()

@system_router.callback_query(F.data == 'to_start')
async def to_start(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    last_message_id = data.get("last_message_id")

    keyboard = await Menu.start()
    new_message = await callback_query.message.edit_text(
        text="👋 Добро пожаловать в IoT Security Monitor!",
        reply_markup=keyboard
    )

    await state.update_data(last_message_id=new_message.message_id)

@system_router.callback_query(F.data == 'example_reaction')
async def example_reaction(callback_query: CallbackQuery, state: FSMContext):

    new_message = await callback_query.answer(
        text = "❌ Возможность реагирования в примерах отсутствует",
    )