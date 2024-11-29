import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
import sqlite3

#Open connection
db = sqlite3.connect('Data1.db')
c = db.cursor()
c.execute("SELECT rowid, Text FROM Writes")
print(c.fetchall())

logging.basicConfig(level=logging.INFO)

bot = Bot(token="7891480705:AAEr1AIcU4oFvMw3df5ttOWKDoXK9MWRzp4")
admin_id="1950908998"

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="О боте"),
            types.KeyboardButton(text="Настройки")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Ы squad presents"
    )
    await message.answer("Доброго времени суток", reply_markup=keyboard)

@dp.message(F.text.lower() == "о боте")
async def with_puree(message: types.Message):
    animation="https://www.google.com/imgres?q=%D0%BC%D0%B0%D1%80%D1%88%D0%B0%D0%BA&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fru%2F5%2F5c%2FMarshak_1934.jpg&imgrefurl=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%259C%25D0%25B0%25D1%2580%25D1%2588%25D0%25B0%25D0%25BA%2C_%25D0%25A1%25D0%25B0%25D0%25BC%25D1%2583%25D0%25B8%25D0%25BB_%25D0%25AF%25D0%25BA%25D0%25BE%25D0%25B2%25D0%25BB%25D0%25B5%25D0%25B2%25D0%25B8%25D1%2587&docid=gut4xUGStLkOBM&tbnid=vY50Zg0WcYG0fM&vet=12ahUKEwinna7RiICKAxXpDRAIHYXcH4UQM3oECBUQAA..i&w=285&h=424&hcb=2&ved=2ahUKEwinna7RiICKAxXpDRAIHYXcH4UQM3oECBUQAA"
    await message.answer_photo(
        animation,
        caption="Бот рекомендующий книги, места культурного наследия Воронежа, отправляющий интересные стихи и произведения. С ним интересно изучать новое и познавать литературу Воронежской земли",
        show_caption_above_media=False
    )


@dp.message(F.text.lower() == "настройки")
async def without_puree(message: types.Message):
    settings = [
        [
            types.KeyboardButton(text="Достопримечательностей"),
            types.KeyboardButton(text="Интересных стихотворений"),
            types.KeyboardButton(text="Рекомендуемое к прочтению")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=settings,
        resize_keyboard=True,
        input_field_placeholder="Рассылка:"
    )
    await message.reply("Что хотите настроить?", reply_markup=keyboard)


@dp.message(Command("id"))
async def cmd_start(message: types.Message):
    await message.answer(f"Ваш ID: {message.from_user.id}")

@dp.message(Command('sendall'))
async def send_all(message: types.Message):
    if message.chat.id==admin_id:
        for i in users:##если users-массив id пользователей
            await bot.send_message(i,message.text[message.text.find(' '):])
        await message.answer('Done')
        
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

#Close connection
db.close()