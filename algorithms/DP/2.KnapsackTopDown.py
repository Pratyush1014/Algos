def KnapSack (wt , val , N , w) :
	global dp 
	for i in range (N + 1) :
		for j in range (w + 1) : 
			if ( i == 0 ) or ( j == 0 ) :
				dp[i][j] = 0
			else :
				if (wt[i-1] > w) :
					dp[i][j] = dp[i-1][j]
				else :
					a = val[i-1] + dp[i-1][j-wt[i-1]]
					b = dp[i-1][j]
					dp[i][j] = max(a,b) 

	return dp[-1][-1]


N = int (input())
wt = list(map(int , input().split()))
val = list(map(int , input().split()))
w = int (input())

dp = [[-1 for j in range (w + 1)  ] for i in range (N+1)]


profit =  KnapSack(wt , val , N , w)
print(profit)
