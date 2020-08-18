def rodcut (l , N) :
	global size , value
	if (N == 0) :
		return 0
	elif (l == 0) :
		return 0
	else :
		if (size[N-1] > l ) :
			return rodcut(l , N-1)
		else :
			return max(rodcut(l,N-1) , value[N-1] + rodcut(l-size[N-1],N))

l = int(input("Enter length : "))
N = int(input("Enter arr size : "))
size = list(map(int , input().split()))
value = list(map(int , input().split()))
profit = rodcut(l,N)
print(profit)
