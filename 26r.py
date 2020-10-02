print("prime number in between 100 to 200 :")
for a in range (100,200):
	s=a
	b=1
	for e in range (2,a):
			if (a%e==0):
				b=0
				break
	if (b!=0):
		print(a,end=" ")
