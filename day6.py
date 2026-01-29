# 1.Write a program to swap two variables without using a third variable.

a = 5
b = 10

a , b = b , a 
print(a)
print(b)

# 2.Create a program that takes user input for name and age, then prints a formatted message using f-strings.

name = str(input("Enter name : "))
age = int(input("Enter age : "))

print(f" Hello , the age of {name} is {age}")


# 3.Write a program to check if a number is even or odd using modulo operator.

num = int(input("Enter a number : "))

if num %2 == 0:
    print("the number is even.")

else:
    print("the number is odd.")

# 4.Convert temperature from Celsius to Fahrenheit and vice versa. 

def fahrenheit_to_celsius(f):

    return ((f - 32) * 5 / 9)

print(fahrenheit_to_celsius(5))

def celsius_to_fahrenheit(c):

    return (c * 9/5) + 32

print(celsius_to_fahrenheit(5))

# 5.Check if a given string is a palindrome (case-insensitive).

def check_palindrome(s):

    reversed = ""

    for ch in s:
        reversed = ch + reversed

    if s == reversed:
        print("yes , the string is palindrome . ")
    else:
        print("no , the string is not a palindrome")

check_palindrome("hello")

# 6.Count the frequency of each character in a string using a dictionary.

def check_freq(s) :

    frequency = {}

    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    return frequency

print(check_freq("hello my friend"))

# 7.Write a program to format a string using all three formatting methods (%, .format(), f-strings).

a = "devansh"
b = "lamaniya"

print("hello i am %s %s " % (a , b) )

print("hello i am {0} {1}".format("devansh" , "lamaniya"))

print(f"hello i am {a} {b}")

# 8.Write a program to check if a year is a leap year.

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap(2024))


# 9.Check if two strings are anagrams of each other.

def check_anagram(a , b):

    return sorted(a) == sorted(b)

print(check_anagram("listen" , "silent"))

# 10.Create a CLI calculator that performs basic arithmetic operations based on user input with input validation.


def calc():

    a = float(input("enter a : "))
    b = float(input("enter b : "))
    operator = input("enter operator : + , - , * , / : ")

    if operator == "+":
        return a+b
    
    elif operator == "-":
        return a - b
    
    elif operator == "*":
        return a * b
    
    elif operator == "/":
        return a / b
    
print(calc())