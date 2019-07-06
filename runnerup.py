if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    maxindex=0
    for i in range(0,n):
        if(arr[maxindex]<arr[i]):
            maxindex=i
    arr.sort()        
    c=arr.count(arr[i])
    print(arr[i-c])
