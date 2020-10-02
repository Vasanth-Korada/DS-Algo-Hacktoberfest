##PRINTING FIBONACCI VALUES IN TRIANGLE PATTERN

n=int(input("Enter the Input: ")) #Taking user input 
a,b=0,1 #initialization
print("Fibonacci - Triangle")
for i in range(1,n+1):
    for j in range(i): #Pattern logic
        print(a,end=' ')
        a,b=b,a+b #Fibonacci logic
    a,b=0,1 #Reinitialization the fibonacci values
    print() #To print a new line