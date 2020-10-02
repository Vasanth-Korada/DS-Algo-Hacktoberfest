##INVERTED PYRAMID USING EXTRA LOGIC.

N = int(input("Enter the Input: "))
lines = {}
counter = 1
print("Inverted Pyramid ")
for row in range(N):
    lines[row] = (row*2)*" "
    for col in range(1,(N-row+1)):
        lines[row]+=str(counter)+" " 
        counter+=1

for row in range(N-1,-1,-1):
    for col in range(1,(N-row)):
        lines[row]+=str(counter)+" " # print for all except the last column
        counter+=1
    lines[row]+=str(counter)
    counter+=1

for i in range(N):
    print(lines[i])
    

