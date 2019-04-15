m = [[0,0,0,1,0],[1,0,0,1,1],[0,0,0,1,0],[1,1,1,0,0],[0,1,0,0,0]]

k = 0
j = 0
numNodi = 5

for k in range(numNodi):
    for j in range(numNodi):
        if(m[k][j] == 1):
           print(str(k) + " è adiacente a " + str(j))
