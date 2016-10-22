def solve_matrix(matrix):
    smallest_side = len(matrix) if len(matrix) <= len(matrix[0])-1 else len(matrix[0])-1
    for RC in range(0, smallest_side): # go down main diagonal
        RCp = RC
        if(matrix[RC][RCp] == 0): # switch rows if our pivot is 0
            for i in range(RC, len(matrix)):
                if(matrix[i][RC]!=0):
                    row_switch(matrix, RC, i)
            if(matrix[RC][RCp] == 0): # search for a number to the right of our zero pivot
                for i in range(RCp, len(matrix[0])-1):
                    if(matrix[RC][i]!=0):
                        RCp = i
                        break
        for i in range(0, len(matrix)): # apply row_combined operation to the right rows
            if i == RC:
                continue
            elif check_if_consistent(matrix):
                row_combined(matrix, matrix[RC][RCp], RC, matrix[i][RCp], i)
            else:
                return

def check_if_consistent(matrix): # checks for zero row with non-zero right hand side
    for R in range(0, len(matrix)):
        zero_count = 0
        for C in range(0, len(matrix[R])):
            if matrix[R][C] != 0: # if we run into a non-zero, skip to next Row
                break
            if matrix[R][C] == 0:
                zero_count+=1
            if C == len(matrix[R])-2 and zero_count == C+1 and matrix[R][C+1] != 0:
                print("System is inconsistent")
                return False
    return True

def simplify_matrix(matrix): # iterates through main diagonal using those pivots to divide and smplify each row
    smallest_side = len(matrix) if len(matrix) <= len(matrix[0]) else len(matrix[0])
    for RC in range(0, smallest_side):
        row_div(matrix, matrix[RC][RC], RC)

def row_combined(matrix, p, pivot_row, c, target_row): # performs a combined elementary row operation
    result_row = []
    for i in range(0, len(matrix[pivot_row])): # R' << p(Rc) - c(Rp)
        result_row.append(p*matrix[target_row][i] - c*matrix[pivot_row][i])
    matrix[target_row] = result_row
    print("p:" + str(p))
    print_matrix(matrix)
    print("")

def row_div(array, divisor, target_row_index):
    if(divisor == 0):
        return
    temp_target_row = []
    for i in range(0, len(array[target_row_index])):
        temp_target_row.append(array[target_row_index][i]/divisor+0.0) # add zero to get rid of negative zeros
    array[target_row_index] = temp_target_row

def row_switch(array, row_a, row_b):
    temp = array[row_a]
    array[row_a] = array[row_b]
    array[row_b] = temp

def print_matrix(array):
    for i in range(0, len(array)):
        for j in range(0, len(array[i])):
            if j+1 == len(array[i]):
                print("|", array[i][j])
            else:
                print(array[i][j], end=" ")

def solve(matrix):
    solve_matrix(matrix)
    simplify_matrix(matrix)
    print_matrix(matrix)

if __name__ == "__main__":
    tridiagonal = [[1,4,0,0,23],
                   [3,4,1,0,46],
                   [0,2,3,4,69],
                   [0,0,1,3,138]]
    solve(tridiagonal)
