def CoinChange (N,n) :
	global dp,darr
	if (dp[N][n]) :
		return dp[N][n]
	if (N == 0) :
		dp[N][n] = 1
		return dp[N][n]
	elif (n == 0) and (N != 0):
		dp[N][n] = 0
		return dp[N][n]
	else :
		if (darr[n-1] > N) :
			dp[N][n] = CoinChange(N,n-1)
		else :
			dp[N][n] = CoinChange(N,n-1) + CoinChange(N-darr[n-1] , n)
		return dp[N][n]

N = int(input("Enter the coin : "))
n = int(input("No of denoms : "))
darr = list(map(int , input().split()))
dp = [[0 for i in range (n+1)] for j in range (N+1)]
print(CoinChange(N,n))

