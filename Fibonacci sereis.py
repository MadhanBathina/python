#Fabinocci sereis:a series of numbers in which each number is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.

num0=input('Enetr a nterms value:')
count=0
if num0.isnumeric():
    n0=int(num0)
    n1=0
    n2=1
    if n0>1:
        print ('Fibonacci sereis : ')
        while count<n0:
            print(n1)
            n=n1+n2
            n1=n2
            n2=n
            count+=1
    elif n0==1 :
        print('Enter a nterms value above 1 to get fabinocci sereis.')
        print(n1)
    else:
        print("Please enter a nterms above 0.")
else:
    print('Syntax error')
    print('Enter numbers only.')
