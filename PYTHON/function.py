#area of circle
'''radius = int(input("enter radius of circle: "))
def area(a,b):
    result = 3.14 * radius**2
    print(result)
area(3.14,3)'''


#square of numbers
'''s = int(input("enter any number: "))
def square(a):
    result = s**2
    print(result)
square(4)'''


#shopping
'''a = int(input("enter cost of pen: "))
b = int(input("enter the pen quantity: "))
def shopping(a,b):
    result = a*b
    print(result)
shopping(7,8)'''

#odd and even
'''def even(number):
    if number%2==0:
        print( number,"is even")
    else:
        print(number,"not even")
even(19)'''


#return statements
'''def add(a,b):
    return a+b
result = add(9,6)
print("the sum is: ",result)'''


#type of args
'''
1.positional
2.keyword
3.default
4.variable-length
'''
#1.positional
'''def  greet(name,wish):
    print("hello",name,wish)
greet('avinash','good morning')'''

#2.keyword
'''def greet(name,wish):
    print("Hello",name,wish)
greet(name = "avinash",
    wish = "good morning")'''


#task
'''def sum_sub(a,b):
    sum = a + b
    sub = a - b
    result = sum , sub
    print(result)
sum_sub(100,500)
sum_sub(500,100)'''

#task on keyword
'''def greet(name,age,city):
    print(name,age,city)
greet(name = 'Name: dhatri',
      age = 'Age: 18',
      city ='City: kadapa')'''
  
#default
'''def greet(name='ravi'):
    print("hello",name)
greet()'''

'''def greet(name='ravi',age='25'):
    print("hello",name,age)
greet()'''

'''def greet(name='dhatri',age='18'):
    print("hello",name,age)
greet()'''

'''def movie(hero='bob'):
    print('hi',hero)
movie()'''


#variable-length
'''def greet(*args):
    result = a + b
    print(result)'''


'''def f1(*a):
    print(a)
f1(10,20,30)'''

'''def f1(*a):
    print(*a)
f1(1,2,3)'''

'''def f2(n1,*s):
    print(n1)
    print(*s)
f2(10,'a',20,'b',30,'c')'''

#-----------------------------
'''def mul(a,b):
    return a * b
print(mul(3,4))'''
#------------------------------


'''def f3(*s,n2):
    print(s)
    print(n2)
f3(10,'a',20,'b',30,n2='c')'''






