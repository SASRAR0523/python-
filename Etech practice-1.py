#secret number finder
scrt_number = 18

while(True):
    num = int(input("Enter your number: "))
    if num == scrt_number:
        print("You got your secret number....!")
        break
    elif num < scrt_number:
        print("too low")
    elif num > scrt_number:
       print("too high")
    else:
        print("Try Again Later...!")

#Reversed character / string / number
char = input("Enter character value : ")

print("Reversed character value :",char[::-1])

#Greatest of three numbers
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
c = int(input("Enter c value: "))

if a>b and a>c:
    print("a is high")
elif b>a and b>c:
    print("b is high")
else:
    print("c is high")

#print the Even Numbers
for i in range(0,12,2):
    print(i)

#print the odd Numbers
for i in range(1,13,2):
    print(i)

#simple login system
username = input("username:")
password = input("password:")

if (username == "coder" and password == "123456"):
    print("Login Successfully...! Do more practice on coding")
else:
    print("Invalid login! try again....")

#To print the right angle triangle of integers
n = int(input("Enter value : "))

for i in range(1, n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#Even numbers array
n = int(input("Enter n value : "))
arr = list(map(int, input().split()))

for num in arr:
    if num % 2 == 0:
        print(num,end=" ")

#odd numbers array
n = int(input("Enter n value : "))
arr = list(map(int, input().split()))

for num in arr:
    if num % 2 != 0:
        print(num,end=" ")

#Average of array
n = int(input("Enter n value : "))
arr = list(map(int, input().split()))

avg = sum(arr) / n
print(avg)  

#smallest , biggest & Average values in array
n = int(input("enter n value: "))
arr = list(map(int,input().split()))
avg = sum(arr) / n

print("Minimum value: ", min()arr))
print("Maximum value: ", max(arr))
print("Average value: ", avg)

#find the leap year

while True:
    year = int(input("Enter Year: "))

    # Check leap year conditions
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("You got it! It's a leap year")
        break  # Exits the loop when correct
    else:
        print("Not a leap year. Try again!\n")

#simple vote & eligible criteria for vote

age = int(input("Enter your age : "))
nationality = input("Enter your nationality : ")

if (age >= 18 and nationality =="indian"):
    print("Eligible for vote !")
else:
    print("Not Eligible for vote ")

#string  operations
s = "hello world"

print(s[::-1])
print(s.upper())
print(s.lower())
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(s.replace('world', 'user'))
print(s.find('hello'))
print(s.count('l'))
print(s.startswith('he'))
print(s.endswith('ll'))

#File operations
file = open('Etech practice-1.txt','w')
file.write("Hello")

#ASCII CHARACTER FINDER
n = int(input("Enter value : "))

if 65<=n<=90 or 97<=n<=122:
    print("it is a ASCII character")
else:
    print("NOT AN ASCII VALUE")

#PROGRAM USING TRY-EXCEPT BLOCK 

def validate_phone(phone):
    if len(phone) != 10:
        raise ValueError(f'phone number must have 10 digits')
    return True

try:
    validate_phone('123456')
except ValueError as e:
    print('Error',e)

#Exam doubted programs 

for i in range(3):
    for j in range(3):
        if j==1:
            break
        print(i,j)

x = [1,2,3,4,5]
print(x[1:3])

squares = {x:x*x in range(4)}
print(squares)


#Bank balance project
balance = 10000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("New Balance:", balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful!")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("Thank you for using the ATM!")
        break   # Exit the loop

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")

#Factorials using for loop

n = int(input("Enter a number : "))

fact = 1

for i in range(1,n+1):
    fact = fact*i

print("Factorial :",fact)

#count the words in the text

text = input("Enter a string : ")

count = 0
for ch in text:
    count += 1

print("no.of words : ",count)

#count the vowels in the text

s = input("enter text : ")

vowels = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1

print("vowels: ",vowels)

#inheritance concept

class animal:
    def sound(self):
        print("animal sound")

class Dog(animal):
    def sound(self):
        print("Bark")

class Cat(animal):
    def sound(self):
        print("meow")

d = Dog()
c = Cat()

d.sound()
c.sound()

#2.

class Dog:
    def sound(self):
        print("dog barks")

class Cat:
    def sound(self):
        print("cat meow's")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())

#3.
class cal:
    def mul(self,a,b):
        return a*b
    def add(self,a,b,c):
        return a+b+c
    def div(self,c,d):
        return c/d
    def sub(self,x,y):
        return x-y
    def asrar(self,m,n):
        return m//n

obj = cal()
print(obj.mul(20,30))
print(obj.add(10,20,30))
print(obj.div(10,2))
print(obj.sub(10,10)
print(obj.asrar(25,5))


#Abstraction in oops
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class rectangle(shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        print(self.l*self.b)

r = rectangle(10, 90)

r.area()

#Mathematical operations

import math

print(math.sqrt(25))
print(math.ceil(25.5))
print(math.floor(25.5))
print(math.pi)

#os keywords

import os

print(os.getcwd)
print(os.listdir)
print(os.mkdir('new folder'))

#Date & time operations

#print the today's date
from datetime import datetime,date,timedelta
now = datetime.now()

#print the today's date
print(now.year, now.month,now.day)
print(now.strftime('%H : %M :%S'))

today = date.today()
print(today)

#print the tomorrow date
tomorrow = today + timedelta(days = 1)
print(tomorrow)

#to find the difference between days
diff = datetime(2026,1,1) - datetime.now()
print(diff)

#1.Write a Python program that divides two numbers entered by the user, using 
#exception handling to catch division by zero and invalid (non-numeric) input.  

try:
    num1 = float(input("Enter first value : "))
    num2 = float(input("Enter second value : "))

    result = num1/num2
    print("Result : ",result)


except ZeroDivisionError :
    print("Error : Divided by zero is not allowed...!")

except ValueError :
    print("Error : please enter valid numeric values")

finally:
    print("Note : program successfully closed!")

#2.  Write a Python program to create a class Employee with attributes name and 
#salary, and a method to display employee details. Create two objects and print 
#their details.

class Asrar:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.age)
        print(self.salary)
        print()

n1=input("enter the name of the student:")
n2=int(input("enter age:"))
n3=int(input("enter the salary:"))

p1=input("enter the name of the student:")
p2=int(input("enter age:"))
p3=int(input("enter the salary:"))

a1 = Asrar(n1,n2,n3)
a2 = Asrar(p1,p2,p3)

print("employee one details :")
a1.display()
print("employee two details :")
a2.display()

 #3.Write a Python program to implement inheritance where a class Shape has a 
#method area(), and subclasses Rectangle and Circle override it to calculate their 
#respective areas.  

import math

class Area:
    def area(self):
        print("Area of shape")

class Rectangle(Area):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of Rectangle = ",self.length * self.breadth)

class circle(Area):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print("Area of circle = ",math.pi * self.radius * self.radius)   

r1 = Rectangle(10,20)
c1 = circle(50)

r1.area()
c1.area()

# 4. Write a Python program to demonstrate polymorphism by creating a function describe(animal) 
# that calls a speak() method, which behaves differently for Dog and Cat class objects.

class Dog:
    def speak(self):
        return "Barks...!"

class Cat:
    def speak(self):
        return "Meows...!"

def describe(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

describe(dog)
describe(cat)

# 5.Write a Python program to demonstrate encapsulation by creating a class 
# BankAccount with a private balance attribute, along with getter and setter 
# methods to access and update it safely.  



#project using simple python
# Calculator App Project

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a % b

def power(a, b):
    return a ** b

while True:
    print("\n1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. MODULUS")
    print("6. POWER")
    print("7. EXIT")

    choice = int(input("Enter your choice: "))

    if choice == 7:
        print("Calculator Closed")
        break

    if choice < 1 or choice > 7:
        print("Invalid Choice")
        continue

    value1 = float(input("Enter first value: "))
    value2 = float(input("Enter second value: "))

    if choice == 1:
        print("Result:", add(value1, value2))
    elif choice == 2:
        print("Result:", sub(value1, value2))
    elif choice == 3:
        print("Result:", multiply(value1, value2))
    elif choice == 4:
        print("Result:", divide(value1, value2))
    elif choice == 5:
        print("Result:", modulus(value1, value2))
    elif choice == 6:
        print("Result:", power(value1, value2))

#project - 2
#Bank Management project using oops concepts & getter , setter methods

from abc import ABC, abstractmethod

# Abstract Class
class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def display(self):
        pass


# Bank Account Class
class BankAccount(Person):
    total_account = 0

    def __init__(self, name, account_no, balance):
        super().__init__(name)
        self.account_no = account_no
        self.__balance = balance

        BankAccount.total_account += 1

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Amount cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Amount deposited successfully...!")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance...!")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.__balance -= amount
            print("Amount withdrawn successfully...!")

    def display(self):
        print("\n----- Account Details -----")
        print("Account Number :", self.account_no)
        print("Account Holder :", self.name)
        print("Balance        :", self.__balance)

    @classmethod
    def show_total(cls):
        print("Total Accounts :", cls.total_account)

    @staticmethod
    def bank_rules():
        print("\nBank Rules")
        print("Minimum balance : 1000")
        print("Working days    : Mon-Fri")
        print("Bank hours      : 9 AM - 5 PM")
        print("Interest        : 5%")


# Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, name, account_no, balance):
        super().__init__(name, account_no, balance)

    def display(self):
        super().display()


# Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_no = int(input("Enter Account Number: "))
        name = input("Enter Name: ")
        balance = float(input("Enter Balance: "))

        account = SavingsAccount(name, account_no, balance)

        self.accounts[account_no] = account
        print("Account created successfully...!")

    def search(self):
        account_no = int(input("Enter Account Number: "))

        if account_no in self.accounts:
            return self.accounts[account_no]
        else:
            print("Account not found")
            return None

    def deposit(self):
        account = self.search()
        if account:
            amount = float(input("Enter Deposit Amount: "))
            account.deposit(amount)

    def withdraw(self):
        account = self.search()
        if account:
            amount = float(input("Enter Withdraw Amount: "))
            account.withdraw(amount)

    def display(self):
        account = self.search()
        if account:
            account.display()


# Driver Code
bank = Bank()

while True:
    print("\n========= BANK MENU =========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Bank Rules")
    print("6. Total Accounts")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bank.create_account()

    elif choice == 2:
        bank.deposit()

    elif choice == 3:
        bank.withdraw()

    elif choice == 4:
        bank.display()

    elif choice == 5:
        BankAccount.bank_rules()

    elif choice == 6:
        BankAccount.show_total()

    elif choice == 7:
        print("Thank You... Visit Again!")
        break

    else:
        print("Invalid Choice")

#prime number

n = int(input())

if n <= 0:
    print(“Not prime”)
else:
    prime = True

for i in range(2,n):
    if n%i == 0:
        prime = False
	  break

if prime:
    print(“prime”)
else:
    print(“Not prime”)


#reverse the number

n = int(input())

reverse = 0

while n>0:
    digit = n%10
    reverse = reverse * 10 + digit
    n = n//10

print(reverse)

#palindrome number

n = int(input())

original = n

reverse = 0

while n>0:
    digit = n%10
    reverse = reverse * 10 + digit
    n = n//10

if original == reverse:
    print(“palindrome”)
else:
    print(“Not palindrome”)

#Input Format
#The input is a single integer N, representing the value of the item code.

#Output Format
#Print the product of all the digits of the number N.

n = int(input())

product = 1

if n == 0:
    product = 0
else:
    while n > 0:
        digit = n % 10
        product *= digit
        n //= 10

print(product)

#Input Format
#The input is a single integer n.

#Output Format
#Print the sum of all even digits in the number.

n = int(input())

sum = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        sum += digit

    n = n//10
print(sum)

#Input Format
#The input consists of two integers: N (positive integer) and R (non-negative integer).

#Output Format
#Print the single-digit result obtained after R iterations of summing the digits of N.

n = int(input())
r = int(input())

if r == 0:
    print(0)
else:
    for i in range(r):
        sum = 0

        while n > 0:
            digit = n % 10
            sum = sum + digit
            n = n // 10

        n = sum

    print(n)

#Given two integers, dividend and divisor, find the remainder when dividend is divided by divisor without using the / or % operators.

#Input Format
#The input consists of two integers: dividend and divisor.

#Output Format
#Print the remainder when dividend is divided by divisor.

dividend , divisor = map(int,input().split())

while dividend >= divisor:
    dividend = dividend - divisor

print(dividend)

#Input Format
#First line contains an integer n, representing size of an array.

#Second line contains n space separated integer values.

#Output Format
#The output is the array with all zeros moved to the end, while maintaining the order of non-zero elements.

n = int(input())
arr = list(map(int, input().split()))

result = []

for x in arr:
    if x != 0:
        result.append(x)

while len(result) < n:
    result.append(0)

print(*result)

#Print all prime numbers between n1 and n2.

n1, n2 = map(int, input().split())

for n in range(n1, n2 + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")

#Given an unsorted array of integers, find the length of the longest increasing subsequence.

n = int(input())
arr = list(map(int, input().split()))

lis = []

for num in arr:
    if not lis or num > lis[-1]:
        lis.append(num)
    else:
        for i in range(len(lis)):
            if lis[i] >= num:
                lis[i] = num
                break

print(len(lis))

# You are given an array/list `ARR` consisting of `N` integers. 
# Your task is to find the majority element in the array. 
# If there is no majority element, print `-1`. 
# A majority element is an element that appears more than `floor(N / 2)` times in the array.

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    majority = -1

    for num in arr:
        if arr.count(num) > n // 2:
            majority = num
            break

print(majority)

# You are given two strings S and T with lengths M and N.
# Your task is to find the length of the 'Longest Common Subsequence' (LCS) between the two strings. 
# subsequence of a string is a sequence containing characters in the same relative order as in the string, 
# but not necessarily contiguous. The LCS is the longest subsequence that appears in both strings.

s = input()
t = input()

m = len(s)
n = len(t)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[m][n])

# Rhea Pandey’s teacher has asked her to prepare for a lesson on seasons. When her teacher mentions a month,
# Rhea needs to identify the corresponding season. Your task is to write a program that takes an input month (as a number from 1 to 12) and 
# outputs the season it belongs to: - **Spring** – March (3) to May (5) - **Summer** – June (6) to August (8) - **Autumn** – September (9) to November (11)
# - **Winter** – December (12) to February (2) If the input month is not in the range of 1 to 12, print "Invalid month".

month = int(input())

if month >= 3 and month <= 5:
    print("Season:Spring")
elif month >= 6 and month <= 8:
    print("Season:Summer")
elif month >= 9 and month <= 11:
    print("SeasonAutumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("Invalid month")

# A Discrete Mathematics professor will cancel class if fewer than a threshold number of students are on time. 
# Given a list of student arrival times, determine if the class will be cancelled. 
# Non-positive arrival times represent students who arrived early or on time, while positive times indicate lateness.

n,k = map(int,input().split())
arr = list(map(int,input().split()))

count = 0

for time in arr:
    if time <= 0:
        count += 1

if count < k:
    print("YES")
else:
    print("NO")

#You are given an array A of size N. An equilibrium point is an index in A such that the sum of elements to 
#the left of that index is equal to the sum of elements to the right of that index. Find the total number of equilibrium points in A.

n = int(input())
a = list(map(int, input().split()))

total_sum = sum(a)
left_sum = 0
count = 0

for i in range(n):
    right_sum = total_sum - left_sum - a[i]

    if left_sum == right_sum:
        count += 1

    left_sum += a[i]

print(count)

#Little Bobby loves chocolate and can exchange wrappers for free chocolates in a promotional offer.
#Given the amount of money, the cost of each chocolate, and the number of wrappers needed to exchange 
#for a free chocolate, determine how many chocolates Bobby can eat.

n, c, m = map(int, input().split())

chocolates = n // c
wrappers = chocolates

while wrappers >= m:
    free = wrappers // m
    chocolates += free
    wrappers = (wrappers % m) + free

print(chocolates)

#You are given an array 'ARR' of integers of length N. Find the first missing positive integer in linear time and constant space. 
#In other words, find the lowest positive integer that does not exist in the array. The array can contain negative numbers as well.

import sys

def first_missing_positive(arr):
    n = len(arr)
    for i in range(n):
        while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
            correct_idx = arr[i] - 1
            arr[i], arr[correct_idx] = arr[correct_idx], arr[i]

    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1

def solve():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx + n])); idx += n
        results.append(str(first_missing_positive(arr)))
    print('\n'.join(results))

solve()

#Jack loves Sundays and wants to count how many Sundays will occur within a given number of days 
#from the start of the month, based on the starting day of the week.

import sys

# Read all lines, strip whitespace, and ignore empty lines
lines = [line.strip() for line in sys.stdin if line.strip() != ""]

start_day = lines[0].lower()
n = int(lines[1])

day_index = {
    "mon": 0,
    "tue": 1,
    "wed": 2,
    "thu": 3,
    "fri": 4,
    "sat": 5,
    "sun": 6
}

start_idx = day_index[start_day]

# Find the day number (1-indexed) of the first Sunday
days_until_sunday = (6 - start_idx) % 7
first_sunday_day = days_until_sunday + 1

# Count how many Sundays fall within n days
if n >= first_sunday_day:
    count = (n - first_sunday_day) // 7 + 1
else:
    count = 0

print(count)

#Joseph is learning digital logic and faces a tricky problem: given a positive integer,
#convert its decimal value to a binary representation, toggle all bits of it including 
#and after the most significant bit, and then print the positive integer value after toggling.

n = int(input().strip())

# Find number of bits required to represent n in binary
num_bits = n.bit_length()

# Create a mask of all 1s with the same number of bits
mask = (1 << num_bits) - 1

# Toggle all bits by XOR-ing with the mask
result = n ^ mask

print(result)

#A furnishing company is manufacturing a new collection of curtains. 
#The curtains are of two colors aqua(a) and black (b). The curtains color is represented as a string(str) consisting of a's and b's of length N. 
#Then, they are packed (substring) into L number of curtains in each box. The box with the maximum number of 'aqua' (a) color curtains is labeled.
#The task here is to find the number of 'aqua' color curtains in the labeled box.

# Read input
curtains = input().strip()
L = int(input().strip())

n = len(curtains)
max_count = 0

# Split the string into chunks of size L
for i in range(0, n, L):
    chunk = curtains[i:i+L]
    a_count = chunk.count('a')
    if a_count > max_count:
        max_count = a_count

print(max_count)

#Count the number of digits in a positive integer.

num = input().strip()

n = int(num)

digit_count = len(str(abs(n)))

print(digit_count)

#Particulate matters are the biggest contributors to Delhi pollution. 
#The main reason behind the increase in the concentration of PMs include vehicle emission by applying 
#Odd Even concept for all types of vehicles. The vehicles with the odd last digit in the registration number 
#will be allowed on roads on odd dates and those with even last digit will on even dates.

import sys

# Read all tokens from input, ignoring how they're split across lines
data = sys.stdin.read().split()

# First token is N
n = int(data[0])

# Next N tokens are the digits
digits = [int(x) for x in data[1:1+n]]

# Last two tokens are D and X
d = int(data[1+n])
x = int(data[2+n])

# Determine which parity is allowed based on the date
date_is_odd = (d % 2 == 1)

fine_count = 0
for digit in digits:
    digit_is_odd = (digit % 2 == 1)
    if digit_is_odd != date_is_odd:
        fine_count += 1

total_fine = fine_count * x

print(total_fine)




















































