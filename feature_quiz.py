import random

counties = ('Hennepin', 'Ramsey', 'Dakota', 'Washington', 'Anoka', 'Carver', 'Scott', 'Olmsted', 'Winona')
units = ('millimeter', 'centimeter', 'meter', 'kilometer', 'hectare', 'square_meter')
prop_info = ('county', 'township', 'section', 'acreage', 'unit', 'owner', 'address', 'city', 'state', 'zip')
packages = ('pydub', 'pytz', 'pyperclip', 'pyautogui', 'pyquery', 'pyinstaller', 'pylint', 'pyodbc', 'pyserial', 'pyyaml')
functions = ('get_data', 'process_data', 'write_data', 'read_data', 'plot_data', 'analyze_data', 'clean_data', 'transform_data', 'load_data', 'save_data')

def random_string(depth=None, data=(counties, units, prop_info, packages, functions)):
    """
    return a random word
    """
    choice_list = list(random.choice(data))
    string_num = repr(random_int_or_float())
    string_bool = repr(random_bool())
    choice_list.extend([string_num, string_bool])
    return random.choice(choice_list)

def random_int_or_float(depth=None):
    """
    return a random integer or float
    """
    return random.choice([random.randint(0, 100), random.random()])

def random_bool(depth=None):
    """
    return a random boolean
    """
    return random.choice([True, False])
    
def random_code(depth=None):
    """
    return a string of Python code
    """
    if depth is None:
        depth = random.randint(1, 3)
    if depth == 0:
        return random.choice([random_string, random_int_or_float, random_bool])(depth)
    depth -= 1
    return random.choice([random_string, random_int_or_float, random_bool, random_list, random_tuple, random_dict])(depth)

def random_list(depth=1, min_len=1, max_len=10):
    """
    return a random list of random length
    """
    return [random_code(depth) for _ in range(random.randint(min_len, max_len))]

def random_tuple(depth=1, min_len=1, max_len=10):
    """
    return a random tuple of random length
    """
    return tuple(random_code(depth) for _ in range(random.randint(min_len, max_len)))

def random_index_access(depth=1):
    """
    return a string of Python code showing random index access
    """
    seq = random.choice([random_list, random_tuple])(depth, min_len=2)
    if random.random() < 0.5:
        return f"{seq}[{random.randint(0, len(seq) - 1)}]"
    start = random.randint(0, len(seq) - 1)
    end = random.randint(start + 1, len(seq))
    return f"{seq}[{start}:{end}]"

def random_dict(depth=1, data=prop_info):
    """
    return a random dictionary of random length
    """
    return {random.choice(data): random_code(depth) for _ in range(random.randint(1, 5))}

def random_variable(data=prop_info):
    """
    return a string of Python code showing assignment of a random value to a random variable name
    """
    return f'{random.choice(data)} = {random_code()}'

def random_conditional(data=prop_info):
    """
    return a string of Python code showing a random conditional statement
    """
    return f"if {random.choice(data)} {random.choice(['==', '>=', '<=', '>', '>', '!='])} {random_int_or_float()}:"

def random_loop(data=prop_info):
    """
    return a string of Python code showing a random loop
    """
    var = random.choice(data)
    return f"for {var} in {var}_list:"

def random_function_call(data=(counties, functions, prop_info)):
    """
    return a string of Python code showing a random function call
    """
    
    func_name = f"{random.choice(data[0])}_{random.choice(data[1])}".lower()
    return f"{func_name}({', '.join([i for i in random_list() if i in data[2]])})"

def random_function_def():
    """
    return a string of Python code showing a random function definition
    """
    return f"def {random_function_call()}:"

def random_full_import(data=packages):
    """
    return a string of Python code showing a random import statement
    """
    return f"import {random.choice(data).lower()}"

def random_from_import(data=(packages, functions)):
    """
    return a string of Python code showing a random from-import statement
    """
    return f"from {random.choice(data[0]).lower()} import {random.choice(data[1]).lower()}"

def random_open():
    """
    return a string of Python code showing a random open statement
    """
    open_mode = random.choice(["'r'", "'w'", "'a'"])
    return f"with open('{random_string()}.{random.choice(['csv', 'txt'])}', {open_mode}) as f:"
    
default_func_dict = {
        1: ['numeric data type', random_int_or_float],
        2: ['boolean data type', random_bool],
        3: ['string data type', random_string],
        4: ['list data type', random_list],
        5: ['tuple data type', random_tuple],
        6: ['access sequence elements by index', random_index_access],
        7: ['dictionary data type', random_dict],
        8: ['variable asignment', random_variable],
        9: ['conditional', random_conditional],
        10: ['for loop', random_loop],
        11: ['function call', random_function_call],
        12: ['function definition', random_function_def],
        13: ['import module', random_full_import],
        14: ['import portion of module', random_from_import],
        15: ['open file', random_open]
    }       

def get_answer(q_description, q_func, func_dict):
    """
    print the question and answer choices
    """
    print("\nWhich Python feature does the following code snippet represent?\n")
    if q_description == 'string data type':
        print(repr(q_func()), '\n')
    else: print(q_func(), '\n')
    for k, v in func_dict.items():
        print(f"{k}) {v[0]}")
    answer = input("Enter the number of the correct answer: ")
    return answer

def welcome():
    """
    print the welcome message
    """
    print("Welcome to the Python Feature Quiz!")
    print("You will be shown a snippet of Python code and you must determine which feature it represents.")
    print("You will be given a list of features to choose from.")
    print("Good luck!")

def continue_play(message):
    """
    ask the user if they want to play again
    """
    response = input(f"Press enter to {message} or 'q' to quit: ")
    if response.lower().startswith('q'):
        return False
    return True

def game(func_dict):
    """
    play the game
    """
    while True:
        q_num, [q_description, q_func]  = random.choice(list(func_dict.items()))
        answer = get_answer(q_description, q_func, func_dict)
        if answer is None or not answer.isnumeric() or int(answer) != q_num:
            print(f"Incorrect. The correct answer is: {q_num}) {q_description}")
        else:
            print("Correct!")
            func_dict = {k: v for k, v in func_dict.items() if k != q_num}
            if not func_dict:
                print("You've answered all the questions!")
                if not continue_play("play again"):
                    break
                func_dict = default_func_dict
                continue            
        if not continue_play("keep playing"):
            break

if __name__ == '__main__':
    welcome()
    if continue_play("start the quiz"):
        game(default_func_dict)
    print("Thanks for playing!")
    