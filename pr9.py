# Stack Operations and Infix to Postfix Conversion


# ---------------- STACK OPERATIONS ----------------

stack = []

print("STACK OPERATIONS")

# Push operation
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after Push:")
print(stack)

# Peek operation
print("Top element:", stack[-1])

# Pop operation
item = stack.pop()
print("Popped element:", item)

print("Stack after Pop:")
print(stack)


# ---------------- INFIX TO POSTFIX ----------------

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0


def infix_to_postfix(expression):
    operators = []
    postfix = ""

    for character in expression:

        # If character is an operand
        if character.isalnum():
            postfix = postfix + character

        # If opening bracket
        elif character == '(':
            operators.append(character)

        # If closing bracket
        elif character == ')':
            while operators and operators[-1] != '(':
                postfix = postfix + operators.pop()

            if operators:
                operators.pop()

        # If operator
        else:
            while (operators and
                   operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(character)):
                postfix = postfix + operators.pop()

            operators.append(character)

    # Pop remaining operators
    while operators:
        postfix = postfix + operators.pop()

    return postfix


print("\nINFIX TO POSTFIX")

infix = input("Enter infix expression: ")

postfix = infix_to_postfix(infix)

print("Infix Expression:", infix)
print("Postfix Expression:", postfix)