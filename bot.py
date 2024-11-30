import asyncio
from aiogram.filters.command import CommandObject
from aiogram.filters import Command
from aiogram.utils.formatting import (
    Bold, as_list, as_marked_section, as_key_value, HashTag
)
from email import message
import logging
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
import sqlite3

dbu = sqlite3.connect('Data2.db')
cu = dbu.cursor()
#cu.execute("""CREATE TABLE users(
#           id integer
#           flag integer
#           )""")

#animation="https://www.google.com/imgres?q=%D0%BC%D0%B0%D1%80%D1%88%D0%B0%D0%BA&imgurl=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fru%2F5%2F5c%2FMarshak_1934.jpg&imgrefurl=https%3A%2F%2Fru.wikipedia.org%2Fwiki%2F%25D0%259C%25D0%25B0%25D1%2580%25D1%2588%25D0%25B0%25D0%25BA%2C_%25D0%25A1%25D0%25B0%25D0%25BC%25D1%2583%25D0%25B8%25D0%25BB_%25D0%25AF%25D0%25BA%25D0%25BE%25D0%25B2%25D0%25BB%25D0%25B5%25D0%25B2%25D0%25B8%25D1%2587&docid=gut4xUGStLkOBM&tbnid=vY50Zg0WcYG0fM&vet=12ahUKEwinna7RiICKAxXpDRAIHYXcH4UQM3oECBUQAA..i&w=285&h=424&hcb=2&ved=2ahUKEwinna7RiICKAxXpDRAIHYXcH4UQM3oECBUQAA"
#    await message.answer_photo(
#        show_caption_above_media=False
#    )

#Open connection
#n = int(input())
#db = sqlite3.connect('Data1.db')
#c = db.cursor()
#c.execute("SELECT rowid, Text FROM Writes")
#items = c.fetchall()
#for el in items:
#    if(el[0] == n):
#        print(el[1] + "\n")

#logging.basicConfig(level=logging.INFO)

bot = Bot(token="7891480705:AAEr1AIcU4oFvMw3df5ttOWKDoXK9MWRzp4")

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
#    cu.execute(""" INSERT INTO users (id) VALUES (q) """)
    a=0
    m=open('text.txt', 'r')
    for w in m:
        if f"{message.from_user.id}" == m.read(10):
            a=1
            break
    m.close()
    if a==0:  
        m=open('text.txt', 'a')
        m.write(f"{message.from_user.id}\n")
        m.close()
        h=open('Data.txt', 'r')
        p=h.read()
        b = int(p.replace(',',''))
        b=b+1
        h.close()
        h=open('Data.txt', 'w')
        h.write(f"{b}")
        h.close()






    kb = [
        [
            types.KeyboardButton(text="О боте"),
            types.KeyboardButton(text="Расскажите о ваших предпочтениях")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Ы squad presents"
    )
    await message.answer("Доброго времени суток, пожалуйста проведите настройку бота", reply_markup=keyboard)

@dp.message(F.text.lower() == "о боте")
async def with_puree(message: types.Message):
    animation="https://yapx.ru/album/YOYL7"
    await message.answer_photo(
        animation,
        caption="Бот рекомендующий книги, места культурного наследия Воронежа, отправляющий интересные стихи и произведения. С ним интересно изучать новое и познавать литературу Воронежской земли. После быстрой и простой настройки бот сможет отправлять интересующие вас произведения исскуства.",
        show_caption_above_media=False
    )

@dp.message(F.text.lower() == "выход")
async def cmd(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="О боте"),
            types.KeyboardButton(text="Расскажите о ваших предпочтениях")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Ы squad presents"
    )
    await message.answer("Меню",reply_markup=keyboard)

@dp.message(F.text.lower() == "расскажите о ваших предпочтениях")
async def without_puree(message: types.Message):
    settings = [
        [
            types.KeyboardButton(text="Интересных стихотворений"),
            types.KeyboardButton(text="Рекомендуемое к прочтению")
        ],
        [
            types.KeyboardButton(text="Выход"),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=settings,
        resize_keyboard=True,
        input_field_placeholder="Рассылка:"
    )
    await message.reply("Какую рассылку вы хотите настроить?", reply_markup=keyboard)

@dp.message(F.text.lower() == "интересных стихотворений")
async def without_puree(message: types.Message):
    settings = [
        [
            types.KeyboardButton(text="Не хочу их видеть"),
            types.KeyboardButton(text="Не против просмотра"),
            types.KeyboardButton(text="Высокий приоритет")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=settings,
        resize_keyboard=True,
        input_field_placeholder="Приоритет"
    )

    await message.reply("Расставьте приоритет рассылки красивейших литературных произведений", reply_markup=keyboard)
    @dp.message(F.text.lower() == "не хочу их видеть")
    #переменная в базе данных стихотворения=0
    async def cmd_start(message: types.Message):
        h=open('stihy.txt', 'r')
        p=h.read()
        b = int(p.replace(',',''))
        b=b+0
        h.close()
        h=open('stihy.txt', 'w')
        h.write(f"{b}")
        h.close()
        
        settings = [
            [
                types.KeyboardButton(text="Интересных стихотворений"),
                types.KeyboardButton(text="Рекомендуемое к прочтению")
            ],
            [
                types.KeyboardButton(text="Выход"),
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=settings,
            resize_keyboard=True,
            input_field_placeholder="Рассылка:"
        )
        await message.reply("Выполнено")
        await message.answer("Какую рассылку вы хотите настроить?", reply_markup=keyboard)


    @dp.message(F.text.lower() == "не против просмотра")
    #переменная в базе данных стихотворения=1
    async def cmd_start(message: types.Message):
        h=open('stihy.txt', 'r')
        p=h.read()
        b = int(p.replace(',',''))
        b=b+1
        h.close()
        h=open('stihy.txt', 'w')
        h.write(f"{b}")
        h.close()
        
        settings = [
            [
                types.KeyboardButton(text="Интересных стихотворений"),
                types.KeyboardButton(text="Рекомендуемое к прочтению")
            ],
            [
                types.KeyboardButton(text="Выход"),
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=settings,
            resize_keyboard=True,
            input_field_placeholder="Рассылка:"
        )
        await message.reply("Выполнено")
        await message.answer("Какую рассылку вы хотите настроить?", reply_markup=keyboard)


    @dp.message(F.text.lower() == "высокий приоритет просмотра")
    #переменная в базе данных стихотворения=2
    async def cmd_start(message: types.Message):
        h=open('stihy.txt', 'r')
        p=h.read()
        b = int(p.replace(',',''))
        b=b+2
        h.close()
        h=open('stihy.txt', 'w')
        h.write(f"{b}")
        h.close()
        
        settings = [
            [
                types.KeyboardButton(text="Интересных стихотворений"),
                types.KeyboardButton(text="Рекомендуемое к прочтению")
            ],
            [
                types.KeyboardButton(text="Выход"),
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=settings,
            resize_keyboard=True,
            input_field_placeholder="Рассылка:"
        )
        await message.reply("Выполнено")
        await message.answer("Какую рассылку вы хотите настроить?", reply_markup=keyboard)

@dp.message(F.text.lower() == "рекомендуемое к прочтению")
async def without_puree(message: types.Message):
    settings = [
        [
            types.KeyboardButton(text="Не хочу их видеть"),
            types.KeyboardButton(text="Не против просмотра"),
            types.KeyboardButton(text="Высокий приоритет просмотра")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=settings,
        resize_keyboard=True,
        input_field_placeholder="Приоритет"
    )

    await message.reply("Расставьте приоритет рассылки познавательных книг", reply_markup=keyboard)
    @dp.message(F.text.lower() == "не хочу их видеть")
    #переменная в базе данных произведения=0
    async def cmd_start(message: types.Message):
        h=open('knigy.txt', 'r')
        p=h.read()
        b = int(p.replace(',',''))
        b=b+0
        h.close()
        h=open('knigy.txt', 'w')
        h.write(f"{b}")
        h.close()
        
        settings = [
            [
                types.KeyboardButton(text="Интересных стихотворений"),
                types.KeyboardButton(text="Рекомендуемое к прочтению")
            ],
            [
                types.KeyboardButton(text="Выход"),
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=settings,
            resize_keyboard=True,
            input_field_placeholder="Рассылка:"
        )
        await message.reply("Выполнено")
        await message.answer("Какую рассылку вы хотите настроить?", reply_markup=keyboard)


    @dp.message(F.text.lower() == "не против просмотра")
    #переменная в базе данных произведения=1
    async def cmd_start(message: types.Message):
        h=open('knigy.txt', 'r')
        p=h.read()
        b = int(p.replace(',',''))
        b=b+1
        h.close()
        h=open('knigy.txt', 'w')
        h.write(f"{b}")
        h.close()
        
        settings = [
            [
                types.KeyboardButton(text="Интересных стихотворений"),
                types.KeyboardButton(text="Рекомендуемое к прочтению")
            ],
            [
                types.KeyboardButton(text="Выход"),
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=settings,
            resize_keyboard=True,
            input_field_placeholder="Рассылка:"
        )
        await message.reply("Выполнено")
        await message.answer("Какую рассылку вы хотите настроить?", reply_markup=keyboard)


    @dp.message(F.text.lower() == "высокий приоритет просмотра")
    
    async def cmd_start(message: types.Message):
        h=open('knigy.txt', 'r')
        p=h.read()
        b = int(p.replace(',',''))
        b=b+2
        h.close()
        h=open('knigy.txt', 'w')
        h.write(f"{b}")
        h.close()
        
        settings = [
            [
                types.KeyboardButton(text="Интересных стихотворений"),
                types.KeyboardButton(text="Рекомендуемое к прочтению")
            ],
            [
                types.KeyboardButton(text="Выход"),
            ],
        ]
        keyboard = types.ReplyKeyboardMarkup(
            keyboard=settings,
            resize_keyboard=True,
            input_field_placeholder="Рассылка:"
        )
        await message.reply("Выполнено")
        await message.answer("Какую рассылку вы хотите настроить?", reply_markup=keyboard)

@dp.message(Command("id"))
async def cmd_start(message: types.Message):
    await message.answer(f"{message.from_user.id}")


@dp.message(Command("sendall"))
async def send(message: types.Message):
    if f"{message.from_user.id}"=="1950908998":
        await message.answer("Ожидаю текст для отправки")
        @dp.message(F.text)
        async def send(message: types.Message):
            if f"{message.from_user.id}"=="1950908998":
                c=message.text
                m=open('text.txt', 'r')
                i=0
                h=open('Data.txt')
                q=h.read()
                v=int(q)
                while i<v:
                    k=m.readline()
                    await bot.send_message(f"{k}", f"{c}")
                    i=i+1
                await message.answer('Done')
                m.close()
      
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
