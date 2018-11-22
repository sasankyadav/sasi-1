b=int(input())
s=[int(x) for x in input().split()]
m=int((b+1)/2)
if(m%2==0):
		print(s[m-1],s[m])
else:
		print(s[m-1])
