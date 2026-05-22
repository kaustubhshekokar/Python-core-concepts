num=int(input("enter a no, to check it is prime or not"))

def prime_check(num):
   

    is_true=True
    if num==1:
        print("it is neither prime nor composite ")
        is_true=False
        

    for i in range(2,num):
        if num%i==0:
            is_true=False
    if is_true==True:
        print("it is prime")
    else:
        print("its not prime")    
            

prime_check(num)
         
   
#to reduce time complexity
import math
for i in range(2,math.ceil(num)+1):
        if num%i==0:
            is_true=False
      
    











