Start=int(input('Starting intiger :'))
End=int(input('Ending intiger :'))

if Start < 0 :
    print('1 ) The numbers lessthan 0 is not supposed to be count as either odd or even.')
    print('2 ) {0} to -1 are not considered as per the above statement.'.format(Start))
    Start = 0
    
oddcount = 0
evencount= 0
for i in range (Start, End+1) :
    
    if i % 2 == 0 :
        evencount += 1
    else :
         oddcount += 1
    

print ('evencount={0}.'.format(evencount))
print ('oddcount={0}.'.format(oddcount))

