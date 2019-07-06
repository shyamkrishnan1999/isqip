if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    A=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                B=[]
                if(i+j+k!=n):
                    B.append(i)
                    B.append(j)
                    B.append(k)
                    A.append(B)
        
print(A)
