# Test Case 1: Runtime Error - Division by Zero

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import CodeDebuggingTutor

print("=" * 60)
print("TEST CASE 1: Runtime Error - Division by Zero")
print("=" * 60)

buggy_code = """def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

grades = []
result = calculate_average(grades)
print(f\"Average: {result}\")"""

error_msg = "ZeroDivisionError: division by zero"

print("""
INPUT CODE:
-----------""")
print(buggy_code)

print("""
PROMPT SENT TO LLM:
-------------------
Be a friendly programming tutor helping a beginner student debug their code.
The student's code crashes with: ZeroDivisionError: division by zero
Identify the bug, explain it in simple words, and give a hint to fix it.
""")

tutor = CodeDebuggingTutor()

print("-" * 60)
print("PROMPT 1 - Identify and explain the bug:")
print("-" * 60)
response1 = tutor.analyze_code(buggy_code, error_msg)
print(response1)

print("-" * 60)
print("PROMPT 2 - Show the corrected code:")
print("-" * 60)
response2 = tutor.request_correction()
print(response2)

print("-" * 60)
print("PROMPT 3 - What other edge cases should I handle with lists?")
print("-" * 60)
response3 = tutor.ask_follow_up("What other edge cases should I handle when working with lists in Python?")
print(response3)

print("=" * 60)
