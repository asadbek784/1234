from aiogram import Router, html
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

class Roxat(StatesGroup):
    phone = State()
    address = State()

r = Router()

@r.message(Command("start"))
async def command_start_handler(message: Message, state: FSMContext):
    await state.clear()

    keyword = [
        [KeyboardButton(text="Telefon yuborish", request_contact=True)]
    ]

    menu = ReplyKeyboardMarkup(
        keyboard=keyword,
        resize_keyboard=True
    )

    await message.answer(
        f"Salom, {html.bold(message.from_user.full_name)}!",
        reply_markup=menu
    )

    await state.set_state(Roxat.phone)


@r.message(StateFilter(Roxat.phone))
async def command_phone(message: Message, state: FSMContext):
    if message.contact:
        phone = message.contact.phone_number
        await message.answer(f"Telefon qabul qilindi: {phone}")
        await state.clear()
    else:
        await message.answer("Iltimos, tugma orqali telefon yuboring.")


def user(dp):
    dp.include_router(r)
