def matrix(a,b,c):
    mate = []
    for i in range(a):
        inner = []
        for j in range(b):
            inner.append(c)
        mate.append(inner)
    return mate


def betterMinor(a,i,j):
    A=b=0
    new=matrix(len(a)-1,len(a)-1,0)
    arrA=[]
    arrB=[]
    arrC=[]
    for x in range(len(a)):
        arrA.append(x)
        arrB.append(x)
        arrC.append(x)
    #print("arrA: ",arrA)
    arrA.remove(i)
    #print("arrA:",arrA)
    for p in arrA:
        arrB.remove(j)
        #print("arrB:",arrB)
        for q in arrB:
            #print("p:",p,"q:",q)
            new[A][b]=a[p][q]
            #print("New changed: ",new)
            arrB=arrC
            #print("arrB",arrB)
            #print("arrC",arrC)
            #print("A,b: ", A,b)
            b+=1
        arrA,arrC=[],[]
        for x in range(len(a)):
            arrA.append(x)
            arrC.append(x)
        b=0
        A+=1
    return new    
#a=[[1,2,3,4,1],[5,6,7,8,2],[9,10,11,12,3],[13,14,15,16,4],[1,2,3,4,5]]
#print(betterMinor(a,2,4))
#aryan's stamp of approval
#OK TESTED