'''
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
'''
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


