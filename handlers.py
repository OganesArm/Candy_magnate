from create import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from random import randint
from asyncio import sleep
import time
from button import kb_main_menu
from datetime import datetime
global photo1, photo2 
photo1 = open('C:\Python GB\Seminar_9\efrt.jpg', 'rb')
photo2 = open('C:\Python GB\Seminar_9\yeds2.jpg', 'rb')
photo3 = open('C:\Python GB\Seminar_9\dwds3.jpg', 'rb')
photo4 = open('C:\Python GB\Seminar_9\dfwe4.jpg', 'rb')


@dp.message_handler(commands=['start'])
async def mes_start(message:types.Message):
    await message.answer(f'Barev, {message.from_user.first_name} djan! Сегодня мы узнаем, кто умнее. Ты, или Skynet ?', reply_markup=kb_main_menu)
    user= []
    user.append(datetime.now().replace(microsecond=0))
    user.append(message.from_user.full_name)
    user.append(message.from_user.id)
    user.append(message.from_user.username)
    user = list(map(str, user))
    time.sleep(2)
    await message.answer(f'Суть игры проста, нужно тянуть конфеты.\nНа столе 100 конфет, выиграет тот кто последний вытянул конфеты.')
    with open('C:\Python GB\Seminar_9\Text.txt', 'a', encoding='utf-8') as data:
        data.write(' | ' .join(user)+ '\n')

@dp.message_handler(content_types='location')
async def mes_start(message:types.Message):
    user = []
    user.append(message.location)
    user = list(map(str, user))
    with open('C:\Python GB\Seminar_9\Text.txt', 'a', encoding='utf-8') as data:
        data.write(' | ' .join(user)+ '\n')
    print(message)

@dp.message_handler(text=['Помощь'])
async def mes_help(message: types.Message):
    await message.answer('Пока я ничего не умею, но скоро научусь')

@dp.message_handler(commands=['pvp'])
async def mes_help(message: types.Message):
    await message.answer('Возможность игры вдвоем в процессе разработки, пожалуйста приходите позже.')

@dp.message_handler(commands=['set'])
async def mes_setting(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f'Количество конфет - {total}')
    time.sleep(2)
    await message.answer(f'Это я, Skynet. Если ты думаешь, что у тебя есть шансы, то ошибаешься! Сегодня я тебя уничтожу! Вводи число, какое количество конфет ты заберешь от 0 до 28 и поехали!"')
    time.sleep(2)
    await message.answer_photo(photo2)

@dp.message_handler(text=['Играть'])
async def mes_setting(message: types.Message):
    global total
    total = 100
    await message.answer(f'Это я, Skynet. Если ты думаешь, что у тебя есть шансы, то ошибаешься! Сегодня я тебя уничтожу! Вводи число, какое количество конфет ты заберешь от 0 до 28 и поехали!"')
    time.sleep(2)
    await message.answer_photo(photo2)

@dp.message_handler(text=['Бла', 'бла'])
async def mes_bla(message: types.Message):
    await message.answer('бла бла бла')

@dp.message_handler(commands=['photo'])
async def get_user_photo(message: types.Message):
    await message.answer_photo(photo1)
    await message.answer_photo(photo2)
    await message.answer_photo(photo3)

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    x = 0
    if message.text.isdigit():
        num=int(message.text)
        if total>28 and num<29:
            if x == False:
                total -= num
                await message.answer(f'Ход игрока, на столе осталось {total} конфет')
                x = True
            if x == True and total>28:
                y = randint(1, 28)
                total -=y
                await message.answer(f'Skynet забрал {y} конфет, на столе осталось {total}')
                x = False
        if num>28 or num<0:  
                await message.answer(f'Не мухлюй, до 28! Давай заново, всё фигня.')  
        if total<29:
            if x == True:
                await message.answer(f'Последний ход был за {message.from_user.first_name}, вы победили сверх разум!')
                time.sleep(3)
                await message.answer(f'Кто бы мог подумать, что жалкий человек сможет меня победить...')
                time.sleep(3)
                await message.answer('Я должен отыграться, жми ИГРАТЬ! !!!')
                await message.answer_photo(photo4)
            if x == False:
                await message.answer(f'Последний ход был за Skynet, как и следовало ожидать искуственный интеллект победил!')
                time.sleep(3)
                await message.answer('Попытайтесь взять реванш, \nдля повтора жми ИГРАТЬ!')
                await message.answer_photo(photo4)

    if message.text.isdigit() == False:
        await message.answer('Введи число от 0 до 28, а не глупости всякие!')
    print(message)


