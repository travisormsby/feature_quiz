# PyScript version of the quiz, intended to be run in the browser

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
    
feature_dict = {
        '1': ['Numeric data type', random_int_or_float],
        '2': ['Boolean data type', random_bool],
        '3': ['String data type', random_string],
        '4': ['List data type', random_list],
        '5': ['Tuple data type', random_tuple],
        '6': ['Access sequence elements by index', random_index_access],
        '7': ['Dictionary data type', random_dict],
        '8': ['Variable asignment', random_variable],
        '9': ['Conditional', random_conditional],
        '10': ['Loop over elements in sequence', random_loop],
        '11': ['Function call', random_function_call],
        '12': ['Function definition', random_function_def],
        '13': ['Bring in external modules', random_full_import],
        '14': ['Bring in a portion of an external module', random_from_import],
        '15': ['Access file', random_open]
}

# Number of times you must correctly identify a feature to complete the game
correct_needed = 1

# Make a dict to hold the score for each feature
# This dict will be purposefully mutated as a default argument
score_dict = {k:0 for k, v in feature_dict.items()}

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

def show_choices(choice_dict=feature_dict):
    """
    show the answer choices
    """
    options_div = document.querySelector("#options")
    options_html = "<ol>"
    for func in choice_dict.values():
        options_html += f"<li>{func[0]}</li>"
    options_html += "</ol>"
    options_div.innerHTML = options_html

def check_answer(event, feature_dict=feature_dict, score_dict=score_dict, correct_needed=correct_needed):
    """
    Update the score
    """
    answer = document.querySelector(".answer").value
    correct_answer = event.target.id
    response_div = document.querySelector("#response")
    document.querySelector(".answer").value = ""
    button = document.querySelector(".continue")

    if answer is None or not answer.isnumeric() or answer != correct_answer:
        button.id = "incorrect"
        if answer in score_dict.keys():
            score_dict[answer] -= 1
            answer = feature_dict[answer][0] # convert numeric answer to function description
        else:
            random_answer = random.choice(list(score_dict.keys()))
            score_dict[random_answer] -= 1
        score_dict[correct_answer] -= 1
        response_div.innerText = f"{answer} is incorrect. The correct answer is: {feature_dict[correct_answer][0]}. Click Continue to keep playing."
    else:
        button.id = correct_answer
        score_dict[answer] += 1
        response_div.innerText = (f"{feature_dict[answer][0]} is correct! Click Continue to keep playing.")
    display_score(score_dict, correct_needed)

def set_display():
    """
    Remove the introduction / instructions
    """
    pydom['.answer'][0].style["display"] = 'inline'
    pydom['.submit'][0].style["display"] = 'inline'
    pydom['#intro'][0].style["display"] = 'none'
    document.querySelector('.continue').innerText = "Continue"
    document.querySelector('#response').innerText = ""

def display_score(score_dict, correct_needed):
    """
    display the score
    """
    score_div = document.querySelector("#score")
    score = sum(score_dict.values())
    score_div.innerText = f"Score: {score} / {len(score_dict) * correct_needed}"

def game_complete():
    """
    Clean up the display when the game is complete
    """
    document.querySelector("#question").innerText = "You've completed the quiz! Refresh the page to play again."
    document.querySelector("#feature").innerText = ""
    document.querySelector("#options").innerHTML = ""
    document.querySelector("#score").innerText = ""
    document.querySelector(".continue").id = "reset"
    pydom['.continue'][0].style["display"] = 'none'
    pydom['.answer'][0].style["display"] = 'none'
    pydom['.submit'][0].style["display"] = 'none'


def game(event, score_dict=score_dict, feature_dict=feature_dict, correct_needed=correct_needed):
    """
    play the game
    """
    set_display()

    if sum(score_dict.values()) == len(score_dict) * correct_needed:
        game_complete()
        score_dict = {k:0 for k, v in feature_dict.items()}

        # Recursive means you can only play 999 games without refreshing browser
        # This is an acceptable limitation
        return
    
    q_num = random.choice([k for k,v in score_dict.items() if v < correct_needed])
    _, q_func = feature_dict[q_num]
    
    show_question(q_num, q_func)
    show_choices()
    display_score(score_dict, correct_needed)