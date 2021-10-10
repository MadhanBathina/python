def plusMinus(arr):
    # Write your code here
    plus_num=0
    minus_num=0
    zero_count=0
    for i in range(0,len(arr)):
        if arr[i]>0:
            plus_num+=1
        elif arr[i]<0:
            minus_num+=1
        else:
            zero_count+=1
    print('proportion of positive values',plus_num/n)
    print('proportion of negative values',minus_num/n)
    print('proportion of zeros',zero_count/n)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
