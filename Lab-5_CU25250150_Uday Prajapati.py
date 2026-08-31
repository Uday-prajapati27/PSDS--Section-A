# LAB ASSIGNMENT 5
# Infix to Postfix Conversion
# Using Custom Operator Stack


class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, value):
        self.stack.append(value)

    # Pop operation
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    # Peek operation
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    # Check whether stack is empty
    def is_empty(self):
        return len(self.stack) == 0


# Operator precedence
def precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0


def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""

    for character in expression:

        # Ignore spaces
        if character == ' ':
            continue

        # If operand, add directly to postfix
        if character.isalnum():
            postfix += character

        # If opening bracket
        elif character == '(':
            stack.push(character)

        # If closing bracket
        elif character == ')':

            while not stack.is_empty() and stack.peek() != '(':
                postfix += stack.pop()

            stack.pop()  # Remove '('

        # If operator
        else:

            while (not stack.is_empty() and
                   stack.peek() != '(' and
                   precedence(stack.peek()) >= precedence(character)):

                postfix += stack.pop()

            stack.push(character)

    # Pop remaining operators
    while not stack.is_empty():
        postfix += stack.pop()

    return postfix


# Main program
expression = input("Enter infix expression: ")

result = infix_to_postfix(expression)

print("Postfix expression:", result)


# LAB ASSIGNMENT 5
# Postfix Expression Evaluation
# Using Integer Stack


class IntegerStack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, value):
        self.stack.append(value)

    # Pop operation
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()


def evaluate_postfix(expression):

    stack = IntegerStack()

    for character in expression:

        # If character is a digit
        if character.isdigit():
            stack.push(int(character))

        # If character is an operator
        else:

            operand2 = stack.pop()
            operand1 = stack.pop()

            if character == '+':
                result = operand1 + operand2

            elif character == '-':
                result = operand1 - operand2

            elif character == '*':
                result = operand1 * operand2

            elif character == '/':
                result = operand1 / operand2

            elif character == '^':
                result = operand1 ** operand2

            stack.push(result)

    return stack.pop()


# Main program
expression = input("Enter postfix expression: ")

result = evaluate_postfix(expression)

print("Result:", result)
