#creating a functions(global variable)
'''a = 'this is global variable'
b = 10
def l():
    print(a)
    print(b)
def l1():
    print(a)
    print(b)
l()
l1()'''
#creating a function(local variable)
'''def g():
    a = 'this is local variable'
    b = 10
    print(a)
    print(b)
def f():#NameError
    print(a)
    print(b)
g()
f()'''

#lambda function
'''a = lambda n:n*n
print(a(8))'''

#adding two numbers
'''s = lambda n,m:n+m
print(s(3,4))'''

#even or odd
'''s = lambda n:n%2==0
print(s(3))'''

#greater of 2 numbers
'''s =lambda u,k:u>k or u<k
print(s(76,90))'''

#Recursive function
'''def factorial(n):
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        return result
print(factorial(5))'''

#palindrome
'''def palindrome(n):
    if n == n[::-1]:
     return "it is a palindrome"
    else:
       result = "not a palindrome"
       return result
print(palindrome("mom"))'''


