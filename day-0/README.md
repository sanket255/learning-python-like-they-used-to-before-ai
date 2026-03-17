# Day 0: Python Basics - Three Challenges

This is Day 0 of the Python learning journey! This day focuses on fundamental Python concepts including user input, conditionals, loops, and basic data structures.

## Overview

The `main.py` file contains three progressive Python challenges that build on each other:

---

## Challenge 1: Simple Calculator (Easy)

**Objective:** Create a basic calculator program

**What it does:**
- Asks the user for two numbers
- Prompts the user to select an operation (+, -, *, /)
- Performs the mathematical operation
- Displays the result

**Concepts Covered:**
- User input with `input()`
- Type conversion with `int()`
- Conditional statements (`if`, `elif`, `else`)
- Basic arithmetic operations

**Example Usage:**
```
welcome to the calculator
insert the value number 1: 10
insert the value number 2: 5
insert the operation you wanna get done (+, -, *, /): +
15
```

---

## Challenge 2: Temperature Converter (Intermediate)

**Objective:** Convert temperatures from Celsius to Fahrenheit repeatedly

**What it does:**
- Runs a loop 5 times, allowing multiple conversions
- Takes a temperature in Celsius as input
- Converts to Fahrenheit using the formula: `(C × 9/5) + 32`
- Prints the converted temperature

**Concepts Covered:**
- Loops (`for` loop with `range()`)
- Variables and user input
- Mathematical calculations with formula

**Example Usage:**
```
insert the temprature1: 0
32.0
insert the temprature1: 100
212.0
insert the temprature1: 37
98.6
... (continues for 5 iterations)
```

---

## Challenge 3: Grade Calculator (Hard)

**Objective:** Calculate average test scores and assign letter grades

**What it does:**
- Asks the user to input 5 test scores
- Calculates the sum and average of the scores
- Assigns a letter grade based on the average:
  - A+ : 90+
  - A : 80-89
  - B+ : 70-79
  - B : 60-69
  - C+ : 50-59
  - C : 35-49
  - F : Below 35
- Prints all scores, the average, and the assigned grade

**Concepts Covered:**
- Lists and `append()` method
- Loop iteration
- Built-in functions (`sum()`, `len()`) 
- Complex conditional logic with multiple `elif` statements
- Data collection and display

**Example Usage:**
```
insert the marks: 95
insert the marks: 88
insert the marks: 92
insert the marks: 85
insert the marks: 90
450
90.0
A+
[95, 88, 92, 85, 90]
```

---

## Learning Outcomes

By completing these three challenges, you'll practice:
- Taking user input and validating data types
- Using conditionals to make decisions in code
- Implementing loops for repetitive tasks
- Working with lists and collections
- Performing calculations
- Combining multiple concepts in a single program
