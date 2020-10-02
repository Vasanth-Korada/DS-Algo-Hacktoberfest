##TO CHECK IF A NUMBER IS PRIME NUMBER OR NOT USING SIEVE ALGO.

def SieveOfEratosthenes(n): 
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True]*(n+1) 
    prime[0]=False
    prime[1]=False
    p = 2
    while (p * p <= n): 
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime[n]

n=int(input("Enter the Input: "))
print(SieveOfEratosthenes(n))