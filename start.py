import solver

width = int(input("Width of the matrix (including right hand side): "))
height = int(input("Height of the matrix: "))
matrix = []

for i in range(0, height):
    matrix.append([])
    for j in range(0, width):
        if(j+1 == width):
            print("-->Right Hand Side:")
        t = eval(input("->entry at ["+ str(i)+", "+ str(j)+ "]: "))
        matrix[i].append(t)
    print("<-Next Row: ")

solver.print_matrix(matrix)
solver.solve(matrix)
