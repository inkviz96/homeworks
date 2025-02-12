
def quiz_game_start():
	questions = [
		{
			"question": "Какого цвета небо?",
			"options": ["1. Голубое", "2. Зеленый", "3. Красный"],
			"correct": 1,
		},
		{
			"question": "Какая столица Франции?",
			"options": ["1. Берлин", "2. Париж", "3. Киев"],
			"correct": 2,
		},
		{
			"question": "Сколько будем 2+2(2*2)?",
			"options": ["1. 4", "2. 2", "3. 8"],
			"correct": 3,
		},
	]
	score = 0
	print("Добро пожаловать в Викторину от Room1!")
	print("Отвечайте на вопросы, выбирая правельный номер ответа.\n")
	for i, question in enumerate(questions, 1):
		print(f"Вопрос {i}: {question['question']}")
		for option in question["options"]:
			print(option)
		while True:
			try:
				answer = int(input("Введите номер ответа: "))
				if 1 <= answer <= len(question["options"]):
					break
				else:
					print(f"Введите число от 1 до {len(question["options"])}.")
			except ValueError:
				print("Введите число!")
		if answer == question["correct"]:
			print("Правильно!\n")
			score += 1
		else:
			print(f"Неправильно! Правильный ответ: {question["options"][question["correct"] - 1]})\n")
	print(f"Викторина окончена! Вы набрали {score} из {len(questions)} очков.")

quiz_game_start()













