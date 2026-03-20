# Test Case 5: Type Error - String + Integer Concatenation

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import CodeDebuggingTutor

print("=" * 60)
print("TEST CASE 5: Type Error - String + Integer Concatenation")
print("=" * 60)

buggy_code = """def create_message(age):
    message = \"You are \" + age + \" years old\"
    return message

user_age = 25
print(create_message(user_age))"""

error_msg = "TypeError: can only concatenate str (not 'int') to str"

print("""
INPUT CODE:
-----------""")
print(buggy_code)

print("""
PROMPT SENT TO LLM:
-------------------
Be a friendly programming tutor helping a beginner student debug their code.
The student's code crashes with: TypeError: can only concatenate str (not int) to str
Explain in simple words why this happens and show how to fix it.
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
print("PROMPT 3 - Which fix is most modern and recommended in Python 3?")
print("-" * 60)
response3 = tutor.ask_follow_up("Which fix is the most modern and recommended in Python 3?")
print(response3)

print("=" * 60)
