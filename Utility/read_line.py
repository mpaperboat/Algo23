def read_line(*a):
    r=input().split()
    for i in range(len(r)):
        r[i]=a[min(i,len(a)-1)](r[i])
    return r