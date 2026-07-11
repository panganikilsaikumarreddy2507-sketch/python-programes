r=int(input("enter no.rows:"))
c=int(input("enter no.col:"))
A=[list(map(int, input("enter the A matrix:").split() for _ in range(r)))]
B=[list(map(int, input("enter the B matrix:").split()for _ in range(r)))]
print("matrix:",A)
print("matrix:",B)
C=[[A[i][j]+B[i][j] for j in range(r)]for i in range(r)]
for row in C:
    print(row)























