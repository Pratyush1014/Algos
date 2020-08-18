def MCM (i , j) :
	global arr,dp
	if (dp[i][j] != -1) :
		return dp[i][j]
	if (i >= j) :
		dp[i][j] = 0
		return dp[i][j]
	else :
		product = float('inf')
		for k in range (i,j) :
			a = MCM (i,k) + MCM (k+1,j) + arr[i-1]*arr[k]*arr[j]
			if (a < product) :
				product = a
				dp[i][j] = product
		return dp[i][j]
N = int(input())
arr = list(map(int , input().split()))
dp = [[ -1 for i in range (N+1)] for i in range (N+1)]
product = MCM (1 , N-1)
print(dp[1][N-1])
