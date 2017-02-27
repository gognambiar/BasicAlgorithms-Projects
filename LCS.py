import numpy as np

file = open("input.txt")
ctr = 0
temp1 = []
temp2 = []
A = {}
B = {}
for line in file:
    if(ctr == 0):
        temp1.append(line)
        temp1[0] = temp1[0].replace("\n","")
    elif(ctr == 1):
        temp2.append(line)
	temp2[0] = temp2[0].replace("\n","")
    ctr += 1

file.close()
n = len(temp1[0])
m = len(temp2[0])


ctr = 1
while(ctr <= n):
    A.update({ctr : temp1[0][ctr-1]})
    ctr += 1    

ctr = 1
while(ctr <= m):
    B.update({ctr : temp2[0][ctr-1]})
    ctr += 1


opt = np.zeros((n+1,m+1))
pi = np.zeros((n+1,m+1))


for i in range(1,n+1):
    opt[i][0] = 0
    for j in range(1,m+1):
        if(A[i] == B[j]):
            opt[i][j] = opt[i-1][j-1] + 1
            pi[i][j] = 1
        elif(opt[i][j-1] >= opt[i-1][j]):
            opt[i][j] = opt[i][j-1]
            pi[i][j] = 2
        else:
            opt[i][j] = opt[i-1][j]
            pi[i][j] = 3

i = n
j = m
S = []

while((i > 0) & (j > 0)):
    if(pi[i][j] == 1):
        S.append(A[i])
        i -= 1
        j -= 1
    elif(pi[i][j] == 3):
        i -= 1
    else:
        j -= 1

K = S[::-1]

file = open("output.txt","w")
file.write(str(len(S)) + "\n")

for kj in K:
    file.write(kj)


file.close()
