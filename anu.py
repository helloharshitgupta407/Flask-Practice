x=[]
n=int(input())
for i in range(n):
    b=input().split()
    x.append(b)
x.sort(key=lambda x: x[1])
y=[]
y.append(x[1][0])
for i in range(1,len(x)-1):
    if float(x[i][1])==float(x[i+1][1]):
        y.append(x[i+1][0])
    else:
        break
z=sorted(y)
print("\n".join(z))