
#open and read the text file data contains marks list

#Calculate the Average, mean, median
from math import floor
file  = open("marks.txt",'r')
line  = file.readline() # read line and store in l varaiable
total = 0
count = 0
list_of_numbers = []
arranged_list = []
indexnum=0

for num in line.split(','):
    
    list_of_numbers = list_of_numbers + [int(num)]

    total+=float(num)

    count+=1
    
list_of_numbers.sort()


if count%2 == 0:
    medianindex=floor(count/2)
    print('median',list_of_numbers[medianindex])
else:
    medianindex=floor(((count+1)/2)-1)
    print('median',list_of_numbers[medianindex])


print('Mean',total/count)
