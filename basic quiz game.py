print('Welcome to world war 1 quiz')
answer = input('Are you ready to play the Quiz ? (yes/no):\n ')
score = 0
total_questions = 3

if answer.lower() == 'yes':
    answer = int(input('Question 1: What year did world war 1 start?\n'))
    if answer == 1914:
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer = input('Question 2: what was the immidiate cause of the world war 1?\n')
    if answer.lower() == 'assasination of franz ferdinand':
        score += 1
        print('correct')
    elif answer.lower() == 'assasination':
        score += 1
        print('correct')
    elif answer.lower() == 'franz':
        score += 1
        print('correct')
    elif answer.lower() == 'ferdinand':
        score += 1
        print('correct')
    else:
        print('Wrong Answer answer :(')

    answer = input('Question 3: is latvia an east or west europe country?\n')
    if answer.lower() == 'east':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Thankyou for Playing this small quiz game, you attempted', score, "questions correctly!")
mark = (score / total_questions) * 100
print('Marks obtained:', mark,'%')
print('BYE!')
