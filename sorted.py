s=int(input())
j=[int(x) for x in input().split()]
j.sort()
for i in range(0,s):
		if(i<s-1):
				k=' '
		else:
				k=''
		print(j[i],end=k)
