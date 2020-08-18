def MCM (i , j) :
	global arr
	if (i == j) :
		return 0
	else :
		product = float('inf')
		for k in range (i,j) :
			a = MCM (i , k) + MCM (k+1 , j) + arr[i-1]*arr[k]*arr[j]
			if (a < product) :
				product	= a	
		return product
N = int(input())
arr = list(map(int , input().split()))
product = float('inf')
product = MCM (1 , N-1)
print(product)
