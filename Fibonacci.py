def fibonacci():
    first = int(input("Enter Starting Number:  "))
    second = int(input("Enter Second Number:  "))
    terms = int(input("Enter Number of Terma:  "))
    count=0
    print("Fibonnaci Series is :  ")
    while count<terms:
        print(first, end=' , ')
        temp=first+second
        first=second
        second=temp
        count+=1
        

        
fibonacci()