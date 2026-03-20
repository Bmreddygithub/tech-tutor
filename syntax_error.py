# Test Case 3: Syntax Error - Missing Colons

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import CodeDebuggingTutor

print("=" * 60)
print("TEST CASE 3: Syntax Error - Missing Colons")
print("=" * 60)

buggy_code = """def greet_user(name)
    if name
        print(f\"Hello, {name}!\")
    else:
        print(\"Hello, stranger!\")

greet_user(\"Alice\")"""

error_msg = "SyntaxError: invalid syntax"

print("""
INPUT CODE:
-----------""")
print(buggy_code)

print("""
PROMPT SENT TO LLM:
-------------------
Be a friendly programming tutor helping a beginner student debug their code.
The student's code gives: SyntaxError: invalid syntax
Identify all the syntax mistakes in this code and explain each one simply.
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
print("PROMPT 3 - What are all the places in Python that require a colon?")
print("-" * 60)
response3 = tutor.ask_follow_up("What are all the places in Python where I need to put a colon at the end of a line?")
print(response3)

print("=" * 60)

