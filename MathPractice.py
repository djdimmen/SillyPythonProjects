# MathPractice.py
import random
import os
import time

MIN_NUMBER = 0  # Minimum number for random generation
MAX_NUMBER = 10  # Maximum number for random generation
NUM_OF_QUESTIONS = 20  # Default number of questions

correct_resp = ['Correct!', 'Well done!', 'Great job!', 'You got it!', 'Nice work!', 'Excellent!', 'Fantastic!', 'Brilliant!', 'Superb!', 'Right on!', 'Rock on!']
incorrect_resp = ['Not quite.', 'Almost, but not quite.', 'Nope! Sorry.', 'No, but don\'t give up!', 'Stay focused!', 'No, but keep at it!', 'Almost there!', 'Tighten up!']

def set_difficulty():
    print("Select difficulty level:")
    print("1. Easy (numbers 0-10)")
    print("2. Medium (numbers 0-50)")
    print("3. Hard (numbers 0-100)")
    print("4. Word Problems")
    choice = input(":> ").strip()
    
    global MAX_NUMBER
    if choice == '1':
        MAX_NUMBER = 10
    elif choice == '2':
        MAX_NUMBER = 50
    elif choice == '3':
        MAX_NUMBER = 100
    elif choice == '4':
        print("Practicing word problems.")
        time.sleep(2)
    else:
        print("Invalid choice, defaulting to Easy.")
        MAX_NUMBER = 10

    return choice

def Greeting():
    message1 = "Welcome to the Math Practice Program!"
    message2 = "You can practice addition, subtraction, multiplication, and division."
    message3 = "Let's get started!"
    print('=========================================================================')
    print('\n')
    print(message1)
    print(message2)
    print('\n')
    print(message3)
    print('=========================================================================')

def get_inputs():
    # Receive a number to practice against
    while True:
        print("Enter a number to practice against (e.g., 2, 3, 4, 5, etc.) ")
        user_input = input(":> ").strip()
        try:
            number = int(user_input)
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Receive the operator to practice (+, -, *, /)
    valid_operators = ['+', '-', '*', '/']
    while True:
        print("Enter the operator to practice (+, -, *, /) ")
        operator = input(":> ").strip()
        if operator in valid_operators:
            break
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")

    return number, operator

def post_basic_problem(number, operator, question_num):
    print("Enter 'exit' to quit at any time.\n")
    
    if operator == '+':
        a = number
        b = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(f"{question_num}/{NUM_OF_QUESTIONS}) What is {a} + {b}?")
        answer = a + b
    elif operator == '-':
        a = number
        b = random.randint(MIN_NUMBER, MAX_NUMBER)
        if a > b:
            print(f"{question_num}/{NUM_OF_QUESTIONS}) What is {a} - {b}?")
            answer = a - b
        else:
            print(f"{question_num}/{NUM_OF_QUESTIONS}) What is {b} - {a}?")
            answer = b - a 
    elif operator == '*':
        a = number
        b = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(f"{question_num}/{NUM_OF_QUESTIONS}) What is {a} * {b}?")   
        answer = a * b
    elif operator == '/':
        div_min = MIN_NUMBER + 1
        a = number
        b = random.randint(div_min, MAX_NUMBER)
        print(f"{question_num}/{NUM_OF_QUESTIONS}) What is {a} / {b}?")
        answer = a / b

    return answer

def post_word_problem(question_num):
    """Prints a question to the screen and returns the answer for the posted question."""
    print("Enter 'exit' to quit at any time.\n")

    random_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack', 'Scarlet', 'Andy', 'Charlotte', 'Jenny', 'Albus', 'Hermione', 'Ron', 'Harry', 'Snape']
    random_items = ['apples', 'bananas', 'oranges', 'grapes', 'pears', 'peaches', 'mangoes', 'cherries', 'plums', 'kiwis', 'wands', 'toads', 'owls', 'broomsticks']

    chosen_name = random.choice(random_names)
    chosen_item = random.choice(random_items)
    large_num = random.randint(3,20)
    small_num = random.randint(2,large_num)

    chosen_operator = random.choice(['addition', 'subtraction'])

    ## Addition problems
    addition_word_problems = [
        f'"{chosen_name} has {large_num} {chosen_item}. If {chosen_name} gets {small_num} {chosen_item} more, how many {chosen_item} do they have now?"',
        f'"{chosen_name} has {large_num} {chosen_item}. If {chosen_name} gets {small_num} extra {chosen_item}, how many {chosen_item} do they have now?"',
        f'"{chosen_name} has {large_num} {chosen_item}. If {chosen_name} gets {small_num} new {chosen_item}, how many {chosen_item} do they have now?"',
        f'"{chosen_name} buys {large_num} {chosen_item}. If {chosen_name} buys {small_num} more {chosen_item}, how many {chosen_item} do they own now?"'
    ]
    
    ## Subtraction problems
    subtraction_word_problems = [
        f'"{chosen_name} has {large_num} {chosen_item}. If {chosen_name} loses {small_num} {chosen_item}, how many {chosen_item} do they have now?"',
        f'"{chosen_name} has {large_num} {chosen_item}. If {chosen_name} gives away {small_num} {chosen_item}, how many {chosen_item} do they have now?"',
        f'"{chosen_name} is holding {large_num} {chosen_item}. If {chosen_name} drops {small_num} {chosen_item}, how many {chosen_item} are they still holding?"'
    ]
    
    if chosen_operator == 'addition':
        word_problem = random.choice(addition_word_problems)
        answer = 1
    elif chosen_operator == 'subtraction':
        word_problem = random.choice(subtraction_word_problems)
        answer = 2
    
    print(f"{question_num}/{NUM_OF_QUESTIONS})")
    print(word_problem, '\n')
    print("What does this problem require?")
    print("  1. Addition")
    print("  2. Subtraction")
    
    return answer
    
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    clear_screen()
    
    Greeting()

    difficulty = set_difficulty()

    if difficulty != '4':
        number, operator = get_inputs()

    clear_screen()

    correct_count = 0
    incorrect_count = 0
    question_num = 1

    for _ in range(NUM_OF_QUESTIONS):
        if difficulty == '4':
            answer = post_word_problem(question_num)
        else:
            answer = post_basic_problem(number, operator, question_num)

        user_answer = input(":> ").strip()
        try:
            if user_answer == 'exit':
                print("\nExiting the practice session.")
                print(".")
                time.sleep(0.75)
                print("..")
                time.sleep(0.75)
                print("...")
                time.sleep(0.75)
                print("....")
                time.sleep(0.75)
                print(".....")
                time.sleep(0.75)
                break
            elif int(user_answer) != answer:
                print(f"{random.choice(incorrect_resp)} \nThe correct answer is {answer}.\n")
                incorrect_count += 1
            elif int(user_answer) == answer:
                print(random.choice(correct_resp) + "\n")
                correct_count += 1
        except ValueError as e:
                print(f"{random.choice(incorrect_resp)} \nThe correct answer is {answer}.\n")
                incorrect_count += 1
                
        question_num += 1
        time.sleep(3)
        clear_screen()
    
    clear_screen()
    print("Thanks for practicing math!\n")
    print(f'You got {correct_count} correct and {incorrect_count} incorrect.')
    if correct_count > incorrect_count:
        print("Great job!\n")
    else:
        print("Keep practicing and you'll get better!\n")
    print("Goodbye!")
    print('=========================================================================')
    time.sleep(8) 