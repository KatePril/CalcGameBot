import logging
from aiogram import Bot, Dispatcher, executor, types
from decouple import config
from expressions import give_expression

API_TOKEN = config('API_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

expressions = 0
points = 0
correct = 0
incorrect = 0

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm CalcGameBot!\nPowered by aiogram.\nType '/next' to get the expression")

@dp.callback_query_handler(text_contains='correct_') 
async def plus(call: types.CallbackQuery):
    global expressions, points, correct
    expressions = expressions + 1
    correct = correct + 1
    points = points + 1
    await call.message.answer('+1 points\n/next\n/stop_game')
    
@dp.callback_query_handler(text_contains='wrong_') 
async def minus(call: types.CallbackQuery):
    global expressions, points, incorrect
    expressions = expressions + 1
    incorrect = incorrect + 1
    if points > 0:
        points = points - 1
        await call.message.answer('-1 points\n/next\n/stop_game')
    else:
        await call.message.answer('0 points\n/next\n/stop_game')
    
@dp.message_handler(commands='stop_game')
async def end_game(message: types.Message):
    global expressions, points, correct, incorrect
    await message.reply(f'Your points are {points}.\nYou have solved {expressions} expressions with {correct} correct and {incorrect} incorrect')
    if correct > incorrect:
        await message.answer_sticker('CAACAgIAAxkBAANRZCcax0l86nyq-EKOzyZRT2GE-pYAAtsPAAK5GRBKnttZU3ZDWm4vBA')
    else:
        await message.answer_sticker('CAACAgIAAxkBAANSZCcay46nFGm1hFN5QS2LQgc5DugAAqgSAALBLBBK6if4dAPxg-QvBA')
    expressions = 0
    points = 0
    correct = 0
    incorrect = 0
    
@dp.message_handler(commands='next')
async def next(message: types.Message):
    expected_result, markup = give_expression()
    await message.answer(expected_result, reply_markup=markup)
    
@dp.message_handler(content_types=types.ContentType.STICKER)
async def echo(message: types.Message):
    print(message.sticker.file_id)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
            
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)