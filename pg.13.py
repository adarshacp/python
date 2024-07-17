def towerofhanoi(n,source,destination,auxilary):
    if n==1:
        print("move disk 1 from",source,"to",destination)
        return
    towerofhanoi(n-1,source,auxilary,destination)
    print("move disk",n,"from",source,"to",destination)
    towerofhanoi(n-1,auxilary,destination,source)
n=4
towerofhanoi(n,'A','B','C')
