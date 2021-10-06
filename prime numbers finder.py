nt=input('Enter a value : ')
if nt.isnumeric():
    nt1=int(nt)
    for l in range (0,nt1):
        n=input('Enter a Number :')
        if n.isnumeric():
            n1=int(n)
            notprime = False
            if n1>1:
                for i in range (2, n1):
                    if (n1%i) == 0 :
                        notprime = True
                        break
            if notprime:
                print(n,'is a Composite number')
            else :
                print(n,'is a Prime number')
        else :
            print(n,'is invalid. Please enter a number')
else :
    print(nt,'is invalid. Please enter a valid number')
