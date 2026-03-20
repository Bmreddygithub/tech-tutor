# Test Case 2: Logic Error - Wrong Initialization

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import CodeDebuggingTutor

print("=" * 60)
print("TEST CASE 2: Logic Error - Wrong Initialization")
print("=" * 60)

buggy_code = """def find_max(numbers):
    max_value = 0
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

scores = [-5, -2, -8, -1]
print(f\"Maximum score: {find_max(scores)}\")"""

print("""
INPUT CODE:
-----------""")
print(buggy_code)

print("""
PROMPT SENT TO LLM:
-------------------
Be a friendly programming tutor helping a beginner student debug their code.
This code runs without an error but gives the wrong answer.
The function should return the maximum value from a list of negative numbers,
but it returns 0 instead of -1. Explain why the output is wrong and how to fix it.
""")

tutor = CodeDebuggingTutor()

print("-" * 60)
print("PROMPT 1 - Identify and explain the bug:")
print("-" * 60)
response1 = tutor.analyze_code(buggy_code)
print(response1)

print("-" * 60)
print("PROMPT 2 - Show the corrected code:")
print("-" * 60)
response2 = tutor.request_correction()
print(response2)

print("-" * 60)
print("PROMPT 3 - Are there Python built-ins that prevent this mistake?")
print("-" * 60)
response3 = tutor.ask_follow_up("Are there any Python built-in functions that could help me avoid this type of mistake?")
print(response3)

print("=" * 60)
