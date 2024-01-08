n=int(input("enter no of rows"))
for i in range (0,n):
	for k in range (5-i,1,-1):
		print(" ",end=" ")
	for j in range (1,i+1):
		print(j,end=" ")
	for l in range (5-k,0):
		print(l,end=" ")
	print()





      