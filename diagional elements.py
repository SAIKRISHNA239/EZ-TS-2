def display_diagonal_elements(matrix):
    diagonal = []
    non_diagonal = []
    upper_diagonal = []
    lower_diagonal = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if i == j:
                diagonal.append(matrix[i][j])
            else:
                non_diagonal.append(matrix[i][j])
            if i < j:
                upper_diagonal.append(matrix[i][j])
            elif i > j:
                lower_diagonal.append(matrix[i][j])
    print("Diagonal elements:", diagonal)
    print("Non-diagonal elements:", non_diagonal)
    print("Upper diagonal elements:", upper_diagonal)
    print("Lower diagonal elements:", lower_diagonal)
matrix = [] 
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print("Enter the matrix elements:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input("Enter element at position ({}, {}): ".format(i, j)))
        row.append(element)
    matrix.append(row)
display_diagonal_elements(matrix)
