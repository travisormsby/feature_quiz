import random
from pyscript import document
from pyweb import pydom

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
    
default_func_list = [
        ['numeric data type', random_int_or_float],
        ['boolean data type', random_bool],
        ['string data type', random_string],
        ['list data type', random_list],
        ['tuple data type', random_tuple],
        ['access sequence elements by index', random_index_access],
        ['dictionary data type', random_dict],
        ['variable asignment', random_variable],
        ['conditional', random_conditional],
        ['loop over elements in sequence', random_loop],
        ['function call', random_function_call],
        ['function definition', random_function_def],
        ['bring a module into your code', random_full_import],
        ['bring a portion of a module into your code', random_from_import],
        ['access file', random_open]
]

# Purposefully mutating func list default arg
# Make a copy of the default list to avoid mutating the orginal
func_list = default_func_list[:]

def show_question(q_num, q_func):
    """
    print the question
    """
    question_div = document.querySelector("#question")
    feature_div = document.querySelector("#feature")
    button = document.querySelector(".submit")
    
    # hold the right answer in the button id
    button.id = q_num

    question_div.innerText = "Which Python feature does the following code snippet represent?"
    if q_func == random_string or q_func == random_bool:
        feature_div.innerText = repr(q_func())
    else: 
        feature_div.innerText = q_func()

def show_choices(func_list):
    """
    show the answer choices
    """
    options_div = document.querySelector("#options")
    options_html = "<ol>"
    for func in func_list:
        options_html += f"<li>{func[0]}</li>"
    options_html += "</ol>"
    options_div.innerHTML = options_html

def check_answer(event):
    """
    check if the answer is correct
    """
    answer = document.querySelector(".answer").value
    correct_answer = event.target.id
    response_div = document.querySelector("#response")
    document.querySelector(".answer").value = ""
    button = document.querySelector(".continue")

    if answer is None or not answer.isnumeric() or answer != correct_answer:
        button.id = "incorrect"
        response_div.innerText = f"{answer} is incorrect. The correct answer is: {correct_answer}. Click Continue to keep playing."
    else:
        button.id = correct_answer
        response_div.innerText = (f"{answer} is correct! Click Continue to keep playing.")

def reset_display():
    answer_input = pydom['.answer'][0]
    answer_input.style["display"] = 'inline'
    submit_button = pydom['.submit'][0]
    submit_button.style["display"] = 'inline'
    intro_div = pydom['#intro'][0]
    intro_div.style["display"] = 'none'
    response_div = document.querySelector('#response')
    response_div.innerText = ""

def mutate_func_list(event, func_list=func_list):
    """
    remove the correct answer from the function list
    """
    if event.target.id.isnumeric():
        if len(func_list) == 0:
            # reset the func_list
            func_list = default_func_list[:]
        
        func_list.pop(int(event.target.id)-1)
        
        if len(func_list) == 0:
            # reset the func_list
            func_list = default_func_list[:]
        
    return func_list

def game(event, func_list=func_list):
    """
    play the game
    """
    reset_display()
    func_list = mutate_func_list(event)
    
    q_num = random.randint(1, len(func_list))
    _, q_func = func_list[q_num-1]
    
    show_question(q_num, q_func)
    show_choices(func_list)

    continue_button = document.querySelector(".continue")
    continue_button.id = "incorrect"