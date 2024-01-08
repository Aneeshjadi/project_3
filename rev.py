n=int(input("enter any number"))
m=n
rev=0
while(n>0):
	r=n%10
	rev=rev*10+r
	n=n//10
if (rev==m):
	print("no is palin",rev)
else:
	print("no not palin",rev)