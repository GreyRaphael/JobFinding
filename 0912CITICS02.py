import sys


def solution(a,b):
    col=int(a)
    row=int(b)

    matrix=[[]]
    for i in range(col):
        if i<col/2:
            matrix[0].append(i+1)
        else:
            matrix[0].append(col-i)

    for j in range(1, row):
        if j<row/2:
            matrix.append([j+1]*col)
        else:
            matrix.append([row-j]*col)


    for i in range(1, row):
        for j in range(1, col):
            matrix[i][j]=matrix[i][j-1]+matrix[i-1][j]
   
    matrix_sum=0
    for k in range(row):
        matrix_sum+=sum(matrix[k])
    
    return matrix_sum
    

if __name__ == "__main__":
    string_data=sys.stdin.readline()
    a, b=string_data.split(' ')
    result = solution(a, b)
    print(result)
