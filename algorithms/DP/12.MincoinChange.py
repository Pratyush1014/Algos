def MinCoinChange (N , n) :
	global darr , dp
	for i in range (n + 1) :
		for j in range (N + 1) :
			if (j == 0) :
				dp[i][j] = 0
			elif (i == 0) :
				dp[i][j] = float('inf')
			else :
				if (darr[i-1] > j) :
					dp[i][j] = dp[i-1][j]	
				else :
					dp[i][j] = min(dp[i-1][j] ,1 + dp[i][j-darr[i-1]])
	return dp[-1][-1]


N = int(input("Enter the value : "))
n = int(input("Enter denoms : "))
darr = list(map(int , input().split()))
dp = [[0 for i in range (N+1)]for j in range(n+1)]
print(MinCoinChange(N,n))
