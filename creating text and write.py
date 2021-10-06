n=int(input())
try:
    file=open('write.txt', 'w')
    for i in range (0,n+1):
        file.write("%d \n" % i)
finally:
    file.close()
