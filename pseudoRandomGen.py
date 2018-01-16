from math import sqrt
import sys

def GCD(b,m):
    while(b!=0):
        try:
            rem=b%m
            b=m
            m=rem
        except Exception as e:
            break
    if b==1:
        print("The numbers don't violetes the first rule.")
    else:
        print("The numbers violetes the first rule.")
        print(b)
        sys.exit()
    return b

def primeFactorization(a,m):
    n=0
    n=m
    prime=True
    factList=[]
    if m%2==0:
        while m%2==0:
            print(2)
            m=m/2
            factList.append(2)
        
        for i in range(3,int(sqrt(m))+1,2):
                while m % i==0:
                    print(i)
                    m=m/i

        checkPrime(n,prime)
        if (a-1)%factList[0]==0:
            print("It does not violetes the second rule too")
        else:
            print("It violetes the second rule")
            sys.exit()
    else:
        for i in range(3,int(sqrt(m))+1,2):
                while m % i==0:
                    print(i)
                    m=m/i

        checkPrime(n,prime)
        if (a-1)%m==0 or prime:
            print("It does not violetes the second rule too")
        else:
            print("It violetes the second rule")
            sys.exit()        
    
def checkPrime(m,prime):
    if m>1:
        for i in range(2,m):
            try:
                if (m%i)==0:
                    prime=False
                    break
            except Exception:
                break
        if prime==True:
            print("m is prime number")
            return prime
        else:
            print("m is not prime")
            return prime
    else:
        print("1 cannot be a prime number")

def checkThirdRule(a):
    if (a-1)%4==0:
        print("It does not violetes the third rule too.Congrats")

    else:
        print("It violetes the third rule")
        sys.exit()
        

if __name__=="__main__":
    print("We are going to create pseudo random numbers")
    a=int(input("Enter the num of constant multiple:"))
    b=int(input("Enter the num of increment:"))
    m=int(input("Enter the num of modulus:"))
    GCD(b,m)
    primeFactorization(a,m)
    checkThirdRule(a)
    
    x=0

    num=int(input("How many times do you want to generate random numbers:"))
    for i in range(num):
       x=(x*a+b)%m
       print(x)
       
