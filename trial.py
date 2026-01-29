# a=[1,2,3,4]
# print(a)
# a.append(5)
# print(a[0:3])
# print(a[3:4])
# print(a[0:5:2])
# print(a[-1])
# c={True, False, True, "ABC", 2}
# print(c)

# import numpy as np
# a=(1,2,3,4)
# b=np.array(a)
# print(type(b))

# for x in a:
#     if x==3:
#         print("numpy")
#     if x==4:
#         print("pandas")


# i=1
# while i<5:
#     if i%2==0:self
#         print(i)
#     i=i+1

# a=int(input("Enter first number \t"))
# b=int(input("Enter second number \t"))
# if a>b:
#     print("First number is greater.")
# elif a==b:
#     print("Both numbers are equal.")
# elif a<b:
#     print("Second number is greater")

# sum=0
# for i in range(1,4,2):
#     sum+=i
# print(sum)

# def find_even(start, end):
#     for x in range(start, end):
#         if x%2==0:
#             print(x)

# def find_odd(start, end):
#     for x in range(start, end):
#         if x%2!=0:
#             print(x)

    
# def take_input():    
#     a=int(input("Enter start of range:"))
#     b=int(input("Enter end of range:"))
#     logic=input("Enter E for even, O for odd:")
#     if logic=="E":
#         find_even(a,b)
#     elif logic=="O":
#         find_odd(a,b)

# take_input()

# vowels='aeiou'
# str1='powerful'
# def find_vowels(vowels,str1):
#     for y in str1:
#         if y in vowels:
#             print(y)
# find_vowels(vowels,str1)

# import matplotlib.pyplot as plt
# plt.ion()
# x=[1,2,3,4]
# y=[10,20,30,40]
# plt.plot(x,y,marker='*')
# plt.show
# input("Enter")

# class Person:
#     age=21
    
#     def show_age(self):
        
#         print(self.age)
#     def update_age(self, add):
#         self.age+=add
#         print(self.age)

# p1=Person()
# p1.show_age()

# add=int(input("Add: "))
# p1.update_age(add)
# p1.age=48
# p1.show_age()

# class Displayer:
#     def __init__(self, message, n):
#         self.n=n
#         self.message=message
    
#     def show(self):
#         for x in range(0,self.n):
#             print(self.message)

# message=input("Enter message to be displayed: ")
# n=int(input("Enter number of times: "))
# d1=Displayer(message, n)
# d1.show()



# x=5
# y=10
# try:
#     z=x/y
#     print(z)
# except:
#     # if e == ZeroDivisionError:
#     print("Cant divide by zero")

class cal:
    def __init__(self, x,y,numbers,n):
        self.x=x
        self.y=y
        self.numbers=numbers
        self.n=n

    def divide(self):
        try:
            div=x/y
            print(div)
        except ZeroDivisionError:
            print("The Divisor cannot be zero(0).")
    
    def array_view(self):
        try:
            print(self.numbers[self.n])
        except IndexError:
            print("Index out of bound")
    
x=int(input("Enter the dividend: "))
y=int(input("Enter the divisor: "))
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
n=int(input("Array index to be viewed:"))
case1=cal(x,y,numbers,n)
case1.divide()
case1.array_view()

