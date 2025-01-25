from platform import version

print("Hello\nWorld")
print("This is a backslash:\\")
print("He said,Hello!\"")
print('It\'s a sunny day')
print(f"Python \nProgramming")
print("She said,'Hi!'")
print("Path to file: c :\\\\")



course = "Python"
level = "beginner"
#result = "This is a {} course for {} learners.".format(course, level)
print('"This is a {} course for {} learners."'.format(course, level))

course = "Python"
level = "beginner"
result = f'"This is a {course} course for {level} learners."'
print(result)

topic = "Machine Learning"
print(f'"Welcome to the {topic} workshop."')

topic = "Machine Learning"
print(f'"Welcome to the {topic} workshop."')

topic ="machine learning"
course_str = f'"Course: {topic.title()}"'
print(course_str)

str1 = "Data"
str2 = "Science"
print(f'"Field: {(str1 + " " + str2) * 3}"')

str = "Information"
print(f'"Third character: {str[2]}"')

str1 ="Neural Networks"
print(f'"Length: {len(str1)*2}" ')

str1 = "Deep Learning"
upper_str = str1.upper()
index = upper_str.find("LEARNING")
print(f'" {upper_str[index]}"')

str1 = "Starta"
length = len(str1)
result = f'"{str1} has length of {length}"'
print(result)















