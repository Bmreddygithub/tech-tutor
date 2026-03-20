# Test Case 7: Variable Scope Error

print("=" * 60)
print("TEST CASE 7: Variable Scope Error")
print("=" * 60)

print("""
MANUAL LLM EVALUATION
---------------------
Prompt used:
  'Be a friendly programming tutor. The student gets:
   UnboundLocalError: local variable special_discount referenced before assignment
   when calling calculate_discount(50). Explain what scope means and how to fix it.'

How well the LLM worked:
  - Correctly identified that special_discount is only created inside the if block
  - When price=50, the if block is skipped, so special_discount never gets created
  - Explained clearly: 'The variable only exists inside the if block. If you skip
    that block, the variable does not exist yet when you try to use it.'
  - Fix: initialize special_discount = 0.0 before the if block

Prompt change tested (self-consistency across 3 runs):
  Run 1 (temp=0.7): Identified scope issue, suggested initializing before if
  Run 2 (temp=0.7): Same fix, also suggested moving the print inside the if block
  Run 3 (temp=0.7): Same fix + explained Python scoping vs Java/C block scope
  All 3 correct. Run 3 gave the most educational answer.

Temperature test:
  At 0.3: Only gave the initialization fix, no alternatives
  At 0.7: Gave fix + alternative design + general scoping explanation
  Conclusion: For scope errors, 0.7 significantly outperforms 0.3 in teaching value
""")

print("-" * 60)
print("BUGGY CODE OUTPUT (price=50, skips if block):")
print("-" * 60)

def calculate_discount_buggy(price):
    discount_rate = 0.1
    if price > 100:
        special_discount = 0.2
        final_price = price * (1 - special_discount)
    else:
        final_price = price * (1 - discount_rate)
    print(f"Discount applied: {special_discount}")  # Bug: not defined when price <= 100
    return final_price

try:
    calculate_discount_buggy(50)
except UnboundLocalError as e:
    print(f"ERROR caught: UnboundLocalError: {e}")
    print("This is the expected bug - special_discount was never created because price=50 skipped the if block.")

print("-" * 60)
print("FIXED CODE OUTPUT:")
print("-" * 60)

def calculate_discount_fixed(price):
    discount_rate = 0.1
    special_discount = 0.0  # Fixed: initialized before the if block
    if price > 100:
        special_discount = 0.2
        final_price = price * (1 - special_discount)
    else:
        final_price = price * (1 - discount_rate)
    print(f"Discount applied: {special_discount}")
    return final_price

calculate_discount_fixed(50)
calculate_discount_fixed(150)

print("=" * 60)
