from random import randint, shuffle

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
    
# def generate_correct_expression(correct_result):
#     while True:
#         tmp_expression = generate_double_expression()
#         if eval(tmp_expression) == correct_result:
#             return tmp_expression
#         tmp_expression = generate_triple_expression()
#         if eval(tmp_expression) == correct_result:
#             return tmp_expression

# def make_dict(expression, correct=False):
#     tmp_dict = dict(zip(['text', 'callback_data'], [expression, f'answer_{correct}']))
#     return tmp_dict

# def generate_buttons():
#     result = generate_result()
#     list = [make_dict(generate_correct_expression(result), True)]
#     for i in range(2):
#         list.append(make_dict(generate_double_expression()))
#     list.append(make_dict(generate_triple_expression()))
#     shuffle(list)
#     return list, result

def generate_list():
    list = [generate_double_expression(), generate_triple_expression(), generate_double_expression(), generate_triple_expression()]
    shuffle(list)
    return list