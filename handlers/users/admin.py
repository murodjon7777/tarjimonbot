import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)
    # await bot.send_message(
    #     chat_id=ADMINS[0],
    #     text = f"Active {active} Unactive: {unactive}"
    # )

@dp.message_handler(text="/reklama", user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    active=0
    unactive=0
    for user in users:
        try:
            active+=1
            user_id = user[0]
            await bot.send_message(chat_id=user_id, text="Taklif fikrlar uchun @uzbek_7700")
            await asyncio.sleep(0.05)
        except:
            unactive+=1
    await bot.send_message(
        chat_id=ADMINS[0],
        text = f"Active {active} Unactive: {unactive}"
    )
@dp.message_handler(text="/active",user_id=ADMINS)
async def send_ad_to_all(message: types.Message):
    users = db.select_all_users()
    active=0
    unactive=0
    for user in users:
        try:
            active+=1
            user_id = user[0]
            # await bot.send_message(chat_id=user_id, text="Taklif fikrlar uchun @uzbek_7700")
            await asyncio.sleep(0.05)
        except:
            unactive+=1
    await bot.send_message(
        chat_id=ADMINS[0],
        text = f"Active {active} Unactive: {unactive}"
    )
    

@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")