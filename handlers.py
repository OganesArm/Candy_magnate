from create import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from random import randint
import time

global photo1, photo2 
photo1 = open('C:\Python GB\Seminar_9\efrt.jpg', 'rb')
photo2 = open('C:\Python GB\Seminar_9\yeds2.jpg', 'rb')
photo3 = open('C:\Python GB\Seminar_9\dwds3.jpg', 'rb')
photo4 = open('C:\Python GB\Seminar_9\dfwe4.jpg', 'rb')



@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Barev, {message.from_user.first_name} djan! Сегодня мы узнаем, кто умнее. Ты, или Skynet ?')
    time.sleep(2)
    await message.answer(f'Суть игры проста, нужно тянуть конфеты.\nВводи команду /set 100 где вместо 100 можетe быть любое число конфет. Выиграет тот, кто последний вытянул конфеты.')

@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Пока я ничего не умею, но скоро научусь')

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
                await message.answer('Я должен отыграться, вводи /set !!!')
                await message.answer_photo(photo4)
            if x == False:
                await message.answer(f'Последний ход был за Skynet, как и следовало ожидать искуственный интеллект победил!')
                time.sleep(3)
                await message.answer('Попытайтесь взять реванш, \nдля повтора /set')
                await message.answer_photo(photo4)

    if message.text.isdigit() == False:
        await message.answer('Введи число от 0 до 28, а не глупости всякие!')
    print(message)


