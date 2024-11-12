# 1) questions 
# 2) choices
# 3) correct answer

import json

with open("questions.json", 'r') as file :
    content = file.read()

data = json.loads(content)

for index, question in enumerate(data) :
    print(f"Q{index+1}) {question["questions"]}")
    for index, choice in enumerate(question["choices"]) :
        print(f"{index + 1}.{choice}")
    user_input = int(input("Enter your answer: "))
    question["user_choice"] = user_input


score = 0
    
for index, question in enumerate(data) :
     
    if question["user_choice"] == question["correct_ans"]:
        result = "Correct Answer"
        score += 1
    else:
        result = "Wrong Answer"

    print(f"{index + 1}. {result}. Your answer: {question['user_choice']}, Correct answer: {question['correct_ans']}")

print(f"your score is {score}/{len(data)}")
   