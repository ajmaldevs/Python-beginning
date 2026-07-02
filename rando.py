import random
programs=[
    "Area and volume of Sphere",
    "Area of Triangle",
    "Biggest from three number",
    "Grading program",
    "Positive Negative and zero",
    "Divisible by 5",
    "Three digit numbers",
    "Divisible by 3 and 4",
    "Grading using switch",
    "Armstrong number",
    "Palindrome number",
    "Multiplication table",
    "Sum of Digits",
    "Fibonacci series",
    "Factorial using Function",
    "Fibonacci series using Function",
    "Area of Different shapes using Function",
    "Factorial of 3 number using Function",
    "Largest element in an array",
    "Linear Search",
    "Sort Array (Ascending Order)",
    "Sum of a matrix",
    "Addition of two matrices"
]
a=[]
a=random.choice(programs)
print(a)
programs.remove(a)
print(f"Remaining: {len(programs)}")
