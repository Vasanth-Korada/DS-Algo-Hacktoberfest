#PRINTING NUMBER IN SPIRAL PATTERN IN SQUARE

N=int(input("Enter the user Input: ")) #Taking user input
chakra=[[0 for i in range(N)] for i in range(N)]
co=1
print("Square - Sprial Pattern")
for i in range(N//2):
    row,col=i,i
    end_col=N-i-1
    while(col<end_col): #printing first row
        chakra[row][col]=co
        co+=1
        col+=1
    end_row=N-i-1
    while(row<end_row): #printing the last column
        chakra[row][col]=co  
        co+=1
        row+=1
    end_col=i
    while(col>end_col): #printing the bottom row
        chakra[row][col]=co
        co+=1
        col-=1
    end_row=i
    while(row>end_row): #printing the first column
        chakra[row][col]=co
        co+=1
        row-=1
if N%2==1:
    chakra[N//2][N//2]=N*N #printing middle most value
for i in range(N):
    for j in range(N):
        print(str(chakra[i][j]),end='\t')
    print()




