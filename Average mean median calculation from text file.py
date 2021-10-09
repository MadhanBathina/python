
#open and read the text file data contains marks list
from math import floor

#Calculate the Average, mean, median
f=open("marks.txt",'r')
l=f.readline() # read line and store in l varaiable
k=0
c=0
m=[]
#s=len(l)
#print('find',l.find('0'))
#print('type',type(l))
#print('index',l[0])
#print('length-s',s)
#l1=False
for i in l.split(','):
    #print(i)
    #print(n)
    m=m+[i]
    k+=float(i)
    #print(k)
    c+=1
    #print(k)
if c%2==0:
    median=((c/2)+1)
    g=median-1
    #print('g',g)
    b=floor(g)
    print('median',m[b])
else:
    median=((c+1)/2)
    g=median-1
    #print('g',g)
    b=floor(g)
    print('median',m[b])

#print(k)
print('Mean',k/c)
#print('c',c)
#print(m)
#print(len(m))
#print(g)

    #j=l[i]
    #print('j',j)
    #if j==',' :
       # print('j2',j)
   # else:
      #  print('l')
    #if l.isalphacii:
     #   l1=True
    #  print(l1)
#for i in range(0,s):
    #k=+1
    #print(l[i])

        

#with open("marks.txt") as f:
 #   print(f.readlines())
