
# Print next prime and previous prime of a given number
num = int(input("Enter a number: "))
next_num=num+1
pre_num=num-1
while True:
    for i in range(2, num+1):
        if next_num % i== 0 and pre_num%i==0:
            next_num += 1
            pre_num -= 1
            print("The next prime number is ",next_num)
            print("The previous prime number is :" ,pre_num) 
        else:
            print(" please enter again")
        break