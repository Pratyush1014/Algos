def UKnapsack (N , s) :
	global dp , wt, val
	for i in range (N + 1) :
		for j in range (s + 1) :
			if (i == 0) :
				dp[i][j] = 0
			elif (j == 0) :
				dp[i][j] = 0
			else :
				if (wt[i-1] > s) :
					dp[i][j] = dp[i-1][j]
				else :
					dp[i][j] = max(dp[i-1][j],val[i-1]+dp[i][j-wt[i-1]])
	return dp[-1][-1]



N = int (input("Enter the number of inputs : "))
wt = list(map(int , input().split()))
val = list(map(int , input().split()))
max_cap = int(input("Enter max cap : "))
dp = [[0 for i in range(max_cap + 1)]for j in range(N + 1)]
print(UKnapsack(N,max_cap))
