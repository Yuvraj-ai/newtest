# my_module.py - Updated version on the main branch, after branching and further changes

def greet(name):
    """Prints a simple greeting."""
    print(f"Hello, {name}!")

def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def process_file(filename):
    """Reads and prints the content of a file (new functionality in main branch)."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Contents of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# TODO: Implement a more robust error handling for file operations

# This function was considered but skipped in the initial version
# def calculate_average(numbers):
#     if numbers:
#         return sum(numbers) / len(numbers)
#     return 0

# This function was considered for a different branch and skipped here
# def analyze_data(data):
#     # Complex data analysis logic
#     pass
