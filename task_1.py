#  find the LCM (least common multiple) of two number 
n1 = int(input("enter first number :"))
n2 = int(input("enter second number :"))
high=0
low=0
if n1>n2:
    high=n1
    low=n2
else:
    high=n2
    low=n1

if high%low==0:
    print(high, "is the LCM of ",n1,n2)
else:
    temp=high
    while True:
        if temp%low==0 and temp%high==0:
            print(temp, "is the LCM of",n1,n2)
            break
        temp+=high

#find the GCD (Greatest common divisor) for input of two numbers

n1=int(input("enter fst number :"))
n2=int(input("enter sec number :"))
small=0
lrg=0
gcd=0
if n1>n2:
    lrg =n1
    small=n2
else:
    lrg=n2
    small=n1

for i in range(1,small+1):
    if lrg%i==0 and small%i==0:
        gcd=i
print(gcd)



