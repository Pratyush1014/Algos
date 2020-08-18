def MaxProduct (N) :
	global arr , dp
	for i in range (N + 1) :
		for j in range (N + 1) :
			if ( i == 0) :
				dp[i][j] = 1
			elif (j == 0) :
				dp[i][j] = 1
			else :
				if (arr[i-1] > j) :
					dp[i][j] = dp[i-1][j]
				else :
					dp[i][j] = max(dp[i-1][j] , arr[i-1]*dp[i][j-arr[i-1]])
	return dp[-1][-1]

N = int(input("Enter a number : "))
arr = [i for i in range (N+1)]
dp = [[0 for i in range (N+1)] for j in range (N+1)]
print(MaxProduct(N))
