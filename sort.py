p=int(input())
b=[int(x) for x in input().split()]
b.sort()
for i in range(0,p):
		if(i<p-1):
				k=' '
		else:
				k=''
		print(b[i],end=k)
