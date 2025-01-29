text = "Baloon was red. But i like blue."
user_input = input("Введите строку для поиска: ")
index_case_sensitive = text.find(user_input)
index_case_insensitive = text.lower().find(user_input.lower())
print(f"Результат с учетом регистра: {index_case_sensitive}")
print(f"Результат без учета регистра: {index_case_insensitive}")

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
sum_length = len(str1) + len(str2)
print(f"Sum was {sum_length}")

text = "I just returned from the greatest summer vacation! It was so fantastic, I never wanted it to end."
text = text.lower()
text = ''.join([char for char in text if char.isalpha()])
max_letter = max(set(text), key=text.count)
print("Самая часто встречающаяся буква:", max_letter)

