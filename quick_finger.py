from datetime import datetime

LEVELS = {
    "1": "Simple text",
    "2": "Medium level text",
    "3": "So hard text for breaking fingers"
}

def choise_level():
    level = input("Choise level(1, 2, 3):")
    if level not in LEVELS.keys():
        print("Wrong level choise!")
        text = check_input_text()
    else:
        text = LEVELS[level]
    return text


def check_input_text(user_text, game_text):
    if user_text != game_text:
        print("So bad!")
    else:
        print("NICE!")


def calculate_result(time):
    if time.minutes < 1:
        print("Super good time!")
    elif 1 < time.minutes < 5:
        print("Not bad")
    else:
        print("So bad!")


def start_game():

    print("Hello do u want play? Let's start!")
    text = choise_level()
    print(text)
    start = datetime.now()
    user_input_text = input("Type your text: ")
    end = start - datetime.now()
    calculate_result(end)
    check_input_text(user_input_text, text)

def quick_fingers():
    while True:
        start_game()
        user_choice = input('Do you want to play again? (yes/no)\n')
        if user_choice.lower() == 'no':
            break
    print('Goodbye!')


start = datetime.datetime.now()
def text_1():
    text = '''Пустое вы сердечным ты    
Она, обмолвясь, заменила
И все счастливые мечты
В душе влюбленной возбудила.
Пред ней задумчиво стою,
Свести очей с нее нет силы;
И говорю ей: как вы милы!
И мыслю: как тебя люблю!'''
    print(text)

def quick_finger():
    print('''
          Привет добропожаловать в игру "Quick Finger"!
            выберите уровень сложности:
            1. Легкий
            2. Средний
            3. Сложный
    ''')
    level = input('Enter the level: ')
    text = ''
    if level == 1:
        text = '''Пустое вы сердечным ты'''
    elif level == 2:
        text = '''Пустое вы сердечным ты
Она, обмолвясь, заменила
И все счастливые мечты
В душе влюбленной возбудила.
Пред ней задумчиво стою,
Свести очей с нее нет силы;
И говорю ей: как вы милы!
И мыслю: как тебя люблю!'''
        print(text)
    elif level == 3:
        text = '''Я вас люблю, — хоть я бешусь,
Хоть это труд и стыд напрасный,
И в этой глупости несчастной
У ваших ног я признаюсь!
Мне не к лицу и не по летам…
Пора, пора мне быть умней!
Но узнаю по всем приметам
Болезнь любви в душе моей:
Без вас мне скучно, — я зеваю;
При вас мне грустно, — я терплю;
И, мочи нет, сказать желаю,
Мой ангел, как я вас люблю!
Когда я слышу из гостиной
Ваш легкий шаг, иль платья шум,
Иль голос девственный, невинный,
Я вдруг теряю весь свой ум.'''
        print(text)
    print(text)
    user_text = input('Enter the text: ')
    if text == user_text:
        print("пять по русскому")
    else:
        print('плохо учился')
    print()
quick_finger()
print(f'Скорость печати: {datetime.datetime.now()-start}')

def text():
    text = '''Пустое вы сердечным ты    
Она, обмолвясь, заменила
И все счастливые мечты
В душе влюбленной возбудила.
Пред ней задумчиво стою,
Свести очей с нее нет силы;
И говорю ей: как вы милы!
И мыслю: как тебя люблю!'''
    print(text)
