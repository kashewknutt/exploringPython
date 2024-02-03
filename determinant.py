from betterMinor import betterMinor

def det(a):
    if len(a)==1:
        ans = a[0][0]
    else:
        ans = 0
        for j in range(len(a)):
            #print("minor",betterMinor(a,0,j))
            ans += ((-1)**(j))*det(betterMinor(a,0,j))*a[0][j]
            #print("ans",ans)
    return ans



