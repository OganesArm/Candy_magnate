from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu= ReplyKeyboardMarkup(resize_keyboard=True) #показать кнопки/ Сделать их одноразовыми  one_time_keyboard=True

btn_pvp=KeyboardButton('/pvp')
btn_help=KeyboardButton('Помощь')
btn_set=KeyboardButton('/set 100', )
btn_location=KeyboardButton('Моя геолокация🇦🇲', request_location=True)
btn_game=KeyboardButton('Играть')

kb_main_menu.add(btn_help, btn_pvp, btn_location, btn_game)