from aiogram import Router, types
from aiogram.filters import Command
from keyboards.menu import main_menu
from utils.messages import START_TEXT, ABOUT_TEXT, HELP_TEXT, UNKNOWN_COMMAND

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(START_TEXT, reply_markup=main_menu())

@router.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer(ABOUT_TEXT)

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(HELP_TEXT)

@router.message(lambda msg: msg.text == "ℹ️ О себе")
async def btn_about(message: types.Message):
    await message.answer(ABOUT_TEXT)
