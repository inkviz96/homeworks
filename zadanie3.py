text = ("I just returned from the greatest summer vacation! It was so fantastic, I never wanted it to end.")
text = text.lower()
filtered_text = " "
for char in text:
    if char >= 'a' and char <= 'z':
        filtered_text += char
        letter_counts = {}
        for char in filtered_text:
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts [char] = 1
                most_common_letter = None
                max_frequency = 0
                for letter, frequency in letter_counts.items():
                    if frequency > max_frequency:
                        most_common_letter = letter
                        max_frequency = frequency
                        print(f"Наиболее частая буква встречаеться:{most_common_letter},")

                        
                
                


