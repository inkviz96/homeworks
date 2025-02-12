


def quiz_game_start():
	questions = [
		{
			"question": "Какого цвета небо?",
			"options": ["Голубое", "Зеленый", "Красный"],
			"correct": 1,
		},
		{
			"question": "Как зовут нашего учителя?",
			"options": ["Евгений", "Семен", "Анатолий"],
			"correct": 2,
		},
		{
			"question": "Сколько будет 2 + 2(2 * 2)?",
			"options": ["4", "2", "10"],
			"correct": 3,
		},
		{
			"question": "Какое число Фибоначчи идет после 5?",
			"options": ["4", "16", "8"],
			"correct": 3,
		},
	]

	score = 0
	print("\nДобро пожаловать в Викторину от Room1!")
	print("Отвечайте на вопросы, выбирая правильный номер ответа.\n")

	for i, question in enumerate(questions, 1):
		print(f"Вопрос {i}: {question['question']}")

		for idx, option in enumerate(question["options"], 1):
			print(f"{idx}. {option}")

		while True:
			try:
				answer = int(input("Введите номер ответа: "))
				if 1 <= answer <= len(question["options"]):
					break
				else:
					print(f"Ошибка! Введите число от 1 до {len(question['options'])}.")
			except ValueError:
				print("Ошибка! Введите корректное число.")

		if answer == question["correct"]:
			print("Правильно!\n")
			score += 1
		else:
			correct_answer = question["options"][question["correct"] - 1]
			print(f"Неправильно! Правильный ответ: {correct_answer}\n")

	print(f"Викторина окончена! Вы набрали {score} из {len(questions)} очков.")


if __name__ == "__main__":
	quiz_game_start()