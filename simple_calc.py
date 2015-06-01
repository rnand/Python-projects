def add(a,b):
        print a+b

def sub(a,b):
        print a-b

def mul(a,b):
        print a*b

def div(a,b):
        print a/b

def powr(a,b):
        print a**b

class num(object):
        def __init__(self):
                self.x=0
                self.y=0
        def get(self):
                self.x=int(raw_input("Enter the first number:"))
                self.y=int(raw_input("Enter the second number:"))


n=num()
n.get()
flag=True
while(flag):
        print "Press 1 for addition."
        print "Press 2 for subtraction."
        print "Press 3 for multiplication."
        print "Press 4 for division."
        print "Press 5 for taking the power."
        print "==============================="
        print "Press 7 to enter new numbers."
        print "PRESS 9 TO QUIT"
        choice=int(input("Enter your choice:"))
        if choice==1:
                add(n.x, n.y)
        elif choice==2:
                sub(n.x,n.y)
        elif choice==3:
                mul(n.x,n.y)
        elif choice==4:
                div(n.x,n.y)
        elif choice==5:
                powr(n.x,n.y)
        elif choice==7:
               n.get()
        elif choice==9:
                flag=False






