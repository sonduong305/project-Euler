"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

primes = []

#biggest prime factor of the num parameter
def primeNumber(num):
    result = num
    pri = 2
    while (isPrime(result) == False):
        print(result)
        if(result % pri == 0):
            result /= pri
        else:
            pri = nextPrime(pri)
    return result

#check whether a number is prime number
def isPrime(number):
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True

# return next prime number greater than num
def nextPrime(number):
    while True:
        number+=1
        if isPrime(number):
            return number

print(primeNumber(600851475143))


