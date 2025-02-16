import random

questions = [
    {'question': 'Столица Франции?', 'options': ['Париж', 'Лондон', 'Берлин', 'Мадрид'], 'answer': 'Париж'},
    {'question': 'Сколько будет 5 + 7?', 'options': ['10', '11', '12', '13'], 'answer': '12'},
    {'question': 'Как называется процесс фотосинтеза?', 'options': ['Процесс получения энергии из света', 'Процесс дыхания', 'Процесс поглощения воды', 'Процесс испарения'], 'answer': 'Процесс получения энергии из света'},
    {'question': 'Какая планета самая большая в Солнечной системе?', 'options': ['Земля', 'Марс', 'Юпитер', 'Сатурн'], 'answer': 'Юпитер'},
    {'question': 'С помощью какого метода мы можем перевернуть наш текст?', 'options': ['sum()', 'txt[::-1]', 'replace()', 'lambda'], 'answer': 'txt[::-1]'},
    {'question': 'Что обозначает H2O?', 'options': ['Вода', 'Кислород', 'Углекислый газ', 'Соль'], 'answer': 'Вода'},
    {'question': 'Столица Японии?', 'options': ['Токио', 'Киото', 'Осака', 'Нагойя'], 'answer': 'Токио'},
    {'question': 'Скорость света в вакууме?', 'options': ['299 792 км/с', '150 000 км/с', '1 080 км/ч', '300 000 км/ч'], 'answer': '299 792 км/с'},
    {'question': 'Кто написал роман "1984"?', 'options': ['Джордж Оруэлл', 'Олдос Хаксли', 'Рэй Брэдбери', 'Дж. Р. Р. Толкин'], 'answer': 'Джордж Оруэлл'},
    {'question': 'Какая столица России?', 'options': ['Москва', 'Санкт-Петербург', 'Новосибирск', 'Екатеринбург'], 'answer': 'Москва'}
]

def quizz_start():
    print('Добро пожаловать в викторину!')
    print('Ответьте на следующие вопросы: ')
    score = 0
    
    random.shuffle(questions)
    
    for question in questions[:10]:  
        print(question['question'])
        for i, option in enumerate(question['options']):
            print(f"{i + 1}. {option}")
        user_answer = input('Введите ваш ответ: ')
        
        if user_answer.lower() == question['answer'].lower():
            print('Верно!')
            score += 1
        else:
            print(f'Неверно! Правильный ответ: {question["answer"]}')
        print()
    
    print(f'Ваш итоговый счёт: {score} из 10')

if __name__ == "__main__":
    quizz_start()
