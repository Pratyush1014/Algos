def Subsetsum (N , s) :
	global arr 
	dp = [[False for i in range (s+1)]for i in range (N + 1) ]
	
	for i in range (N+1) :
		for j in range (s + 1) :
			if ( i == 0 ) :
				dp[i][j] = False  
			if (j == 0) :
				dp[i][j] = True
			else :
				dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
	print(dp[-1][-1])


N = int (input())
arr = list(map(int , input().split()))
s = int(input())

su = sum(arr)
if (su % 2 == 0) :
	Subsetsum(N , su//2)
else :
	print ("No") 
