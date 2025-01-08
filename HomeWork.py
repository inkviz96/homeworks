
name = input("Nikolai: ")
surname = input("Markelov: ")
print(f"Hello, {name} {surname}!")
text = "Baloon was red. But I like blue."
search = input("search: ")
print(f"Case sensitive: {text.find(search)}")
print(f"Case insensitive: {text.lower().find(search.lower())}")
str1 = input("First line: ")
str2 = input("Second line: ")
print(f"Sum of string lengths: {len(str1) + len(str2)}")
text = "I just returned from the greatest summer vacation! It was so fantastic, I never wanted it to end."
cleaned_text = text.replace(" ", "").lower()
most_common = max(cleaned_text, key=cleaned_text.count)
print(f"Most common letter: '{most_common}', meets {cleaned_text.count(most_common)} times.")

