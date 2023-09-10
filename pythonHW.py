# Exercise 1

factorial = 1


def findFactorial(n):
    if n < 0:
        return "Please enter a Positive number"

    elif n == 0 or n == 1:
        return "Output: " + 1

    else: 
        for i in range(1, n + 1):
            factorial *= i

        return "Output: " + factorial
# this function helps us find the factorial of the input


# Exercise 2
divisors = []

def findDivisors(num):
    if n <= 0:
        return "You must enter a Positive number"
    
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
# this function helps us find all the divisors of the input
    

# Exercise 3 
def reverseInput(user_input):
    reversed_input = user_input[::-1]
    return reversed_input
# this function is use to reverse write the input a user puts in


# Exercise 4

list = []

def evenNumbers(nums):
    for i in range(nums):
        if i % 2 == 0:
            list.append(i)
    return list 
# function that captures only even numbers 


#Exercise 5 
def checkUserPassword(password)
#idk what to write 