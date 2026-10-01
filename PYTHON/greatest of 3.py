#n1 = int(input("enter first number: "))
#n2 = int(input("enter second number: "))
#n3 = int(input("enter third number: "))
#if n1 > n2 and n1 > n3:
    #print(n1,"larger is ")
#elif n2 > n1 and n2 > n3:
    #print(n2,"larger is ")
#else:
    #print("larger is ",)


#username = input("enter username: ")
#password = input("enter password: ")
#if username == "admin":
    #if password == "python1234":
        #print("login successfull")
    #else:
        #print("try again")
#else:
    #print("invalid")

#balance = 10000
#amount = int(input("enter amount: "))
#if balance > 0:
    #if amount <= balance:
        #print("withdraw successful")
    #else:
       # print("insuffient balance")
#else:
    #print("invalid")



#marks = int(input("enter marks: "))
#if marks >= 80:
        #print("eligible for scholorship")
#elif marks >= 40:
        #print("pass,you are not eligible")
#else:
       # print("fail")

marks = int(input("enter marks: "))
if marks >= 40:
    if marks >= 80:
        print("eligible for scholorship")
    else:
        print("pass,you are not eligible")
else:
    print("you are fail")
