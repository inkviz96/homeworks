text1 = "Balkon was red"
text2 = "But I like blue"

print(text1+text2)
text = "Balkon was red But I like blue"
user_input = input("Введите строку для поиска: ")
find_case_insensitive = text.lower().find(user_input.lower())

find_case_sensitive = text.find(user_input)
if find_case_insensitive != -1:
    print(f"Строка найдена без учета регисира на позиции:{find_case_insensitive}")
else:
    print("Строка не найдена без учета регистра.")










ы
