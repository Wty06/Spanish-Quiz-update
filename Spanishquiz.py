import random

print("Welcome to my Spanish quiz!")

playing = input("Would you like to play Tyler's Spanish Quiz? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Get Started!")
score = 0

# Explain how the game works
print("""
Welcome to the game! You will be asked a series of questions. Each question is worth points, 
so be sure to answer as best as you can! At the end of the game, your total score and percentage 
will be calculated. Good luck!
Note: Pay attention to special characters like the tilde (~) in Spanish words.
""")

# Define the questions as functions
def question_1():
    answer = input("Translate the word 'Casa' to its English counterpart: ")
    if answer.lower() == "house":
        print("Correcto!")
        return 1
    else:
        print("Incorrecto")
        return 0

def question_2():
    answer = input("How do you say 'Door' in Spanish? ")
    if answer.lower() == "puerta":
        print("Correcto!")
        return 1
    else:
        print("Incorrecto")
        return 0

def question_3():
    # Explain how the scoring for this question works
    print("""
    You can give up to 3 correct answers for how to naturally say 'how are you' in Spanish.
    Each correct answer is worth 1 point. If you provide less than 3 correct answers, or give an incorrect answer,
    you'll lose 1 point for each missing or incorrect one.
    Correct answers: 'Que tal', 'Cómo estás', and 'Cómo está usted'.
    """)
    
    answer = input("What is a natural way to say 'how are you' in Spanish? (You can provide up to 3 answers, separated by commas): ")
    
    # Define the correct answers
    correct_answers = ['que tal', 'cómo estás', 'cómo está usted']
    
    # Split the user's answer into individual responses
    user_answers = answer.lower().split(", ")
    
    # Initialize points for this question
    points = 3  # Start with 3 points
    
    # Check each answer the user gives and adjust points accordingly
    for ans in correct_answers:
        if ans not in user_answers:
            points -= 1  # Subtract 1 point for each missing or incorrect answer
    
    if points == 3:
        print("Correcto! You got all 3 correct.")
    else:
        print(f"Incorrecto! You lost {3 - points} points for missing or incorrect answers.")
    
    return points

def question_4():
    answer = input("Conjugate the verb 'ser' in the present tense (write all forms separated by commas): ")
    conjugations = ["soy", "eres", "es", "somos", "sois", "son"]
    user_answer = answer.lower().split(", ")
    points = 6  # Start with 6 points for this question
    for i, correct_answer in enumerate(conjugations):
        if i < len(user_answer) and user_answer[i] != correct_answer:
            points -= 1  # Subtract 1 point for each incorrect conjugation
    if points == 6:
        print("Correcto!")
    else:
        print(f"Incorrecto! You lost {6 - points} points for incorrect conjugations.")
    return points

def question_5():
    answer = input("What does the Spanish verb 'ir' translate to in English? ")
    if answer.lower() == "to go":
        print("Correcto!")
        return 1  # Update: 1 point for a correct answer
    else:
        print("Incorrecto")
        return 0

def question_6():
    answer = input('How do you say "I go" in Spanish? ')
    if answer.lower() == "yo voy":
        print("Correcto!")
        return 1
    else:
        print("Incorrecto")
        return 0

def question_7():
    answer = input("How do you say 'I go home' in Spanish? ")
    if answer.lower() == "yo voy a la casa":
        print("¡Wondísimo!")
        return 10
    else:
        print("Incorrecto")
        return 0

def question_8():
    answer = input("¿Cómo se dice 'máquina' en inglés? ")
    if answer.lower() == "machine":
        print("Correcto!")
        return 1
    else:
        print("Incorrecto")
        return 0

def question_9():
    answer = input("How do you say 'little' in Spanish? \n(Note: The second 'n' in 'Niña' has a tilde (ñ), making the sound like 'ny' in 'onion') ")
    if answer.lower() == "niña":
        print("Correcto!")
        return 10  # Update: 10 points for this question
    else:
        print("Incorrecto")
        return 0

def question_10():
    answer = input("What is the capital of Cuba? ")
    if answer.lower() == "havana":
        print("Correcto!")
        return 15  # Update: 15 points for this question
    else:
        print("Incorrecto")
        return 0

# Create a list of the questions
questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]

# Set of selected questions to avoid duplicates
selected_questions = set()

# Randomly choose numbers for the questions and ensure no duplicates
while len(selected_questions) < 7:  # Adjust the number of questions you want to ask
    question_num = random.randint(0, 9)
    if question_num not in selected_questions:
        selected_questions.add(question_num)
        score += questions[question_num]()  # Call the corresponding question function

# Calculate the total possible points
total_possible_points = 38  # Update based on new point allocation (1+1+3+6+1+1+10+1+10+15)

# Calculate the percentage score
percentage = (score / total_possible_points) * 100

# Display the score
print(f"Your score is: {percentage:.2f}%")
