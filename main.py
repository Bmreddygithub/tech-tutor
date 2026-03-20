"""
Code Debugging Tutor - Main Application
An LLM-based educational tool using Groq API

AI Tasks Performed:
- Diagnosis + Classification  : Identifies and categorizes bug types (syntax, logic, runtime, type)
- Analysis + NL understanding : Comprehends code structure and programmer intent
- NL generation + Explanation : Produces beginner-friendly explanations and corrected code
- Question-answering*         : Responds to follow-up student questions with targeted answers
- Dialogue management         : Maintains conversation context across multiple prompt turns
- Knowledge representation    : Maps error patterns to general programming principles
"""

import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CodeDebuggingTutor:
    def __init__(self):
        """Initialize the debugging tutor with Groq client"""
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file")
        
        self.client = Groq(api_key=api_key)
        self.conversation_history = []
        self.model = "llama-3.3-70b-versatile"  # Fast and capable model
        
    def add_to_history(self, role, content):
        """Dialogue management: Appends a message to the conversation history."""
        self.conversation_history.append({
            "role": role,
            "content": content
        })
    
    def get_llm_response(self, user_message):
        """Core NL generation + Dialogue management: Sends prompt to LLM and returns response."""
        # Add user message to history
        self.add_to_history("user", user_message)
        
        # Get response from Groq
        chat_completion = self.client.chat.completions.create(
            messages=self.conversation_history,
            model=self.model,
            temperature=0.7,
            max_tokens=2000
        )
        
        # Extract assistant's response
        assistant_message = chat_completion.choices[0].message.content
        
        # Add assistant response to history
        self.add_to_history("assistant", assistant_message)
        
        return assistant_message
    
    def analyze_code(self, buggy_code, error_message=None):
        """AI Tasks: Diagnosis + Classification + Analysis + NL understanding
        Identifies, categorizes, and explains the bug in beginner-friendly terms."""
        prompt = f"""Be a friendly programming tutor helping a beginner student debug their code.

The student's code:
```python
{buggy_code}
```
"""
        if error_message:
            prompt += f"\nError message they received:\n{error_message}\n"
        
        prompt += """
Please:
1. Identify what's wrong with the code
2. Explain the error in beginner-friendly terms
3. Explain why this error happens
4. Give a brief hint about how to fix it (don't show the full solution yet)

Be encouraging and educational in your response."""
        
        return self.get_llm_response(prompt)
    
    def request_correction(self):
        """AI Tasks: NL generation + Explanation
        Generates corrected code and explains each fix in educational terms."""
        prompt = """Can you now show me the corrected version of the code? 
Please explain each important change you made and why it fixes the problem."""
        
        return self.get_llm_response(prompt)
    
    def ask_follow_up(self, question):
        """AI Tasks: Question-answering* + Dialogue management
        Answers student questions while maintaining full conversation context."""
        return self.get_llm_response(question)
    
    def reset_conversation(self):
        """Resets Dialogue management state — clears conversation history for a new session."""
        self.conversation_history = []
    
    def print_separator(self):
        """Print a visual separator"""
        print("\n" + "="*80 + "\n")


def demo_scenario_1():
    """Demo: Runtime Error - Division by Zero
    AI Tasks demonstrated: Diagnosis, Analysis, NL understanding, NL generation, Explanation, Dialogue management"""
    print("=" * 80)
    print("DEMO SCENARIO 1: Runtime Error - Division by Zero")
    print("=" * 80)
    
    tutor = CodeDebuggingTutor()
    
    buggy_code = """def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Test the function
grades = []
result = calculate_average(grades)
print(f"Average: {result}")"""
    
    error_msg = "ZeroDivisionError: division by zero"
    
    print("\nSTUDENT'S BUGGY CODE:")
    print(buggy_code)
    print(f"\nERROR: {error_msg}")
    
    # Prompt 1: Initial Analysis
    tutor.print_separator()
    print("PROMPT 1: Initial Code Analysis\n")
    response1 = tutor.analyze_code(buggy_code, error_msg)
    print(response1)
    
    # Prompt 2: Request Correction
    tutor.print_separator()
    print("PROMPT 2: Show Corrected Code\n")
    response2 = tutor.request_correction()
    print(response2)
    
    # Prompt 3: Follow-up Question
    tutor.print_separator()
    print("PROMPT 3: Follow-up Question\n")
    follow_up = "What other edge cases should I consider when working with lists in Python?"
    print(f"Student asks: {follow_up}\n")
    response3 = tutor.ask_follow_up(follow_up)
    print(response3)
    
    tutor.print_separator()
    print("Demo Scenario 1 Complete!\n")


def demo_scenario_2():
    """Demo: Logic Error - Wrong Initialization
    AI Tasks demonstrated: Diagnosis, Analysis, NL understanding, NL generation, Explanation, Question-answering*, Dialogue management"""
    print("\n" + "=" * 80)
    print("DEMO SCENARIO 2: Logic Error - Off-by-one")
    print("=" * 80)
    
    tutor = CodeDebuggingTutor()
    
    buggy_code = """def find_max(numbers):
    max_value = 0  # BUG: Assumes all numbers are positive
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Test
scores = [-5, -2, -8, -1]
print(f"Maximum score: {find_max(scores)}")  # Returns 0, should be -1"""
    
    print("\nSTUDENT'S BUGGY CODE:")
    print(buggy_code)
    
    # Prompt 1: Initial Analysis
    tutor.print_separator()
    print("PROMPT 1: Initial Code Analysis\n")
    response1 = tutor.analyze_code(buggy_code)
    print(response1)
    
    # Prompt 2: Request Correction
    tutor.print_separator()
    print("PROMPT 2: Show Corrected Code\n")
    response2 = tutor.request_correction()
    print(response2)
    
    # Prompt 3: Follow-up Question
    tutor.print_separator()
    print("PROMPT 3: Follow-up Question\n")
    follow_up = "Are there any Python built-in functions that could help me avoid this type of mistake?"
    print(f"Student asks: {follow_up}\n")
    response3 = tutor.ask_follow_up(follow_up)
    print(response3)
    
    tutor.print_separator()
    print("Demo Scenario 2 Complete!\n")


def demo_scenario_3():
    """Demo: Syntax Error - Missing Colon
    AI Tasks demonstrated: Diagnosis, Classification, NL understanding, NL generation, Explanation"""
    print("\n" + "=" * 80)
    print("DEMO SCENARIO 3: Syntax Error - Missing Colon")
    print("=" * 80)
    
    tutor = CodeDebuggingTutor()
    
    buggy_code = """def greet_user(name)
    if name
        print(f"Hello, {name}!")
    else:
        print("Hello, stranger!")

greet_user("Alice")"""
    
    error_msg = "SyntaxError: invalid syntax"
    
    print("\nSTUDENT'S BUGGY CODE:")
    print(buggy_code)
    print(f"\nERROR: {error_msg}")
    
    # Prompt 1: Initial Analysis
    tutor.print_separator()
    print("PROMPT 1: Initial Code Analysis\n")
    response1 = tutor.analyze_code(buggy_code, error_msg)
    print(response1)
    
    # Prompt 2: Request Correction
    tutor.print_separator()
    print("PROMPT 2: Show Corrected Code\n")
    response2 = tutor.request_correction()
    print(response2)
    
    tutor.print_separator()
    print("Demo Scenario 3 Complete!\n")


def demo_scenario_4():
    """Demo: Index Error - Out of Bounds
    AI Tasks demonstrated: Diagnosis, Analysis, NL understanding, NL generation, Explanation, Dialogue management"""
    print("\n" + "=" * 80)
    print("DEMO SCENARIO 4: Index Error - Out of Bounds")
    print("=" * 80)

    tutor = CodeDebuggingTutor()

    buggy_code = """def get_first_and_last(items):
    first = items[0]
    last = items[-1]
    return first, last

my_list = []
result = get_first_and_last(my_list)
print(result)"""

    error_msg = "IndexError: list index out of range"

    print("\nSTUDENT'S BUGGY CODE:")
    print(buggy_code)
    print(f"\nERROR: {error_msg}")

    # Prompt 1: Initial Analysis
    tutor.print_separator()
    print("PROMPT 1: Initial Code Analysis\n")
    response1 = tutor.analyze_code(buggy_code, error_msg)
    print(response1)

    # Prompt 2: Request Correction
    tutor.print_separator()
    print("PROMPT 2: Show Corrected Code\n")
    response2 = tutor.request_correction()
    print(response2)

    # Prompt 3: Follow-up Question
    tutor.print_separator()
    print("PROMPT 3: Follow-up Question\n")
    follow_up = "Also explain what negative indexing means in Python."
    print(f"Student asks: {follow_up}\n")
    response3 = tutor.ask_follow_up(follow_up)
    print(response3)

    tutor.print_separator()
    print("Demo Scenario 4 Complete!\n")


def demo_scenario_5():
    """Demo: Type Error - String + Integer Concatenation
    AI Tasks demonstrated: Diagnosis, Classification, NL understanding, NL generation, Explanation, Dialogue management"""
    print("\n" + "=" * 80)
    print("DEMO SCENARIO 5: Type Error - String + Integer Concatenation")
    print("=" * 80)

    tutor = CodeDebuggingTutor()

    buggy_code = """def create_message(age):
    message = "You are " + age + " years old"
    return message

user_age = 25
print(create_message(user_age))"""

    error_msg = "TypeError: can only concatenate str (not 'int') to str"

    print("\nSTUDENT'S BUGGY CODE:")
    print(buggy_code)
    print(f"\nERROR: {error_msg}")

    # Prompt 1: Initial Analysis
    tutor.print_separator()
    print("PROMPT 1: Initial Code Analysis\n")
    response1 = tutor.analyze_code(buggy_code, error_msg)
    print(response1)

    # Prompt 2: Request Correction
    tutor.print_separator()
    print("PROMPT 2: Show Corrected Code\n")
    response2 = tutor.request_correction()
    print(response2)

    # Prompt 3: Follow-up Question
    tutor.print_separator()
    print("PROMPT 3: Follow-up Question\n")
    follow_up = "Which fix is the most modern and recommended in Python 3?"
    print(f"Student asks: {follow_up}\n")
    response3 = tutor.ask_follow_up(follow_up)
    print(response3)

    tutor.print_separator()
    print("Demo Scenario 5 Complete!\n")


def interactive_mode():
    """Interactive mode — full AI task pipeline:
    Diagnosis + Classification → Analysis + NL understanding → NL generation + Explanation → Question-answering* + Dialogue management
    """
    print("\n" + "=" * 80)
    print("INTERACTIVE MODE - Code Debugging Tutor")
    print("=" * 80)
    print("\nPaste your buggy code below (type 'END' on a new line when done):")
    
    lines = []
    while True:
        line = input()
        if line.strip() == 'END':
            break
        lines.append(line)
    
    buggy_code = '\n'.join(lines)
    
    error_msg = input("\nError message (optional, press Enter to skip): ").strip()
    error_msg = error_msg if error_msg else None
    
    tutor = CodeDebuggingTutor()
    
    # Initial analysis
    print("\nAnalyzing your code...\n")
    response = tutor.analyze_code(buggy_code, error_msg)
    print(response)
    
    # Conversation loop
    while True:
        print("\n" + "-" * 80)
        user_input = input("\nYour follow-up question (or 'quit' to exit): ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("\nHappy coding!")
            break
        
        if user_input:
            response = tutor.ask_follow_up(user_input)
            print(f"\n{response}")


def main():
    """Main function to run demos or interactive mode"""
    print("\n" + "=" * 80)
    print(" CODE DEBUGGING TUTOR - Assignment 4 Demo".center(80))
    print(" Powered by Groq (Llama 3.1)".center(80))
    print("=" * 80)
    
    while True:
        print("\nChoose an option:")
        print("1. Run Demo Scenario 1 (Runtime Error - Division by Zero)")
        print("2. Run Demo Scenario 2 (Logic Error - Wrong Initialization)")
        print("3. Run Demo Scenario 3 (Syntax Error - Missing Colon)")
        print("4. Run Demo Scenario 4 (Index Error - Out of Bounds)")
        print("5. Run Demo Scenario 5 (Type Error - String + Integer)")
        print("6. Run All 5 Test Cases")
        print("7. Interactive Mode (paste your own code)")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == '1':
            demo_scenario_1()
        elif choice == '2':
            demo_scenario_2()
        elif choice == '3':
            demo_scenario_3()
        elif choice == '4':
            demo_scenario_4()
        elif choice == '5':
            demo_scenario_5()
        elif choice == '6':
            demo_scenario_1()
            demo_scenario_2()
            demo_scenario_3()
            demo_scenario_4()
            demo_scenario_5()
        elif choice == '7':
            interactive_mode()
        elif choice == '8':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
