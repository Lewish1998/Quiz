import json

with open ('data.json', 'r') as file:
    file = json.load(file)

question_list = []
answer_list = []

for q in file['results']:
    question = q['question']
    question_list.append(question)

for q in file['results']:
    answer = q['correct_answer']
    answer_list.append(answer)

# lists for all 10 questions and answers