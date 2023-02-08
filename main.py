from aiogram import Bot, Dispatcher, executor, types
from handlers import dp

total = 50
async def on_start(_):
    print('Bot start!')


executor.start_polling(dp, skip_updates=True, on_startup=on_start)   #должно быть всегда в самом низу