#Maths quiz. This asks the user to choose a level of math difficulty.
#Easy and medium just use the addition operator, hard, uses a random operator.
#The user can also submit the number of questions to be asked.
import operator
import random

def random_numbers(level, *args):
    if level == "easy":
        return random.sample(range(1, 50), 10)
    if level == "medium":
        return random.sample(range(100, 200), 20)
    if level == "hard":
        return random.sample(range(500, 1500), 30)

ops = {'+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv}


level_choice = input("Please enter level from:" + " hard" + "/" + " medium" + "/" + " easy ")
number_of_questions = int(input("How many questions would you like to answer"))
count = 0

for x in range(number_of_questions):
 while count < number_of_questions:
     num1 = random.choice(random_numbers(level_choice))
     num2 = random.choice(random_numbers(level_choice))
     answer = num1 + num2
     if level_choice != "hard":
         question = input(("What is " + str(num1) + " + " + str(num2) + " = "))
         if int(question) == answer:
            print("Correct")
         else:
            print("wrong")
     elif level_choice == "hard":
         op = random.choice(list(ops.keys()))
         answer = ops.get(op)(num1,num2)
         question = input(f'What is {num1} {op} {num2}?\n')
         if int(question) == answer:
            print("Correct")
         else:
            print("wrong")
     count += 1

     












 
