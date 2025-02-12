import random
import tkinter as tk
from tkinter import messagebox

# --- Глобальные переменные ---
words = [
        'виселица', 'европа', 'азия', 'тигр', 'жираф', 
         'Валентина', 'Николай', 'Бийбарс', 'Айтишник',
         'Питон', 'Пайчарм', 'Джанго', 'Веб' 
 ]
vowels = "аеёиоуыэюя"
secret_word = random.choice(words).lower()
guessed_word = ["_" if ch not in vowels else ch for ch in secret_word]
attempts = 6

# --- Функция рисования виселицы ---
def draw_hangman(stage):
    canvas.delete("all")  # Очистка холста
    canvas.create_rectangle(0, 0, 300, 300, fill="#ffeadb", outline="")  # Фон
    
    if stage >= 0:
        canvas.create_line(50, 250, 150, 250, width=4, fill="brown")  # Основание
        canvas.create_line(100, 250, 100, 50, width=4, fill="brown")   # Столб
        canvas.create_line(100, 50, 200, 50, width=4, fill="brown")    # Верхняя перекладина
        canvas.create_line(200, 50, 200, 80, width=4, fill="brown")    # Веревка
    if stage >= 1:
        canvas.create_oval(180, 80, 220, 120, width=3, outline="black", fill="lightgray")  # Голова
    if stage >= 2:
        canvas.create_line(200, 120, 200, 180, width=3, fill="black")  # Туловище
    if stage >= 3:
        canvas.create_line(200, 130, 170, 160, width=3, fill="black")  # Левая рука
    if stage >= 4:
        canvas.create_line(200, 130, 230, 160, width=3, fill="black")  # Правая рука
    if stage >= 5:
        canvas.create_line(200, 180, 170, 230, width=3, fill="black")  # Левая нога
    if stage >= 6:
        canvas.create_line(200, 180, 230, 230, width=3, fill="black")  # Правая нога

# --- Функция проверки буквы ---
def check_letter():
    global attempts, guessed_word

    letter = entry.get().lower()
    entry.delete(0, tk.END)  # Очистка поля ввода

    if len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning("Ошибка", "Введите одну букву!")
        return

    if letter in secret_word:
        for index, char in enumerate(secret_word):
            if char == letter:
                guessed_word[index] = letter
    else:
        attempts -= 1

    word_label.config(text=" ".join(guessed_word))
    status_label.config(text=f"Осталось попыток: {attempts}", fg="red" if attempts <= 2 else "black")
    draw_hangman(6 - attempts)  # Обновляем рисунок виселицы

    # Проверка победы/поражения
    if "_" not in guessed_word:
        messagebox.showinfo("Победа!", f"Вы угадали слово: {secret_word}")
        reset_game()
    elif attempts == 0:
        messagebox.showerror("Проигрыш", f"Вы проиграли! Слово было: {secret_word}")
        reset_game()

# --- Функция перезапуска игры ---
def reset_game():
    global secret_word, guessed_word, attempts
    secret_word = random.choice(words).lower()
    guessed_word = ["_" if ch not in vowels else ch for ch in secret_word]
    attempts = 6

    word_label.config(text=" ".join(guessed_word))
    status_label.config(text=f"Осталось попыток: {attempts}", fg="black")
    draw_hangman(0)

# --- Создание окна ---
root = tk.Tk()
root.title("Виселица")
root.geometry("400x500")
root.configure(bg="#f8f8ff")

# --- Полотно для рисования ---
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=10)

# --- Метка слова ---
word_label = tk.Label(root, text=" ".join(guessed_word), font=("Arial", 22, "bold"), bg="#f8f8ff")
word_label.pack(pady=10)

# --- Поле ввода ---
entry = tk.Entry(root, font=("Arial", 16))
entry.pack(pady=5)

# --- Кнопка проверки буквы ---
guess_button = tk.Button(root, text="Проверить букву", command=check_letter, font=("Arial", 14), bg="blue", fg="white")
guess_button.pack(pady=5)

# --- Статус игры ---
status_label = tk.Label(root, text=f"Осталось попыток: {attempts}", font=("Arial", 16), bg="#f8f8ff")
status_label.pack(pady=5)

# --- Запуск начальной виселицы ---
draw_hangman(0)

root.mainloop()
