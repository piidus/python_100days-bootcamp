'''
Instructions
Prime numbers are numbers that can only be cleanly divided by itself and 1.

https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.

e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

Unsupported image

Here are the numbers up to 100, prime numbers are highlighted in yellow:
'''

#Write your code below this line 👇
def prime_checker(number):
    len_number=range(2,number-1)
    prime = False
    for i in len_number:
        ew= number%i
        if ew==0:
            prime = True
    if prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
