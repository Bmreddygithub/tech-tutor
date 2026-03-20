# Test Case 6: Off-by-one Error in Loop

print("=" * 60)
print("TEST CASE 6: Off-by-one Error - Loop Range")
print("=" * 60)

print("""
MANUAL LLM EVALUATION
---------------------
Prompt used:
  'Be a friendly programming tutor. This code is supposed to print
   numbers 1 to 5 but instead prints 0 to 4. Explain why and show the fix.'

How well the LLM worked:
  - Correctly identified that range(n) starts at 0 by default
  - Explained clearly: 'Python counts from 0, so range(5) gives 0,1,2,3,4
    not 1,2,3,4,5. You need to tell it to start at 1.'
  - Provided the correct fix: range(1, n+1)
  - Also mentioned range(1, 6) as an alternative for fixed numbers

Prompt change tested:
  Added: 'Also explain how range() works in general'
  With modification: LLM gave a fuller explanation of range(start, stop, step)
  which is more educational and helps students avoid similar bugs in future

Self-consistency check (ran 3 times at temp=0.7):
  Run 1: fix was range(1, n+1) - correct
  Run 2: fix was range(1, n+1) - correct, also mentioned enumerate()
  Run 3: fix was range(1, n+1) - correct
  All 3 runs consistent. Off-by-one in range() is a well-known pattern.
""")

print("-" * 60)
print("BUGGY CODE OUTPUT (prints 0 to 4 instead of 1 to 5):")
print("-" * 60)

def print_numbers_buggy(n):
    for i in range(n):  # Bug: starts at 0, not 1
        print(i, end=" ")
    print()

print("Buggy output:  ", end="")
print_numbers_buggy(5)
print("Expected:       1 2 3 4 5")

print("-" * 60)
print("FIXED CODE OUTPUT:")
print("-" * 60)

def print_numbers_fixed(n):
    for i in range(1, n + 1):  # Fixed: starts at 1
        print(i, end=" ")
    print()

print("Fixed output:  ", end="")
print_numbers_fixed(5)

print("=" * 60)
