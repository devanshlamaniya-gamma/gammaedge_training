# # 1.Write a program to print all even numbers from 1 to 100 using a for loop.

for i in range(100+1):
    if i%2 == 0:
        print(i)

# # 2.Print the first 10 numbers in the Fibonacci sequence using a while loop.

def fibo(n):

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibo(n-1) + fibo(n-2)

for i in range(10+1):
    print(fibo(i) , end= " ")
print()

# # 3.Create a list of squares of numbers from 1 to 10 using list comprehension.

l = [x * x for x in range(10 + 1)]
print(l)

# # 4.Write a program to find the largest element in a list.

l = [3,54,6,5,76,45,33,98]
max = 0

for i in l:
    if i > max:
        max = i

print(max)

# # 5.Write a program to find the second largest number in a list without sorting.

def second_highest(l):

    max1 = max2 = 0

    for i in l:
        if i > max1:
            max2 = max1
            max1 = i

    if max2 > max1:
        max2 = max1

    return max2

l = [3,54,6,5,76,45,33,98]
print(second_highest(l))

# # 6.Create a dictionary from two lists (one for keys, one for values) using zip().

list1 = [1,2,3,4,5]
list2 = ["one", "two", "three", "four", "five"]

a = dict(zip(list1 , list2))
print(a)

# # 7.Find the common elements between two lists using sets.

l1 = [1,3,5,2,6,6,8,9]
l2 = [7,5,5,7,8,3,4,7,8]

s1 = set(l1)
s2 = set(l2)
print(s1 & s2)

# 8.Implement a basic phonebook using a dictionary (add, search, delete, update contacts).


def phonebook():

    phonebook_dict = {}

    while True:

        print("""
these are options
              1.see all contacts
              2.add a contact
              3.search a contact
              4.delete a contact
              5.update a contact
              6.exit
""")
        user = int(input("enter your choice : "))

        if user == 1:
            for key,value in phonebook_dict.items():
                print(key ,"=>" , value)

        elif user == 2 or user == 5:
            name = input("enter name :")
            number = input("enter number : ")

            phonebook_dict[name] = number

        elif user == 3:

            name = input("enter name :")

            print(phonebook_dict[name])

        elif user == 4:
            name = input("enter name : ")

            phonebook_dict.pop[name]

        elif user ==6:
            break

        else:
            print("invalid input")

phonebook()

# 9.Implement a program to check if parentheses/brackets in a string are balanced using a stack (list).

def check_brackets(s):

    count = 0
    
    for i in s:
        if i == "[" or i == "(" or i == "{":
            count +=1

        elif i == "]" or i == ")" or i == "}":
            count -=1

    if count != 0:
        return "no the brackets are not balanced"
    
    else:
        return "the brackets are balanced"
    
print(check_brackets("([[{}]]])"))


def check_brackets(s):

    s = list(s)

    open = []
    close = []

    for i in range(0,len(s)):
        if s[i] == "(":
            open.append(s[i])

        elif s[i] == ")":
            close.append(s[i])

    if len(open) == len(close): 
        return True
    else:
        return False

print(check_brackets("(((a+b)*c)+(b*a))"))        


# 10.Create a dictionary that groups anagrams together from a list of words.


# l = ["tea" , "eat" ,"ate" ]

# for i in l:
#     if 