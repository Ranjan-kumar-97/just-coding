def largest():
    n = int(input("Please Enter how many Numbers you want to Compare:  "))

    i=1
    larg=0
    if n<2:
        print("Not Comparable")
    else:
        while i<=n:
            tmp=str(i)
            temp = int(input("Enter " +  tmp + " Number :  "))
            if temp > larg:
                larg = temp
            i+=1
    print(larg, "is the Largest Number in given", n , "Numbers" )


largest()




