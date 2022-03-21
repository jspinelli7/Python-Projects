question_file = open('questions.txt', 'r')
question_answer = [line.strip() for line in question_file.readlines()]
question_file.close()

x = 1
n = 0
m = len(question_answer)

for question in question_answer:
    equation = question.split('=')[0] + "="
    correct_answer = question.split('=')[1]
    print(f'Question {x}: {equation}')
    user_input = int(input("Please enter your answer: "))
    if user_input == int(correct_answer):
        n += 1
    x += 1

final_result = f'Your final score is {n}/{m}'

result_file = open('result.txt', 'w')
result_file.write(final_result)
result_file.close()




"""
def user_input(n):
    if n >= 0 && n == correct_answer:
        print(f'Correct! The answer was {correct_answer}.')
    elif n >= 0 && n != correct_answer:
        print(f'Incorrect! Please enter another integer: ')

    else:
        raise ValueError('Please enter a positive integer.')
"""
