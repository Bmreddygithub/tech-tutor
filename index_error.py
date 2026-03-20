# Test Case 4: Index Error - Out of Bounds

import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import CodeDebuggingTutor

print("=" * 60)
print("TEST CASE 4: Index Error - Out of Bounds")
print("=" * 60)

buggy_code = """def get_first_and_last(items):
    first = items[0]
    last = items[-1]
    return first, last

my_list = []
result = get_first_and_last(my_list)
print(result)"""

error_msg = "IndexError: list index out of range"

print("""
INPUT CODE:
-----------""")
print(buggy_code)

print("""
PROMPT SENT TO LLM:
-------------------
Be a friendly programming tutor helping a beginner student debug their code.
The student's code crashes with: IndexError: list index out of range
The list passed in is empty. Explain what went wrong and how to fix it.
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
print("PROMPT 3 - What does negative indexing mean in Python?")
print("-" * 60)
response3 = tutor.ask_follow_up("Also explain what negative indexing means in Python.")
print(response3)

print("=" * 60)
