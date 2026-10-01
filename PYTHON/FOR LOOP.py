#s = range(1,6)
#for i in s:
    #print(i)
#s = "python"


#count = 0
#for i in s:
    #if i in 'aeiou':
        #count = count + 1
        #print("no.of vowels:",count)


#s = [1,2,3,4,5]
#k = [3,4,6,7,8,]
#for i in s:
    #if i in k:
       # print(i)


#str = "python language"
#reverse = " "
#for i in str:
    #reverse = i + reverse
#print(reverse)


#s = range(1,11)
#for i in s:
    #print(i)


#s = "python is programming language"
#words = s.split()
#count = 0
#for i in words:
   # count = count + 1
#print(count)


#n = int(input("enter n value: "))
#sum = 0
#for i in range(1 , n + 1):
   # sum = sum + i
#print(sum)

#n = int(input("enter n value: "))
#fact = 1
#for i in range(1,n + 1):
   # fact = fact * i
#print(fact)

#-------membership operator + if else condition (strings)------------
#main_string = "python is progrmming language"
#sub_string = "language"
#if sub_string in main_string:
    #print("true")
#else:
   # print("false")

#-------strings------
#k = "Python is a programming language"
#print(k.strip())
#print(len(k))
#print(k.lstrip())
#print(k.rstrip())
#print(k.swapcase())hg
#print(k.capitalize())
#print(k.count("programming"))
#print(k.replace("Python" , 'java'))
#print(k.endswith("python"))
#print(k.startswith("Python"))
#print(k.split())


#example of list
'''d = ['10','20','30','40','50']
print(len(d))
print(d.count('50'))
print(d.index('10'))
d.insert(4,500)
print(d)
print(d.pop())
print(d)
d.remove('30')
print(d)
d.append('60')
print(d)'''


#
'''def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
#f(3,2)  3 2 4 8 --->positional with default
#f(10,20,30,40) 10 20 30 40 --->positional arg
#f(25,50,arg4=100) 25 50 4 100 --->positional with default
#f(arg4=2,arg1=3,arg2=4) 3 4 4 2 ---->keyword arg
#f() error
#f(4,5,arg2=6)#error
#f(arg3=10,arg4=20,30,40) error
#f(4,5,arg3=5,arg5=6)'''


#keyword args
'''def f1(**a):
    print(a)
    print(type(a))
f1(a=10,b=20,c=30,d=40)'''





