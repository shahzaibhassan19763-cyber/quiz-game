import random
import pandas as pd
from datetime import datetime

print("=== Welcome to Dynamic Math Quiz Game ===")
username = input("Apna naam enter karein: ")

score = 0
total_questions = 7
operations = ['+', '-', '*', '/', '**']

for i in range(1, total_questions + 1):
    # Randomly operation choose karna (addition, subtraction, multiplication, division, power)
    op = random.choice(operations)
    
    # Operations ke hissab se numbers generate karna
    if op == '+':
        a, b = random.randint(1, 100), random.randint(1, 100)
        correct_ans = a + b
        question_str = f"{a} + {b}"
        
    elif op == '-':
        a, b = random.randint(1, 100), random.randint(1, 100)
        if a < b: # Negative values se bachne ke liye
            a, b = b, a
        correct_ans = a - b
        question_str = f"{a} - {b}"
        
    elif op == '*':
        a, b = random.randint(1, 12), random.randint(1, 12)
        correct_ans = a * b
        question_str = f"{a} * {b}"
        
    elif op == '/':
        b = random.randint(1, 10)
        correct_ans = random.randint(1, 10)
        a = b * correct_ans  # Point mein answer se bachne ke liye clean division
        question_str = f"{a} / {b}"
        
    elif op == '**':
        a = random.randint(2, 5)
        b = random.randint(2, 3)  # Power choti rakhi hai taake values bohat bari na hon
        correct_ans = a ** b
        question_str = f"{a} ki power {b} ({a}^{b})"

    # User se sawal pochna
    print(f"\nSawal {i}: {question_str} kitna hoga?")
    try:
        user_ans = float(input("Aapka jawab: "))
        
        if user_ans == correct_ans:
            print("Sahi jawab! 🎯 +1 point")
            score += 1
        else:
            print(f"Ghalat jawab! Sahi jawab {correct_ans} tha.")
            
    except ValueError:
        print("Ghalat input! Aapne number nahi likha, yeh sawal skip ho gaya.")

print(f"\nGame Khatam! {username}, aapka total score: {score} / {total_questions}")

# Score ko Pandas ke zariye Excel sheet mein save karna
data = {
    "Name": [username],
    "Score": [score],
    "Total Questions": [total_questions],
    "Date & Time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
}

df = pd.DataFrame(data)

try:
    # Agar purani file mojood hai toh naya record sath attach (append) kar dega
    existing_df = pd.read_excel("math_quiz_scores.xlsx")
    updated_df = pd.concat([existing_df, df], ignore_index=True)
    updated_df.to_excel("math_quiz_scores.xlsx", index=False)
except FileNotFoundError:
    # Agar file nahi hai toh nayi ban jaye gi
    df.to_excel("math_quiz_scores.xlsx", index=False)

print("Aapka score successfully 'math_quiz_scores.xlsx' sheet mein save ho gaya hai!")