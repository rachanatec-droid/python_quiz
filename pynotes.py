import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Python Core Concepts & Quiz App",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# App Title & Description
st.title("🐍 Python Core Concepts & Interactive Quiz App")
st.markdown(
    """
Welcome to your ultimate Python cheat sheet and quiz companion. 
Select a module from the sidebar to review short, high-yield notes and test your knowledge!
"""
)

# Define data structure for notes and quizzes
modules = {
    "1. Variables & Data Types": {
        "notes": """
        ### Core Concepts: Variables & Data Types
        *   **Variables**: Containers for storing data values. Python is dynamically typed, meaning you don't need to declare the type explicitly.
        *   **Integers (`int`)**: Whole numbers, e.g., `x = 5`.
        *   **Floats (`float`)**: Decimal numbers, e.g., `y = 5.5`.
        *   **Strings (`str`)**: Text wrapped in quotes, e.g., `name = "Python"`.
        *   **Booleans (`bool`)**: True or False values, e.g., `is_active = True`.
        
        ```python
        # Quick Example
        age = 25          # int
        price = 19.99     # float
        course = "Python" # str
        is_passed = True  # bool

        # Type conversion (Casting)
        str_age = str(age) # converts 25 to "25"
        ```
        """,
        "quiz": {
            "question": "What is the output of `type(3.14)` in Python?",
            "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'double'>"],
            "answer": "<class 'float'>",
            "explanation": "In Python, decimal numbers are automatically treated as floating-point numbers (`float`)."
        }
    },
    "2. Control Flow & Loops": {
        "notes": """
        ### Core Concepts: Control Flow & Loops
        *   **Conditional Statements**: Use `if`, `elif`, and `else` to execute code based on conditions.
        *   **For Loops**: Used for iterating over a sequence (list, tuple, dictionary, set, or string).
        *   **While Loops**: Executes a set of statements as long as a condition is true.
        *   **Break & Continue**: `break` stops the loop entirely. `continue` skips the current iteration and moves to the next.

        ```python
        # Check condition
        score = 85
        if score >= 90:
            print("A")
        elif score >= 80:
            print("B")
        else:
            print("C")

        # Loop through a range
        for i in range(3):
            print(f"Iteration {i}")
        ```
        """,
        "quiz": {
            "question": "Which keyword is used to skip the rest of the current loop iteration and move to the next one?",
            "options": ["break", "skip", "continue", "pass"],
            "answer": "continue",
            "explanation": "The `continue` statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop."
        }
    },
    "3. Data Structures (Lists, Tuples, Dicts, Sets)": {
        "notes": """
        ### Core Concepts: Built-in Data Structures
        *   **Lists `[]`**: Ordered, mutable, allows duplicate members.
        *   **Tuples `()`**: Ordered, **immutable** (cannot be changed), allows duplicate members.
        *   **Dictionaries `{}`**: Unordered (ordered since 3.7), mutable, **key-value pairs**, no duplicate keys.
        *   **Sets `{}`**: Unordered, unindexed, **no duplicate members**.

        ```python
        my_list = [1, 2, 2, 3]       # Mutable
        my_tuple = (1, 2, 2, 3)     # Immutable
        my_set = {1, 2, 3}          # Unique values only
        my_dict = {"name": "Alice", "age": 22} # Key-Value
        ```
        """,
        "quiz": {
            "question": "Which of the following data structures is immutable?",
            "options": ["List", "Dictionary", "Tuple", "Set"],
            "answer": "Tuple",
            "explanation": "Tuples cannot be changed, modified, or appended after they are created, making them immutable."
        }
    },
    "4. Functions & Lambda": {
        "notes": """
        ### Core Concepts: Functions & Lambda Expressions
        *   **Functions**: A block of code that only runs when it is called. Defined using the `def` keyword.
        *   **Arguments**: Information passed into functions. Can have default values.
        *   **Return Value**: Use the `return` statement to send a value back to the caller.
        *   **Lambda Functions**: Small, anonymous (nameless) functions defined with the `lambda` keyword. Can take any number of arguments but only have one expression.

        ```python
        # Standard function
        def greet(name="User"):
            return f"Hello, {name}!"

        # Lambda function
        square = lambda x: x ** 2
        print(square(4)) # Outputs 16
        ```
        """,
        "quiz": {
            "question": "How do you define an anonymous function in Python?",
            "options": ["def", "anonymous", "inline", "lambda"],
            "answer": "lambda",
            "explanation": "The `lambda` keyword is used to create small, one-line anonymous functions in Python."
        }
    },
    "5. Object-Oriented Programming (OOP)": {
        "notes": """
        ### Core Concepts: OOP in Python
        *   **Class**: A blueprint or template for creating objects.
        *   **Object**: An instance of a class.
        *   **`__init__`**: The constructor method that initializes an object's attributes when created.
        *   **`self`**: Represents the specific instance of the object being handled.
        *   **Four Pillars**:
            1. *Inheritance*: A child class deriving attributes/methods from a parent class.
            2. *Polymorphism*: Multiple classes having the same method name but different behaviors.
            3. *Encapsulation*: Hiding internal states and requiring all interaction to be performed through an object's methods.
            4. *Abstraction*: Hiding complex implementation details.

        ```python
        class Animal:
            def __init__(self, name):
                self.name = name
            
            def speak(self):
                return f"{self.name} makes a sound."

        dog = Animal("Buddy")
        print(dog.speak())
        ```
        """,
        "quiz": {
            "question": "What is the purpose of the '__init__' method in a Python class?",
            "options": ["To delete an object", "To initialize the object's attributes", "To import external modules", "To private-encode a class"],
            "answer": "To initialize the object's attributes",
            "explanation": "`__init__` is the constructor method in Python. It automatically runs when a new instance of a class is created."
        }
    }
}

# Sidebar Selection
st.sidebar.title("📚 Course Navigation")
selected_module = st.sidebar.radio("Go to Module:", list(modules.keys()))

# Main Content Layout
notes_tab, quiz_tab = st.tabs(["📝 Revision Notes", "🧠 Interactive Quiz"])

with notes_tab:
    st.markdown(modules[selected_module]["notes"])

with quiz_tab:
    st.subheader("Test Your Knowledge")
    quiz_data = modules[selected_module]["quiz"]
    
    # We use a unique key per module to reset states correctly
    user_choice = st.radio(
        quiz_data["question"], 
        quiz_data["options"], 
        key=f"radio_{selected_module}"
    )
    
    # Check answer button
    if st.button("Submit Answer", key=f"btn_{selected_module}"):
        if user_choice == quiz_data["answer"]:
            st.success("🎉 Correct! Well done.")
        else:
            st.error(f"❌ Incorrect. The correct answer is: {quiz_data['answer']}")
        
        # Display explanation
        st.info(f"**Explanation:** {quiz_data['explanation']}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit. Perfect for quick Python assessments.")
