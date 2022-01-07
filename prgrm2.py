'''
num = 14

for count in range(1, 11):
    print(num, 'x', count, '=',
          num * count)
'''

'''
lower = 100
upper = 2000

for num in range(lower, upper + 1):

    order = len(str(num))

    sum=0
    temp=num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //=10

    if num == sum:
        print(num)
'''

'''
num = 16

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
    print("The sum is",sum)  
'''

'''
nterms = 10

n1=0
n2=1
count=0

if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence upto",nterms,":")
    while count < nterms:
        print(n1,end=',')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
print()
'''

'''
dec = 344

print("The decimal value of",dec,"is:")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal:")
'''
'''
c = 'p'

print("The ASCII value of '" + c + "' is ",ord(c))
'''
'''
def computeHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 = 54
num2 = 24

print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))


def computeHCF(x, y):
    while(y):
        x,y = y, x % y
    return x
print(computeHCF(300,400))
'''
'''
def 1cm(x, y):

   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0))
            1cm = greater
            break
       greater += 1
   return 1cm
num1 = 54
num2 = 24
'''
'''
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
def 1(x, y):
    1 = (x*y)//gcd(x,y)
    
num1 = 54
num2 = 24
'''

'''
def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1,x + 1) :
        if x % i == 0:
            print (i)
num= 235
print_factors(num)
'''

def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice =='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
    print("Invalid input")


'''

def add(x, y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice == '2':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice =='3':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice == '4':
    print(num1,"/",num2,"=",divide(num1,num2))
    print("Invalid input")




