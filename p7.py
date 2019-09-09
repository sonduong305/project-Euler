"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""


def isPrime(number):
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True

num = 0
count = 2
while True:
    num += 6
    if(isPrime(num - 1)):
        count += 1
        if( count > 10000):
            print(num - 1)
            break
    if (isPrime(num + 1)):
        count +=1
        if( count > 10000):
            print(num + 1)
            break
    