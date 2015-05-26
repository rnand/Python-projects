n=int(raw_input("Enter the number of terms:"))
first=0
second=1

if n==1:
        print first

if n==2:
        print first
        print second

if n>2:
        print first
        print second
                
        for i in range(2,n):
                fib=first+second
                print fib
                first=second
                second =fib
