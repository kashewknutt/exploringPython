from betterMinor import matrix
from determinant import det
print("Enter the size of the matrix: ")

choice = input("Enter size:")
while choice.isdigit()==False:
    print("Integers only please:")
    choice = input("Enter size:")
n = int(choice)
mat=matrix(n,n,0)
for i in range(n):
    for j in range(n):
        choicedit=input("Enter the element(%d,%d) please:"%(i,j))
        while (choicedit.lstrip('-')).isdigit()==False:
            print("Integer values only please:")
            choicedit=input("Enter the element (%d,%d) please:"%(i,j))
        mat[i][j]=int(choicedit)
        for x in range(n):
            for y in range(n):
                print(mat[x][y],end='\t')
            print()
            print()    
print("The determinant of the matrix: ",end='\t')
print(det(mat))
