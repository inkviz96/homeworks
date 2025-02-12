import random
def anagramma():
    print('''
          Привет добропожаловать в игру "Anagramma"!
          слова которые ты можешь угадать:
            1. python
            2. java
            3. kotlin
            4. javascript
            5. колейдоскоп
            6. награмма 
            7. антарктида
            8. антарктика
    ''')
    
    words = ['python', 'java', 'kotlin', 'javascript', "колейдоскоп", 'награмма', 'антарктида', 'антарктика']
    word = random.choice(words)
    word_ran = list(word)
    for i in range(len(word_ran)):
        j = random.randint(0, len(word_ran) - 1)
        word_ran[i], word_ran[j] = word_ran[j], word_ran[i]
    user_choice = input(f'Guess the word: {"".join(word_ran)}\n')
    if user_choice.lower() == word.lower():
        print('Ты выиграл!')
    else:
        print('Ты проиграл!')
while True:
    anagramma()
    user_choice = input('Do you want to play again? (yes/no)\n')
    if user_choice.lower() == 'no':
        break
print('Goodbye!')
