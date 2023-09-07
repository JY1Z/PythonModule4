#4 While loops (while)
#1
i = 1
while i < 1000:
  if i%3 == 0:
    print(i)
    i = i + 1
  else:
    i = i + 1


#2
inches = float(input("Enter inches:"))
while inches >= 0:
  centimeters = 2.54 * inches
  print(centimeters)
  inches = float(input("Enter inches:"))
else:
  print("The program ends.")


#3
number = input("Enter a number:")
nums = []
while number != " ":
  number = float(number)
  nums.append(number)
  number = input("Enter a number:")
  if number == " ":
     print("quit")
     break
  else:
   number = float(number)
   nums.append(number)
max = max(nums)
min = min(nums)
print("The largest number:",max,". The smallest number:",min)


#4
import random
num_4 = random.randint(1, 10)
num_guess = int(input("Enter a integer:"))
while num_guess > num_4:
    print("Too high")
    num_guess = int(input("Enter a integer:"))
while num_guess < num_4:
    print("Too low")
    num_guess = int(input("Enter a integer:"))
else:
    print("Correct")


#5
username = str(input("Enter username:"))
password = str(input("Enter password:"))
if username != "python" or password != "rules":
 i = 1
 while i < 5:
    username = str(input("Enter username:"))
    password = str(input("Enter password:"))
    if username == "python" and password == "rules":  #为什么这里加welcome 会打印两次welcome
        break
    i = i + 1
 if i >= 5:
    print("Access denied")
if username == "python" and password == "rules":
 print("Welcome")


#6
import random
x = random.randrange(-1,1)
y = random.randrange(-1,1)
N = int(input("Enter the number of random points:"))
circle = 0
n = N
while N > 0:
    if x**2 + y**2 <= 1:
     circle = circle + 1
    x = random.randrange(-1, 1)
    y = random.randrange(-1, 1)
    N = N - 1
pi = 4 * (circle/n)
print("pi =", pi)
