from random import randint, shuffle
from aiogram import types


# def generate_result():
#     return randint(0, 100)

def generate_number():
    return randint(1, 10)

def generate_action():
    actions = ['+', '-', '*', '/']
    return actions[randint(0, len(actions) - 1)]

def generate_double_expression():
    tmp = f'{generate_number()} {generate_action()} {generate_number()}'
    return tmp
    
def generate_triple_expression():
    tmp = f'{generate_number()} {generate_action()} {generate_number()} {generate_action()} {generate_number()}'
    return tmp

def generate_list():
    list = [generate_double_expression(), generate_triple_expression(), generate_double_expression(), generate_triple_expression()]
    shuffle(list)
    return list
   
def give_expression():
    expressions = generate_list()
    correct_answer_index = randint(0, 3)
    expected_result = eval(expressions[correct_answer_index])
    markup = types.InlineKeyboardMarkup()
    
    for expression in expressions:
        if eval(expression) == expected_result:
            markup.add(types.InlineKeyboardButton(expression, callback_data='correct_answer'))
        else:
            markup.add(types.InlineKeyboardButton(expression, callback_data='wrong_answer'))
    
    return expected_result, markup

