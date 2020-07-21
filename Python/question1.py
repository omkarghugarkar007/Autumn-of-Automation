def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

n = int(input("Enter number of Digits"))

prime_number = list()

fhand = open("MyFirstFile.txt", "w")

for i in range(10**(n-1),10**n):

    bool = isPrime(i)

    if (bool):
        prime_number.append(i)

for i in range(len(prime_number) - 1):

    if (int(prime_number[i+1]) - int(prime_number[i])) == 2:

        fhand.write(str(prime_number[i]) + " " + str(prime_number[i+1]))
        fhand.write("\n")

fhand.close()