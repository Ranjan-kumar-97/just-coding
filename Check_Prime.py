def check_prime():
    num = int(input("Please Enter the Number to check Prime:  "))
    flag=1
    for i in range(2,num):
        if num%i==0:
            flag=0
            print(num," is not a prime number" )
            print(i, "times", num//i, "is", num)
            break
    if flag==1:
        print(num, "is a Prime Number")


check_prime()