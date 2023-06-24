def is_balanced(parentheses):
    stack = []
    opening_brackets = ['[', '{', '(']
    closing_brackets = [']', '}', ')']

    for char in parentheses:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_opening = stack.pop()
            if opening_brackets.index(last_opening) != closing_brackets.index(char):
                return False

    return len(stack) == 0


# Get test cases from user
num_test_cases = int(input("Enter the number of test cases: "))
test_cases = []
for i in range(num_test_cases):
    test_case = input(f"Enter test case #{i + 1}: ")
    test_cases.append(test_case)

# Test the function
for i, test_case in enumerate(test_cases):
    if is_balanced(test_case):
        print(f"Test case #{i + 1}: {test_case} is balanced.")
    else:
        print(f"Test case #{i + 1}: {test_case} is not balanced.")
