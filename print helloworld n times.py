#n=str(input('Enter a value : '))
n= input('Enter a value : ')
if n.isnumeric():
    y=int(n)
    if y>0:
        for i in range (0,y):
            print('Hello world')
    else :
        print(n,'is invalid ')
else :
    print(n,'is invalid')

