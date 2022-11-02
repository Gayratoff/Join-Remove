from aiogram import types
from aiogram.types import ContentTypes
from keyboards.inline.inline import guruh
from filters.guruh import Guruh
from loader import dp, bot

@dp.message_handler(Guruh(), commands='start')
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    await message.reply( text=f"👋🏻 Assalomu alaykum {message.from_user.full_name}!\n\n@MistrUz sizning guruhlaringizni <b>oson</b> va <b>xavfsiz boshqarish</b> uchun eng <b>takomillashgan</b> botdir!\n\n👉🏻 <b>Botni guruhingizga qo'shing</b> va ishga tushishi uchun <b>Admin</b> huquqini bering!\n\n❓ <b>QANDAY BUYRUQLAR BOR?\n\nBarcha buyruqlarni</b> ko'rish va ular qanday ishlashini bilish uchun /help buyrug'ini yuboring!\n "
                                                 f"<a href='{'https://t.me/IT_Subject'}'>📃 Official Page</a>\n",disable_web_page_preview=True,reply_markup=guruh)


@dp.message_handler(Guruh(),content_types=ContentTypes.NEW_CHAT_MEMBERS)
async def bot_echo(message: types.Message):
    nick = message.new_chat_members[0].full_name
    chat_id =  message.chat.id
    mes_id = message.message_id
    await bot.delete_message(chat_id=chat_id,message_id=mes_id)

@dp.message_handler(Guruh(),content_types=ContentTypes.LEFT_CHAT_MEMBER)
async def bot_echo(message: types.Message):
    nick = message.left_chat_member.full_name
    chat_id =  message.chat.id
    mes_id = message.message_id
    await bot.delete_message(chat_id=chat_id,message_id=mes_id)
