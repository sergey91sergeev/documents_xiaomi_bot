from aiogram import Bot, Dispatcher, types
from aiogram import executor
import asyncio
from config import TOKEN
from datetime import datetime
from db_sqlite3 import insert_into_table_User
from db_sqlite3 import insert_into_table_Documents

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["📱 Смартфоны", "🏠 Умный дом"]
    keyboard.add(*buttons)
    await message.reply("Привет! Я бот, и я здесь для того, что бы ты нашёл то, что ищешь!", reply_markup=keyboard)

    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_surname = message.from_user.last_name
    username = message.from_user.username
    date_time = datetime.today()

    insert_into_table_User(user_id, user_name, user_surname, username, date_time)


@dp.message_handler(lambda message: message.text == "🚀 Главная")
async def start2_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["📱 Смартфоны", "🏠 Умный дом"]
    keyboard.add(*buttons)
    await message.reply("Выбери категорию", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📱 Смартфоны")
async def smartphone_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["📱 Xiaomi", "📱 Redmi", "📱 Poco", "🚀 Главная"]
    keyboard.add(*buttons)
    await message.reply("Выбери линейку смартфонов", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📱 Xiaomi")
async def xiaomi_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["📱 Xiaomi 14", "📱 Xiaomi 14T, 14T Pro", "🚀 Главная"]
    keyboard.add(*buttons)
    await message.reply("Выбери нужный смартфон", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📱 Redmi")
async def redmi_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["📱 Note 13", "📱 Note 13 Pro", "📱 Note 13 Pro+ 5G", "🚀 Главная"]
    keyboard.add(*buttons)
    await message.reply("Выбери нужный смартфон", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📱 Poco")
async def redmi_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["📱 Poco F5/F5 Pro", "📱 Poco F6/F6 Pro", "🚀 Главная"]
    keyboard.add(*buttons)
    await message.reply("Выбери нужный смартфон", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "🏠 Умный дом")
async def smartphone_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["🧹 Вертикальные пылесосы", "🤖 Роботы-пылесосы", "🚀 Главная"]
    keyboard.add(*buttons)
    await message.reply("Выбери нужный девайс", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "🧹 Вертикальные пылесосы")
async def vacuum_cleaner_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["🧹 G20", "🧹 G20 max", "🧹 Truclean W20 Wet Dry Vacuum", "🚀 Главная"]
    keyboard.add(*buttons)
    await message.reply("Выбери нужный девайс", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "🤖 Роботы-пылесосы")
async def robot_vacuum_cleaner_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ["🤖 X20+", "🤖 S20+", "🤖 S20", "🚀 Главная"]
    keyboard.add(*buttons)
    await message.reply("Выбери нужный девайс", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "📱 Xiaomi 14")
async def xiaomi_14_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Xiaomi 14.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "📱 Xiaomi 14T, 14T Pro")
async def xiaomi_14T_Pro_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Xiaomi 14T, 14T Pro.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "📱 Note 13")
async def note13_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Redmi Note 13.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)

@dp.message_handler(lambda message: message.text == "📱 Note 13 Pro")
async def note13_pro_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Redmi Note 13 Pro.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "📱 Note 13 Pro+ 5G")
async def note13_pro_plus_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Redmi Note 13 Pro+ 5G.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)

@dp.message_handler(lambda message: message.text == "📱 Poco F5/F5 Pro")
async def poco_f5_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/POCO F5   F5 Pro.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "📱 Poco F6/F6 Pro")
async def poco_f6_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/POCO F6 and F6 Pro.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "🧹 G20")
async def g20_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Xiaomi_G20.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "🧹 G20 max")
async def g20max_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Xiaomi_G20_MAX.pdf", "rb") as document:
        await bot.send_document(chat_id=message.chat.id, document=document)
        await message.reply("Держи полезные материалы")
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "🧹 Truclean W20 Wet Dry Vacuum")
async def w20_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Xiaomi_Truclean_W20_Wet_Dry_Vacuum.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "🤖 X20+")
async def x20plus_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Xiaomi_Robot_vacuum_X20+.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)

@dp.message_handler(lambda message: message.text == "🤖 S20+")
async def s20plus_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Xiaomi_Robot_vacuum_S20+.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


@dp.message_handler(lambda message: message.text == "🤖 S20")
async def s20_handler(message: types.Message):
    with open("D:/PycharmProjects/Домашние задания/ДЗ telegram-bot_quiz/файлы/Xiaomi_Robot_Vacuum_S20.pdf", "rb") as document:
        await message.reply("Держи полезные материалы")
        await bot.send_document(chat_id=message.chat.id, document=document)
        user_id = message.from_user.id
        name_document = message.text
        insert_into_table_Documents(user_id, name_document)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)