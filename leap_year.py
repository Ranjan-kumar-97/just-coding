def leap_year():
    n = int(input("Please Enter a Year:  "))
    if n%4==0:
        if n%100==0 and n%400==0:
            print(n," is a Leap Year")
        else:
            print(n, " is not a Leap Year")
    else:
        print(n, " is not a Leap Year")


leap_year()
