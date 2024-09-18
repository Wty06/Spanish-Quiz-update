# Spanish Quiz Game

## Description

The updated version of the Spanish quiz game introduces significant improvements over the original linear design. In the new version, questions are selected randomly using `random.randint()`, ensuring each playthrough is unique. A more complex scoring system has been implemented, which includes point deductions for incorrect answers and nuanced scoring for multi-part questions such as conjugating the verb "ser" and identifying natural ways to say "how are you" in Spanish. The game's code is modularized, with functions created for each question, making the structure more efficient and reusable. Additionally, player scores are calculated dynamically based on the assigned point values for each question, leading to a more flexible and accurate scoring system.

## Features

### 1. **Randomized Questions**
- Questions are selected randomly from a pool, ensuring no two playthroughs are the same. This is achieved through `random.randint()`, which picks questions in a non-repetitive way.

### 2. **Modularized Code**
- Each question is encapsulated in its own function. This modular structure makes the code easy to maintain and extend. Functions allow for reusability and better organization.

### 3. **Scoring System**
- The game implements a dynamic scoring system:
  - Points are awarded for correct answers.
  - Deductions are made for incorrect or incomplete responses, especially for multi-part questions.
  - A total score is calculated at the end based on the player's performance.

### 4. **Multi-Part Question Complexity**
- Some questions involve more than one answer (e.g., conjugating verbs or providing multiple phrases). These questions are scored based on the number of correct answers, with deductions for wrong or missing responses.

### 5. **Detailed Feedback**
- Players receive immediate feedback after answering each question, letting them know whether their response was correct or incorrect.
- For complex questions, feedback includes the number of correct answers and how many points were lost due to mistakes.

## Example Code Snippets

Here are some examples of the code that power the game:

### Randomized Question Selection

```python
questions = [question_1, question_2, question_3, question_4, question_5, question_6, question_7, question_8, question_9, question_10]

selected_questions = set()
while len(selected_questions) < 7:
    question_num = random.randint(0, 9)
    if question_num not in selected_questions:
        selected_questions.add(question_num)
        score += questions[question_num]()  # Call the corresponding question function
```

### Multi-Part Question Example

```python
def question_3():
    print("""
    You can provide up to 3 correct answers for how to naturally say 'how are you' in Spanish.
    Each correct answer is worth 1 point. If you provide fewer than 3 correct answers or give an incorrect answer,
    you'll lose 1 point for each missing or incorrect one.
    """)
    answer = input("What is a natural way to say 'how are you' in Spanish? (You can provide up to 3 answers, separated by commas): ")
    correct_answers = ['que tal', 'cómo estás', 'cómo está usted']
    user_answers = answer.lower().split(", ")
    points = 3  # Start with 3 points
    for ans in correct_answers:
        if ans not in user_answers:
            points -= 1  # Subtract 1 point for incorrect/missing answers
    if points == 3:
        print("Correcto!")
    elif points > 0:
        print(f"You got {points} correct answers.")
    else:
        print("Incorrecto! You got all answers wrong.")
    return points
```

### Score Calculation

```python
total_possible_points = 38
percentage = (score / total_possible_points) * 100
print(f"Your score is: {percentage:.2f}%")
```

## Installation and Usage

1. Clone the repository to your local machine.
2. Run the game using Python.
3. Answer the randomly selected questions to the best of your ability.
4. At the end of the game, your score will be displayed as a percentage.

## Summary

This game provides a fun and interactive way to test your Spanish knowledge, with dynamic scoring, randomization, and detailed feedback. The modular code design ensures easy maintenance and scalability for future updates.
