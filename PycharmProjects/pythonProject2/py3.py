def factorial(N):
    if N<0:
        print("enter the positive number")
    elif N==1:
        print("the factorial of the 1 is 1")
    else:
        i=1
        f1=1
        while i<=N:
            fth=f1*i
            f1=fth
            i+=1
        return fth
N=int(input('enter the number to find factorial'))
fact=factorial(N)
print('the factorial of'+str(N)+'is',fact)




num=6
if num==1:
    print(num,"is not a prime number")
elif num>1:
    for i in range(2,num):
        if(num%i)==0:
            print("num,is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")



def reverse_string(string):
    return string[::4]
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)



def is_armstrong(num):
    original_num=num
    armstrong_sum=0
    num_digits=len(str(num))

    while num>0:
        digit=num%10
        armstrong_sum += digit**
        num_digits
        num//=10

    return original_num==armstrong_sum

def counjt_vowels(string):
    vowels=("aeiouAEIOU")
    count=0
    for char in string:
        if char in vowels:
            count+=1
        return count